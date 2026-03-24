#!/bin/bash
# Setup AWS credentials for Living Product pipeline

echo "Living Product - AWS Setup"
echo "=========================="
echo ""
echo "This pipeline needs AWS credentials to:"
echo "  - Create S3 buckets"
echo "  - Store generated assets"
echo "  - Call Bedrock (Claude) for brief interpretation"
echo ""
echo "Please provide your AWS credentials:"
echo ""

# Create .aws directory if it doesn't exist
mkdir -p ~/.aws

# Prompt for credentials
read -p "AWS Access Key ID: " aws_access_key
read -sp "AWS Secret Access Key: " aws_secret_key
echo ""
read -p "Default region [us-west-2]: " aws_region
aws_region=${aws_region:-us-west-2}

# Write credentials file
cat > ~/.aws/credentials << EOF
[default]
aws_access_key_id = $aws_access_key
aws_secret_access_key = $aws_secret_key
EOF

# Write config file
cat > ~/.aws/config << EOF
[default]
region = $aws_region
output = json
EOF

echo ""
echo "✓ AWS credentials configured!"
echo ""
echo "Testing connection..."
python3 -c "import boto3; sts = boto3.client('sts'); identity = sts.get_caller_identity(); print(f'✓ Connected to AWS Account: {identity[\"Account\"]}')" 2>&1

if [ $? -eq 0 ]; then
    echo ""
    echo "✓ Setup complete! You can now run the pipeline:"
    echo "  python3 pipeline.py --image-url <url> --brief \"your campaign brief\""
else
    echo ""
    echo "✗ Connection failed. Please check your credentials and try again."
fi
