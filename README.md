# Living Product Pipeline

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Adobe Firefly](https://img.shields.io/badge/Adobe-Firefly-FF0000.svg)](https://www.adobe.com/products/firefly.html)
[![AWS](https://img.shields.io/badge/AWS-S3%20%7C%20Bedrock-FF9900.svg)](https://aws.amazon.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Hackathon](https://img.shields.io/badge/Adobe%20Hackathon-Q1%202026-red.svg)](https://adobe.com)

AI-powered creative production pipeline that transforms a 3D product model into a complete marketing campaign pack in one run.

## What It Does

Input: 3D model (GLB/USDZ) OR 2D product image + campaign brief text
Output: 8 marketing assets ready for deployment

1. Hero render (3D product in photorealistic scene)
2. Product cutout (clean PNG with background removed)
3. Branded hero (product on generated background)
4. Billboard format (1920x1080 extended)
5. Video (5-second animated version)
6. Story format (9:16 vertical)
7. Square format (1:1)
8. Banner format (16:9)

## Quick Start

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Configure AWS credentials:

**Option A - Using setup script (recommended):**
```bash
bash setup_aws.sh
```

**Option B - Manual setup:**
```bash
mkdir -p ~/.aws
# Create ~/.aws/credentials with your AWS access keys
# Create ~/.aws/config with region=us-west-2
```

You'll need AWS credentials with permissions for:
- S3 (create buckets, upload objects)
- Bedrock (invoke Claude Sonnet model)

3. Test setup:
```bash
python test_setup.py
```

4. Run the pipeline:

**With 3D model:**
```bash
python pipeline.py \
  --model-url "https://example.com/model.glb" \
  --brief "luxury watch in sunset desert landscape"
```

**With 2D image (use a direct image URL):**
```bash
python pipeline.py \
  --image-url "https://images.unsplash.com/photo-1629203851122-3726ecdf080e" \
  --brief "refreshing beverage on tropical beach"
```

**Note:** For Adobe Stock images, download them first and upload to a public URL (S3, etc.)

5. View results:
```bash
python view_gallery.py <MANIFEST_URL>
```

See `EXAMPLES.md` for more usage examples.

## Pipeline Steps

✅ **Step 1:** 3D composite render (Firefly 3D API + Substance 3D Space)
✅ **Step 2:** Background removal (Photoshop API with fallback)
✅ **Step 3:** Brand composite with generated background
✅ **Step 4:** Outpaint to billboard (1920x1080)
✅ **Step 5:** Image-to-video with motion (optional, graceful failure)
✅ **Step 6:** Ad format crops (9:16 story, 1:1 square, 16:9 banner)
✅ **Step 7:** Static gallery with manifest

## Viewing Results

After pipeline completes, it outputs a manifest URL. View the gallery:
```bash
python view_gallery.py <MANIFEST_URL>
```

Or manually open `frontend/index.html?manifest=<MANIFEST_URL>` in your browser.

## Architecture

- `pipeline.py` - Main orchestrator script (runs all 6 steps sequentially)
- `tools/` - Individual step implementations (step1-6)
- `utils/` - Adobe API, S3, Bedrock clients with retry logic
- `frontend/` - Static gallery (reads manifest from S3)
- `config/` - Configuration files

## Error Handling

- Step 5 (video): Optional, continues on failure
- Photoshop API failures: Falls back to Firefly outputs
- All API calls: Retry once on timeout/connection errors

## Configuration

Adobe credentials are pre-configured in `config/config.json`.
AWS credentials should be configured via `aws configure`.
