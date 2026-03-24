import logging

logger = logging.getLogger(__name__)

def execute(job_id, step3_output, adobe_client, s3_client):
    """
    Step 6: Ad Format Crops
    - Take hero image
    - Generate multiple aspect ratios via reframe API
    - Formats: 9:16 story, 1:1 square, 16:9 banner
    - Store all in S3
    """
    logger.info(f"[Step 6] Starting reframe for job {job_id}")
    
    hero_url = step3_output["branded_hero_url"]
    
    formats = {
        "story": {"width": 1080, "height": 1920},  # 9:16
        "square": {"width": 1080, "height": 1080},  # 1:1
        "banner": {"width": 1920, "height": 1080}   # 16:9
    }
    
    results = {}
    
    for format_name, dimensions in formats.items():
        try:
            # Reframe to target dimensions
            reframed_url = adobe_client.reframe_image(
                hero_url, 
                dimensions["width"], 
                dimensions["height"]
            )
            
            # Store in S3
            s3_key = f"{job_id}/step6_{format_name}.jpg"
            s3_url = s3_client.upload_from_url(reframed_url, s3_key)
            
            results[f"{format_name}_url"] = s3_url
            logger.info(f"[Step 6] Generated {format_name}: {s3_url}")
        
        except Exception as e:
            logger.error(f"[Step 6] Reframe failed for {format_name}: {e}")
            results[f"{format_name}_url"] = None
    
    return results
