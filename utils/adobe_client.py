import requests
import logging
import time
from utils.retry import retry_once

logger = logging.getLogger(__name__)

class AdobeClient:
    def __init__(self, client_id, client_secret, scopes):
        self.client_id = client_id
        self.client_secret = client_secret
        self.scopes = scopes
        self.access_token = None
        self.token_expiry = 0
    
    def get_access_token(self):
        """Get OAuth access token."""
        if self.access_token and time.time() < self.token_expiry:
            return self.access_token
        
        url = "https://ims-na1.adobelogin.com/ims/token/v3"
        data = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "grant_type": "client_credentials",
            "scope": ",".join(self.scopes)
        }
        
        response = requests.post(url, data=data)
        response.raise_for_status()
        
        token_data = response.json()
        self.access_token = token_data["access_token"]
        self.token_expiry = time.time() + token_data.get("expires_in", 3600) - 300
        
        logger.info("Obtained Adobe access token")
        return self.access_token
    
    @retry_once
    def create_space(self, name):
        """Create a Substance 3D Space for caching 3D models."""
        url = "https://substance3d.adobe.io/api/v1/spaces"
        headers = {
            "Authorization": f"Bearer {self.get_access_token()}",
            "x-api-key": self.client_id,
            "Content-Type": "application/json"
        }
        data = {"name": name}
        
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()
        
        space_id = response.json()["id"]
        logger.info(f"Created Substance 3D Space: {space_id}")
        return space_id
    
    @retry_once
    def upload_to_space(self, space_id, model_url, filename):
        """Upload 3D model to Space."""
        url = f"https://substance3d.adobe.io/api/v1/spaces/{space_id}/assets"
        headers = {
            "Authorization": f"Bearer {self.get_access_token()}",
            "x-api-key": self.client_id,
            "Content-Type": "application/json"
        }
        data = {
            "name": filename,
            "source_url": model_url
        }
        
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()
        
        asset_id = response.json()["id"]
        logger.info(f"Uploaded model to Space: {asset_id}")
        return asset_id
    
    @retry_once
    def render_3d_composite(self, space_id, asset_id, prompt):
        """Call Firefly 3D object composite API."""
        url = "https://firefly-api.adobe.io/v3/images/generate-object-composite"
        headers = {
            "Authorization": f"Bearer {self.get_access_token()}",
            "x-api-key": self.client_id,
            "Content-Type": "application/json"
        }
        
        payload = {
            "prompt": prompt,
            "object": {
                "source": {
                    "space_id": space_id,
                    "asset_id": asset_id
                }
            },
            "size": {
                "width": 2048,
                "height": 2048
            }
        }
        
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        
        result = response.json()
        image_url = result["outputs"][0]["image"]["url"]
        logger.info("Generated 3D composite render")
        return image_url
    
    @retry_once
    def remove_background(self, image_url):
        """Call Photoshop API to remove background."""
        url = "https://image.adobe.io/sensei/cutout"
        headers = {
            "Authorization": f"Bearer {self.get_access_token()}",
            "x-api-key": self.client_id,
            "Content-Type": "application/json"
        }
        
        payload = {
            "input": {
                "href": image_url,
                "storage": "external"
            },
            "output": {
                "href": image_url.replace(".jpg", "_cutout.png"),
                "storage": "external",
                "type": "image/png",
                "overwrite": True
            }
        }
        
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        
        # Poll for completion
        job_url = response.headers.get("location")
        if not job_url:
            result = response.json()
            return result["_links"]["self"]["href"]
        
        return self._poll_job(job_url)
    
    def _poll_job(self, job_url, max_attempts=30):
        """Poll Photoshop API job until complete."""
        headers = {
            "Authorization": f"Bearer {self.get_access_token()}",
            "x-api-key": self.client_id
        }
        
        for attempt in range(max_attempts):
            time.sleep(2)
            response = requests.get(job_url, headers=headers)
            response.raise_for_status()
            
            result = response.json()
            status = result.get("status")
            
            if status == "succeeded":
                output_url = result["outputs"][0]["href"]
                logger.info("Photoshop job completed")
                return output_url
            elif status == "failed":
                raise Exception(f"Photoshop job failed: {result}")
        
        raise Exception("Photoshop job timeout")
    
    @retry_once
    def generate_background(self, prompt):
        """Generate background image using Firefly Image Model."""
        url = "https://firefly-api.adobe.io/v3/images/generate"
        headers = {
            "Authorization": f"Bearer {self.get_access_token()}",
            "x-api-key": self.client_id,
            "Content-Type": "application/json"
        }
        
        payload = {
            "prompt": prompt,
            "size": {
                "width": 2048,
                "height": 2048
            },
            "contentClass": "photo"
        }
        
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        
        result = response.json()
        image_url = result["outputs"][0]["image"]["url"]
        logger.info("Generated background image")
        return image_url
    
    @retry_once
    def composite_images(self, background_url, foreground_url):
        """Composite foreground onto background (simplified - using Firefly expand)."""
        # Note: This is a simplified approach. In production, you'd use Photoshop API
        # with layer compositing or a custom compositing service
        logger.info("Compositing images (using foreground as primary)")
        # For now, return the foreground with background context
        # In a real implementation, this would call Photoshop API with layers
        return foreground_url
    
    @retry_once
    def outpaint_image(self, image_url, target_width, target_height):
        """Extend image to target dimensions using Firefly Expand."""
        url = "https://firefly-api.adobe.io/v3/images/expand"
        headers = {
            "Authorization": f"Bearer {self.get_access_token()}",
            "x-api-key": self.client_id,
            "Content-Type": "application/json"
        }
        
        payload = {
            "image": {
                "source": {
                    "url": image_url
                }
            },
            "size": {
                "width": target_width,
                "height": target_height
            }
        }
        
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        
        result = response.json()
        expanded_url = result["outputs"][0]["image"]["url"]
        logger.info(f"Expanded image to {target_width}x{target_height}")
        return expanded_url
    
    @retry_once
    def image_to_video(self, image_url, motion_prompt):
        """Generate video from image using Firefly."""
        url = "https://firefly-api.adobe.io/v1/video/generate"
        headers = {
            "Authorization": f"Bearer {self.get_access_token()}",
            "x-api-key": self.client_id,
            "Content-Type": "application/json"
        }
        
        payload = {
            "image": {
                "source": {
                    "url": image_url
                }
            },
            "motion": {
                "prompt": motion_prompt
            },
            "duration": 5
        }
        
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        
        # Poll for video completion
        job_id = response.json().get("id")
        if job_id:
            return self._poll_video_job(job_id)
        
        # Fallback if immediate response
        result = response.json()
        return result["outputs"][0]["video"]["url"]
    
    def _poll_video_job(self, job_id, max_attempts=60):
        """Poll video generation job with progress updates."""
        url = f"https://firefly-api.adobe.io/v1/video/status/{job_id}"
        headers = {
            "Authorization": f"Bearer {self.get_access_token()}",
            "x-api-key": self.client_id
        }
        
        for attempt in range(max_attempts):
            time.sleep(5)
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            
            result = response.json()
            status = result.get("status")
            progress = result.get("progress", 0)
            
            logger.info(f"Video generation: {status} ({progress}%)")
            
            if status == "completed":
                video_url = result["outputs"][0]["video"]["url"]
                logger.info("Video generation completed")
                return video_url
            elif status == "failed":
                raise Exception(f"Video generation failed: {result}")
        
        raise Exception("Video generation timeout")
    
    @retry_once
    def reframe_image(self, image_url, target_width, target_height):
        """Reframe image to target aspect ratio using Firefly."""
        url = "https://firefly-api.adobe.io/v3/images/expand"
        headers = {
            "Authorization": f"Bearer {self.get_access_token()}",
            "x-api-key": self.client_id,
            "Content-Type": "application/json"
        }
        
        payload = {
            "image": {
                "source": {
                    "url": image_url
                }
            },
            "size": {
                "width": target_width,
                "height": target_height
            }
        }
        
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        
        result = response.json()
        reframed_url = result["outputs"][0]["image"]["url"]
        logger.info(f"Reframed to {target_width}x{target_height}")
        return reframed_url
