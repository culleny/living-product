import logging

logger = logging.getLogger(__name__)

def execute(job_id, image_url, s3_client):
    """
    Step 0 (Alternative): 2D Image Input
    - Accept a 2D product image instead of 3D model
    - Upload to S3 as starting point
    - Skip 3D rendering step
    """
    logger.info(f"[Step 0] Using 2D image input for job {job_id}")
    
    # Store in S3
    s3_key = f"{job_id}/step0_input_image.jpg"
    s3_url = s3_client.upload_from_url(image_url, s3_key)
    
    logger.info(f"[Step 0] Complete: {s3_url}")
    
    return {
        "render_url": s3_url,
        "source": "2d_image"
    }
