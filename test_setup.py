#!/usr/bin/env python3
"""
Test script to verify setup and credentials.
"""

import json
import sys

def test_config():
    """Test config file exists and is valid."""
    try:
        with open('config/config.json', 'r') as f:
            config = json.load(f)
        
        assert 'adobe' in config, "Missing 'adobe' section"
        assert 'aws' in config, "Missing 'aws' section"
        assert config['adobe']['client_id'], "Missing Adobe client_id"
        assert config['adobe']['client_secret'], "Missing Adobe client_secret"
        
        print("✓ Config file is valid")
        return True
    except Exception as e:
        print(f"✗ Config error: {e}")
        return False

def test_aws_credentials():
    """Test AWS credentials are configured."""
    try:
        import boto3
        sts = boto3.client('sts')
        identity = sts.get_caller_identity()
        print(f"✓ AWS credentials configured (Account: {identity['Account']})")
        return True
    except Exception as e:
        print(f"✗ AWS credentials error: {e}")
        print("  Run: aws configure")
        return False

def test_dependencies():
    """Test required packages are installed."""
    try:
        import boto3
        import requests
        print("✓ Dependencies installed")
        return True
    except ImportError as e:
        print(f"✗ Missing dependency: {e}")
        print("  Run: pip install -r requirements.txt")
        return False

def main():
    print("Testing Living Product setup...\n")
    
    tests = [
        test_dependencies(),
        test_config(),
        test_aws_credentials()
    ]
    
    if all(tests):
        print("\n✓ All tests passed! Ready to run pipeline.")
        print("\nExample usage:")
        print('  python pipeline.py --model-url "https://example.com/model.glb" --brief "luxury watch in sunset desert"')
    else:
        print("\n✗ Some tests failed. Please fix the issues above.")
        sys.exit(1)

if __name__ == "__main__":
    main()
