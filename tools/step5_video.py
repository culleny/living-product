import logging

logger = logging.getLogger(__name__)

def execute(job_id, step3_output, brief_params, adobe_client, s3_client):
    """
    Step 5: Image to Video
    - Take branded hero image
    - Generate video with motion prompt
    - Poll for completion with progress updates
    - Store in S3
    """
    logger.info(f"[Step 5] Starting image-to-video for job {job_id}")
    
    hero_url = step3_output["branded_hero_url"]
    
    try:
        # Create motion prompt from brief params
        motion_prompt = ", ".join(brief_params.get("motion_keywords", ["smooth camera movement", "cinematic"]))
        
        # Generate video (this is optional, can fail gracefully)
        video_url = adobe_client.image_to_video(hero_url, motion_prompt)
        
        # Store in S3
        s3_key = f"{job_id}/step5_video.mp4"
        s3_url = s3_client.upload_from_url(video_url, s3_key)
        
        logger.info(f"[Step 5] Complete: {s3_url}")
        
        return {
            "video_url": s3_url
        }
    
    except Exception as e:
        logger.error(f"[Step 5] Video generation failed: {e}")
        logger.warning("[Step 5] Continuing without video (optional step)")
        
        # Video is optional - continue pipeline
        return {
            "video_url": None,
            "error": str(e)
        }
