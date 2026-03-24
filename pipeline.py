#!/usr/bin/env python3
"""
Living Product Pipeline
Orchestrates AI-powered creative production from 3D model to marketing assets.
"""

import argparse
import json
import logging
import sys
from datetime import datetime

from utils.adobe_client import AdobeClient
from utils.s3_client import S3Client
from utils.bedrock_client import BedrockClient
from tools import (
    step1_3d_composite, 
    step2_bg_removal, 
    step3_brand_composite,
    step4_outpaint,
    step5_video,
    step6_reframe
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def load_config():
    """Load configuration from config.json."""
    with open('config/config.json', 'r') as f:
        return json.load(f)

def create_manifest(job_id, results, bucket_name):
    """Create job manifest for frontend gallery."""
    manifest = {
        "job_id": job_id,
        "timestamp": datetime.now().isoformat(),
        "bucket": bucket_name,
        "brief_params": results.get("brief_params", {}),
        "assets": {
            "hero_render": results.get("step1", {}).get("render_url"),
            "product_cutout": results.get("step2", {}).get("cutout_url"),
            "branded_hero": results.get("step3", {}).get("branded_hero_url"),
            "billboard": results.get("step4", {}).get("billboard_url"),
            "video": results.get("step5", {}).get("video_url"),
            "story": results.get("step6", {}).get("story_url"),
            "square": results.get("step6", {}).get("square_url"),
            "banner": results.get("step6", {}).get("banner_url")
        }
    }
    return manifest

def main():
    parser = argparse.ArgumentParser(description='Living Product Pipeline')
    parser.add_argument('--model-url', help='URL to 3D model (GLB/USDZ)')
    parser.add_argument('--image-url', help='URL to 2D product image (alternative to 3D model)')
    parser.add_argument('--brief', required=True, help='Campaign brief text')
    parser.add_argument('--job-id', help='Optional job ID (auto-generated if not provided)')
    
    args = parser.parse_args()
    
    # Validate input
    if not args.model_url and not args.image_url:
        parser.error('Either --model-url or --image-url is required')
    if args.model_url and args.image_url:
        parser.error('Provide either --model-url or --image-url, not both')
    
    # Generate job ID
    job_id = args.job_id or datetime.now().strftime('%Y%m%d-%H%M%S')
    logger.info(f"Starting pipeline for job: {job_id}")
    
    # Load config
    config = load_config()
    
    # Initialize clients
    adobe = AdobeClient(
        config['adobe']['client_id'],
        config['adobe']['client_secret'],
        config['adobe']['scopes']
    )
    
    s3 = S3Client(config['aws']['region'])
    bedrock = BedrockClient(config['aws']['region'])
    
    # Create S3 bucket
    bucket_name = s3.create_bucket(config['aws']['bucket_prefix'])
    logger.info(f"Using S3 bucket: {bucket_name}")
    
    # Interpret campaign brief with Claude
    logger.info("Interpreting campaign brief...")
    try:
        brief_params = bedrock.interpret_brief(args.brief)
        logger.info(f"Brief parameters: {json.dumps(brief_params, indent=2)}")
    except Exception as e:
        logger.warning(f"Bedrock not available: {e}")
        logger.info("Using fallback brief interpretation")
        # Simple fallback parsing
        brief_params = {
            "mood": "professional",
            "colors": ["vibrant", "natural"],
            "environment": args.brief,
            "motion_keywords": ["smooth", "elegant"]
        }
    
    # Execute pipeline steps
    results = {"job_id": job_id, "brief_params": brief_params}
    
    try:
        # Step 1: 3D Composite Render OR use 2D image
        if args.model_url:
            step1_result = step1_3d_composite.execute(
                job_id, args.model_url, args.brief, adobe, s3
            )
        else:
            # Use 2D image directly, skip 3D rendering
            logger.info(f"[Step 1] Using 2D image input, skipping 3D render")
            s3_key = f"{job_id}/step1_hero_render.jpg"
            s3_url = s3.upload_from_url(args.image_url, s3_key)
            step1_result = {"render_url": s3_url}
        
        results["step1"] = step1_result
        
        # Step 2: Background Removal
        step2_result = step2_bg_removal.execute(
            job_id, step1_result, adobe, s3
        )
        results["step2"] = step2_result
        
        # Step 3: Brand Composite
        step3_result = step3_brand_composite.execute(
            job_id, step2_result, brief_params, adobe, s3
        )
        results["step3"] = step3_result
        
        # Step 4: Outpaint to Billboard
        step4_result = step4_outpaint.execute(
            job_id, step3_result, adobe, s3
        )
        results["step4"] = step4_result
        
        # Step 5: Image to Video (optional)
        step5_result = step5_video.execute(
            job_id, step3_result, brief_params, adobe, s3
        )
        results["step5"] = step5_result
        
        # Step 6: Ad Format Crops
        step6_result = step6_reframe.execute(
            job_id, step3_result, adobe, s3
        )
        results["step6"] = step6_result
        
        # Write manifest to S3
        manifest = create_manifest(job_id, results, bucket_name)
        manifest_key = f"{job_id}/job_manifest.json"
        s3.s3.put_object(
            Bucket=bucket_name,
            Key=manifest_key,
            Body=json.dumps(manifest, indent=2),
            ContentType='application/json'
        )
        
        manifest_url = s3.s3.generate_presigned_url(
            'get_object',
            Params={'Bucket': bucket_name, 'Key': manifest_key},
            ExpiresIn=86400
        )
        
        logger.info("Pipeline complete!")
        logger.info(f"Manifest URL: {manifest_url}")
        logger.info(f"\nView gallery:")
        logger.info(f"  python view_gallery.py {manifest_url}")
        logger.info(f"\nResults: {json.dumps(results, indent=2)}")
        
        return results
    
    except Exception as e:
        logger.error(f"Pipeline failed: {e}", exc_info=True)
        sys.exit(1)

if __name__ == "__main__":
    main()
