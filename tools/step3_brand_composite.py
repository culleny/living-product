import logging

logger = logging.getLogger(__name__)

def execute(job_id, step2_output, brief_params, adobe_client, s3_client):
    """
    Step 3: Brand Composite
    - Generate background based on campaign brief
    - Composite cleaned product onto background
    - Apply brand template (if provided)
    - Store final branded hero in S3
    """
    logger.info(f"[Step 3] Starting brand composite for job {job_id}")
    
    cutout_url = step2_output["cutout_url"]
    
    try:
        # Generate branded background
        background_prompt = f"{brief_params['environment']}, {brief_params['mood']} mood, {', '.join(brief_params['colors'])} color palette, high quality, photorealistic"
        
        background_url = adobe_client.generate_background(background_prompt)
        
        # Composite product onto background
        composite_url = adobe_client.composite_images(background_url, cutout_url)
        
        # Store in S3
        s3_key = f"{job_id}/step3_branded_hero.jpg"
        s3_url = s3_client.upload_from_url(composite_url, s3_key)
        
        logger.info(f"[Step 3] Complete: {s3_url}")
        
        return {
            "branded_hero_url": s3_url
        }
    
    except Exception as e:
        logger.error(f"[Step 3] Brand composite failed: {e}")
        logger.warning("[Step 3] Falling back to cutout")
        
        # Fallback: use cutout from step 2
        return {
            "branded_hero_url": cutout_url,
            "fallback": True
        }
