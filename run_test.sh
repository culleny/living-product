#!/bin/bash
# Test run of Living Product pipeline with sample image

# Check if AWS credentials are set
if [ -z "$AWS_ACCESS_KEY_ID" ]; then
    echo "ERROR: AWS credentials not set!"
    echo ""
    echo "Please set your AWS credentials first:"
    echo '  export AWS_DEFAULT_REGION="ap-southeast-1"'
    echo '  export AWS_ACCESS_KEY_ID="your-key"'
    echo '  export AWS_SECRET_ACCESS_KEY="your-secret"'
    echo '  export AWS_SESSION_TOKEN="your-token"'
    echo ""
    exit 1
fi

echo "Living Product Pipeline - Test Run"
echo "==================================="
echo ""
echo "Testing with sample beverage image..."
echo ""

python3 pipeline.py \
  --image-url "https://images.unsplash.com/photo-1629203851122-3726ecdf080e" \
  --brief "refreshing cola on tropical beach at sunset, vibrant colors, summer vibes"
