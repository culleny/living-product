import logging
import os

logger = logging.getLogger(__name__)

def execute(job_id, model_url, campaign_brief, adobe_client, s3_client):
    """
    Step 1: 3D Composite Render
    - Upload 3D model to Firefly Space
    - Render product into photorealistic background
    - Store result in S3
    """
    logger.info(f"[Step 1] Starting 3D composite for job {job_id}")
    
    # Extract filename from URL
    filename = os.path.basename(model_url)
    
    # Create or reuse Space
    space_name = f"living-product-{job_id}"
    space_id = adobe_client.create_space(space_name)
    
    # Upload model to Space
    asset_id = adobe_client.upload_to_space(space_id, model_url, filename)
    
    # Generate composite render
    render_url = adobe_client.render_3d_composite(space_id, asset_id, campaign_brief)
    
    # Store in S3
    s3_key = f"{job_id}/step1_hero_render.jpg"
    s3_url = s3_client.upload_from_url(render_url, s3_key)
    
    logger.info(f"[Step 1] Complete: {s3_url}")
    
    return {
        "space_id": space_id,
        "asset_id": asset_id,
        "render_url": s3_url
    }
