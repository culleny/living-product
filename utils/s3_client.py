import boto3
import logging
from datetime import datetime
from botocore.exceptions import ClientError

logger = logging.getLogger(__name__)

class S3Client:
    def __init__(self, region):
        self.s3 = boto3.client('s3', region_name=region)
        self.region = region
        self.bucket_name = None
    
    def create_bucket(self, prefix):
        """Create S3 bucket with timestamp suffix."""
        timestamp = datetime.now().strftime('%Y%m%d-%H%M%S')
        bucket_name = f"{prefix}-{timestamp}"
        
        try:
            if self.region == 'us-east-1':
                self.s3.create_bucket(Bucket=bucket_name)
            else:
                self.s3.create_bucket(
                    Bucket=bucket_name,
                    CreateBucketConfiguration={'LocationConstraint': self.region}
                )
            
            # Enable CORS for frontend access
            cors_config = {
                'CORSRules': [{
                    'AllowedHeaders': ['*'],
                    'AllowedMethods': ['GET', 'HEAD'],
                    'AllowedOrigins': ['*'],
                    'MaxAgeSeconds': 3000
                }]
            }
            self.s3.put_bucket_cors(Bucket=bucket_name, CORSConfiguration=cors_config)
            
            self.bucket_name = bucket_name
            logger.info(f"Created S3 bucket: {bucket_name}")
            return bucket_name
        except ClientError as e:
            logger.error(f"Failed to create bucket: {e}")
            raise
    
    def upload_file(self, file_path, key):
        """Upload file to S3 and return presigned URL."""
        try:
            self.s3.upload_file(file_path, self.bucket_name, key)
            url = self.s3.generate_presigned_url(
                'get_object',
                Params={'Bucket': self.bucket_name, 'Key': key},
                ExpiresIn=86400  # 24 hours
            )
            logger.info(f"Uploaded {key} to S3")
            return url
        except ClientError as e:
            logger.error(f"Failed to upload {key}: {e}")
            raise
    
    def upload_from_url(self, url, key):
        """Download from URL and upload to S3."""
        import requests
        response = requests.get(url, stream=True)
        response.raise_for_status()
        
        self.s3.put_object(
            Bucket=self.bucket_name,
            Key=key,
            Body=response.content
        )
        
        presigned_url = self.s3.generate_presigned_url(
            'get_object',
            Params={'Bucket': self.bucket_name, 'Key': key},
            ExpiresIn=86400
        )
        logger.info(f"Uploaded {key} from URL to S3")
        return presigned_url
