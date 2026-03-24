#!/usr/bin/env python3
"""
Quick test of the Living Product pipeline

IMPORTANT: Set your AWS credentials before running:
export AWS_DEFAULT_REGION="ap-southeast-1"
export AWS_ACCESS_KEY_ID="your-key"
export AWS_SECRET_ACCESS_KEY="your-secret"
export AWS_SESSION_TOKEN="your-token"
"""
import os
import sys

# Check if AWS credentials are set
if not os.environ.get('AWS_ACCESS_KEY_ID'):
    print("ERROR: AWS credentials not set!")
    print("Please set your AWS credentials:")
    print('  export AWS_DEFAULT_REGION="ap-southeast-1"')
    print('  export AWS_ACCESS_KEY_ID="your-key"')
    print('  export AWS_SECRET_ACCESS_KEY="your-secret"')
    print('  export AWS_SESSION_TOKEN="your-token"')
    sys.exit(1)

print("Living Product Pipeline - Test Run (Retry with New Credentials)")
print("=" * 70)
print()
print("Using sample image from Unsplash...")
print("Brief: 'refreshing cola on tropical beach at sunset'")
print()

# Run pipeline
sys.argv = [
    'pipeline.py',
    '--image-url', 'https://images.unsplash.com/photo-1629203851122-3726ecdf080e',
    '--brief', 'refreshing cola on tropical beach at sunset, vibrant colors, summer vibes'
]

# Import and run
from pipeline import main
main()
