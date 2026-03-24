import logging
import tempfile
import requests

logger = logging.getLogger(__name__)

def execute(job_id, step1_output, adobe_client, s3_client):
    """
    Step 2: Background Removal
    - Take hero render from Step 1
    - Remove background via Photoshop API
    - Store cleaned PNG in S3
    """
    logger.info(f"[Step 2] Starting background removal for job {job_id}")
    
    render_url = step1_output["render_url"]
    
    try:
        # Call Photoshop cutout API
        cutout_url = adobe_client.remove_background(render_url)
        
        # Store in S3
        s3_key = f"{job_id}/step2_product_cutout.png"
        s3_url = s3_client.upload_from_url(cutout_url, s3_key)
        
        logger.info(f"[Step 2] Complete: {s3_url}")
        
        return {
            "cutout_url": s3_url
        }
    
    except Exception as e:
        logger.error(f"[Step 2] Background removal failed: {e}")
        logger.warning("[Step 2] Falling back to original render")
        
        # Fallback: use original render
        return {
            "cutout_url": render_url,
            "fallback": True
        }
