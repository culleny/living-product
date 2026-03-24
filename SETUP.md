# Living Product - Setup Guide

## Prerequisites

1. **Python 3.9+** ✓ (Installed)
2. **AWS CLI** (Not installed - needs setup)
3. **AWS Account** with credentials
4. **Adobe Firefly API Access** ✓ (Configured)

## Installation Steps

### 1. Install Dependencies

```bash
pip3 install -r requirements.txt
```

✓ **Status:** Complete

### 2. Install AWS CLI

**macOS:**
```bash
brew install awscli
```

Or download from: https://aws.amazon.com/cli/

### 3. Configure AWS Credentials

```bash
aws configure
```

You'll need:
- AWS Access Key ID
- AWS Secret Access Key
- Default region: `us-west-2`
- Default output format: `json`

### 4. Test Setup

```bash
python3 test_setup.py
```

This validates:
- Dependencies installed
- Config file valid
- AWS credentials working

## Running the Pipeline

### With 2D Image (Recommended for testing)

```bash
python3 pipeline.py \
  --image-url "https://images.unsplash.com/photo-1629203851122-3726ecdf080e" \
  --brief "refreshing beverage on tropical beach at sunset"
```

### With 3D Model

```bash
python3 pipeline.py \
  --model-url "https://example.com/model.glb" \
  --brief "luxury watch in desert landscape at golden hour"
```

## Viewing Results

After the pipeline completes, it will output a manifest URL. View the gallery:

```bash
python3 view_gallery.py <MANIFEST_URL>
```

Or open `frontend/index.html?manifest=<MANIFEST_URL>` in your browser.

## Troubleshooting

### AWS Credentials Not Found

Run `aws configure` and enter your credentials.

### Adobe API Errors

Check that your client ID and secret in `config/config.json` are correct.

### S3 Bucket Creation Fails

Ensure your AWS account has permissions to create S3 buckets.

## Next Steps

1. Install AWS CLI
2. Configure AWS credentials
3. Run a test with a 2D image
4. View the generated gallery
5. Try with your own product images or 3D models

## Support

For Adobe Firefly API documentation:
- https://developer.adobe.com/firefly-services/

For AWS S3 documentation:
- https://docs.aws.amazon.com/s3/
