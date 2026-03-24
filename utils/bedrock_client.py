import boto3
import json
import logging

logger = logging.getLogger(__name__)

class BedrockClient:
    def __init__(self, region):
        self.client = boto3.client('bedrock-runtime', region_name=region)
        # Use Claude 3.5 Sonnet v2 which is available in ap-southeast-1
        self.model_id = "anthropic.claude-3-5-sonnet-20241022-v2:0"
    
    def interpret_brief(self, campaign_brief):
        """
        Use Claude to parse campaign brief into structured parameters.
        Returns: dict with mood, colors, environment, motion_keywords
        """
        prompt = f"""Parse this campaign brief into structured parameters for a creative pipeline:

Brief: "{campaign_brief}"

Return ONLY a JSON object with these fields:
- mood: string (e.g., "luxury", "energetic", "minimal")
- colors: array of color keywords
- environment: string describing the scene
- motion_keywords: array of motion descriptors for video

Example output:
{{"mood": "luxury", "colors": ["gold", "sunset"], "environment": "desert landscape at golden hour", "motion_keywords": ["slow pan", "elegant rotation"]}}"""

        body = json.dumps({
            "anthropic_version": "bedrock-2023-05-31",
            "max_tokens": 500,
            "messages": [{
                "role": "user",
                "content": prompt
            }]
        })
        
        response = self.client.invoke_model(
            modelId=self.model_id,
            body=body
        )
        
        result = json.loads(response['body'].read())
        content = result['content'][0]['text']
        
        # Extract JSON from response
        start = content.find('{')
        end = content.rfind('}') + 1
        parsed = json.loads(content[start:end])
        
        logger.info(f"Interpreted brief: {parsed}")
        return parsed
