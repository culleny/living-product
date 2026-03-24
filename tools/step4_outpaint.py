import logging

logger = logging.getLogger(__name__)

def execute(job_id, step3_output, adobe_client, s3_client):
    """
    Step 4: Outpaint to Billboard
    - Take branded hero image
    - Extend to 1920x1080 landscape format
    - Store in S3
    """
    logger.info(f"[Step 4] Starting outpaint for job {job_id}")
    
    hero_url = step3_output["branded_hero_url"]
    
    try:
        # Outpaint to billboard dimensions
        billboard_url = adobe_client.outpaint_image(hero_url, 1920, 1080)
        
        # Store in S3
        s3_key = f"{job_id}/step4_billboard.jpg"
        s3_url = s3_client.upload_from_url(billboard_url, s3_key)
        
        logger.info(f"[Step 4] Complete: {s3_url}")
        
        return {
            "billboard_url": s3_url
        }
    
    except Exception as e:
        logger.error(f"[Step 4] Outpaint failed: {e}")
        logger.warning("[Step 4] Skipping billboard format")
        
        return {
            "billboard_url": None,
            "error": str(e)
        }
