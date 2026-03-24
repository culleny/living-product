# Living Product - Architecture Documentation

## System Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────────────┐
│                          LIVING PRODUCT PIPELINE                         │
│                     AI-Powered Creative Production                       │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│                              INPUT LAYER                                 │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                           │
│  ┌──────────────────┐         ┌──────────────────┐                     │
│  │  Product Image   │         │  Campaign Brief  │                     │
│  │  (2D or 3D)      │         │  (Natural Lang)  │                     │
│  │                  │         │                  │                     │
│  │  • JPG/PNG       │         │  "tropical beach │                     │
│  │  • GLB/USDZ      │         │   at sunset..."  │                     │
│  └────────┬─────────┘         └────────┬─────────┘                     │
│           │                            │                                │
│           └────────────┬───────────────┘                                │
│                        │                                                │
└────────────────────────┼────────────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                        ORCHESTRATION LAYER                               │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                           │
│                      ┌─────────────────────┐                            │
│                      │   pipeline.py       │                            │
│                      │   Main Orchestrator │                            │
│                      │                     │                            │
│                      │  • Job Management   │                            │
│                      │  • Step Sequencing  │                            │
│                      │  • Error Handling   │                            │
│                      └──────────┬──────────┘                            │
│                                 │                                        │
└─────────────────────────────────┼────────────────────────────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                         PROCESSING LAYER                                 │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                           │
│  ┌──────────────┐   ┌──────────────┐   ┌──────────────┐               │
│  │   Step 1     │   │   Step 2     │   │   Step 3     │               │
│  │ 3D Composite │──▶│ BG Removal   │──▶│Brand Composite│              │
│  │              │   │              │   │              │               │
│  │ • 3D Render  │   │ • Photoshop  │   │ • Firefly    │               │
│  │ • 2D Upload  │   │ • Cutout     │   │ • AI BG Gen  │               │
│  └──────────────┘   └──────────────┘   └──────┬───────┘               │
│                                                 │                        │
│                                                 ▼                        │
│  ┌──────────────┐   ┌──────────────┐   ┌──────────────┐               │
│  │   Step 6     │   │   Step 5     │   │   Step 4     │               │
│  │  Reframe     │◀──│    Video     │◀──│  Outpaint    │               │
│  │              │   │              │   │              │               │
│  │ • Story 9:16 │   │ • Animation  │   │ • Billboard  │               │
│  │ • Square 1:1 │   │ • 5 seconds  │   │ • 1920x1080  │               │
│  │ • Banner 16:9│   │ • Optional   │   │              │               │
│  └──────────────┘   └──────────────┘   └──────────────┘               │
│                                                                           │
└─────────────────────────────────────────────────────────────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                         INTEGRATION LAYER                                │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                           │
│  ┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐     │
│  │  Adobe Client    │  │   S3 Client      │  │ Bedrock Client   │     │
│  │  (utils/)        │  │   (utils/)       │  │ (utils/)         │     │
│  │                  │  │                  │  │                  │     │
│  │ • OAuth Token    │  │ • Bucket Mgmt    │  │ • Claude AI      │     │
│  │ • Firefly API    │  │ • Upload/Download│  │ • Brief Parse    │     │
│  │ • Photoshop API  │  │ • Presigned URLs │  │ • Optional       │     │
│  │ • Retry Logic    │  │                  │  │                  │     │
│  └────────┬─────────┘  └────────┬─────────┘  └────────┬─────────┘     │
│           │                     │                      │                │
└───────────┼─────────────────────┼──────────────────────┼────────────────┘
            │                     │                      │
            ▼                     ▼                      ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                         EXTERNAL SERVICES                                │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                           │
│  ┌──────────────────────────────────────────────────────────────┐      │
│  │              Adobe Firefly Services                           │      │
│  │  ┌────────────┐  ┌────────────┐  ┌────────────┐             │      │
│  │  │  Firefly   │  │ Photoshop  │  │Substance 3D│             │      │
│  │  │    API     │  │    API     │  │    API     │             │      │
│  │  │            │  │            │  │            │             │      │
│  │  │ • Generate │  │ • Cutout   │  │ • 3D Model │             │      │
│  │  │ • Expand   │  │ • Layers   │  │ • Render   │             │      │
│  │  │ • Video    │  │ • Composite│  │            │             │      │
│  │  └────────────┘  └────────────┘  └────────────┘             │      │
│  └──────────────────────────────────────────────────────────────┘      │
│                                                                           │
│  ┌──────────────────────────────────────────────────────────────┐      │
│  │                    AWS Services                               │      │
│  │  ┌────────────┐  ┌────────────┐  ┌────────────┐             │      │
│  │  │     S3     │  │  Bedrock   │  │    IAM     │             │      │
│  │  │            │  │            │  │            │             │      │
│  │  │ • Storage  │  │ • Claude   │  │ • Auth     │             │      │
│  │  │ • Buckets  │  │ • AI Model │  │ • Creds    │             │      │
│  │  │ • URLs     │  │            │  │            │             │      │
│  │  └────────────┘  └────────────┘  └────────────┘             │      │
│  └──────────────────────────────────────────────────────────────┘      │
│                                                                           │
└─────────────────────────────────────────────────────────────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                          OUTPUT LAYER                                    │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                           │
│  ┌──────────────────────────────────────────────────────────────┐      │
│  │                    S3 Bucket Storage                          │      │
│  │                                                               │      │
│  │  living-product-{timestamp}/                                 │      │
│  │  ├── step1_hero_render.jpg                                   │      │
│  │  ├── step2_cutout.png                                        │      │
│  │  ├── step3_branded_hero.jpg                                  │      │
│  │  ├── step4_billboard.jpg                                     │      │
│  │  ├── step5_video.mp4                                         │      │
│  │  ├── step6_story.jpg                                         │      │
│  │  ├── step6_square.jpg                                        │      │
│  │  ├── step6_banner.jpg                                        │      │
│  │  └── job_manifest.json                                       │      │
│  │                                                               │      │
│  └──────────────────────────────────────────────────────────────┘      │
│                                                                           │
└─────────────────────────────────────────────────────────────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                        PRESENTATION LAYER                                │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                           │
│                      ┌─────────────────────┐                            │
│                      │  Static Gallery     │                            │
│                      │  (frontend/)        │                            │
│                      │                     │                            │
│                      │  • index.html       │                            │
│                      │  • styles.css       │                            │
│                      │  • app.js           │                            │
│                      │                     │                            │
│                      │  Reads manifest     │                            │
│                      │  from S3            │                            │
│                      └─────────────────────┘                            │
│                                                                           │
└─────────────────────────────────────────────────────────────────────────┘
```

## Data Flow

```
1. User Input
   ├─ Product Image URL
   └─ Campaign Brief Text
        ↓
2. Pipeline Initialization
   ├─ Generate Job ID (timestamp)
   ├─ Create S3 Bucket
   └─ Parse Brief with Claude (optional)
        ↓
3. Step 1: Input Processing
   ├─ If 3D: Render with Substance 3D
   ├─ If 2D: Upload to S3
   └─ Output: Hero Render URL
        ↓
4. Step 2: Background Removal
   ├─ Call Photoshop API (cutout)
   ├─ Fallback: Use original if fails
   └─ Output: Cutout PNG URL
        ↓
5. Step 3: Brand Composite
   ├─ Generate AI background (Firefly)
   ├─ Composite with product
   └─ Output: Branded Hero URL
        ↓
6. Step 4: Outpaint (Optional)
   ├─ Expand to 1920x1080
   ├─ Continue on failure
   └─ Output: Billboard URL
        ↓
7. Step 5: Video (Optional)
   ├─ Animate with motion
   ├─ Continue on failure
   └─ Output: Video URL
        ↓
8. Step 6: Reframe
   ├─ Crop to 9:16 (story)
   ├─ Crop to 1:1 (square)
   ├─ Crop to 16:9 (banner)
   └─ Output: 3 Format URLs
        ↓
9. Manifest Generation
   ├─ Collect all asset URLs
   ├─ Write JSON to S3
   └─ Generate presigned URL
        ↓
10. Gallery Display
    ├─ Load manifest from S3
    ├─ Display all assets
    └─ Enable downloads
```

## Component Details

### Pipeline Orchestrator (pipeline.py)
- **Purpose:** Main entry point, coordinates all steps
- **Responsibilities:**
  - Parse command-line arguments
  - Initialize clients (Adobe, S3, Bedrock)
  - Execute steps sequentially
  - Handle errors gracefully
  - Generate final manifest
- **Error Handling:** Continue on optional step failures

### Step Modules (tools/)
Each step is isolated and independently testable:

- **step1_3d_composite.py:** 3D rendering or 2D upload
- **step2_bg_removal.py:** Background removal with Photoshop
- **step3_brand_composite.py:** AI background generation
- **step4_outpaint.py:** Billboard format expansion
- **step5_video.py:** Video animation (optional)
- **step6_reframe.py:** Multi-format crops

### Utility Modules (utils/)

**adobe_client.py:**
- OAuth token management
- Firefly API calls
- Photoshop API calls
- Automatic retry logic

**s3_client.py:**
- Bucket creation
- File upload/download
- Presigned URL generation
- URL-based uploads

**bedrock_client.py:**
- Claude AI integration
- Campaign brief parsing
- Graceful fallback

**retry.py:**
- Exponential backoff
- Configurable attempts
- Error logging

### Frontend (frontend/)

**index.html:**
- Static gallery page
- Reads manifest from S3
- Displays all assets
- Download buttons

**styles.css:**
- Responsive grid layout
- Professional styling
- Mobile-friendly

**app.js:**
- Fetch manifest from URL
- Render asset cards
- Handle errors

## Technology Stack

### Backend
- **Language:** Python 3.9+
- **Framework:** None (standalone script)
- **Dependencies:**
  - boto3 (AWS SDK)
  - requests (HTTP client)
  - Pillow (image processing)

### Frontend
- **HTML5:** Semantic markup
- **CSS3:** Modern styling
- **JavaScript (ES6):** Async/await, fetch API

### Cloud Services
- **AWS S3:** Object storage
- **AWS Bedrock:** AI model access
- **AWS IAM:** Authentication

### Adobe Services
- **Firefly API:** AI image generation
- **Photoshop API:** Image editing
- **Substance 3D API:** 3D rendering

## Security

### Authentication
- **AWS:** IAM credentials (access key, secret key, session token)
- **Adobe:** OAuth 2.0 (client credentials flow)

### Data Storage
- **S3 Buckets:** Private by default
- **Presigned URLs:** Time-limited access (24 hours)
- **No PII:** Only product images and generated assets

### API Security
- **HTTPS:** All API calls encrypted
- **Token Refresh:** Automatic OAuth token renewal
- **Rate Limiting:** Handled by retry logic

## Scalability

### Current Capacity
- **Throughput:** 1 product per 60 seconds
- **Concurrent Jobs:** 1 (sequential processing)
- **Storage:** Unlimited (S3)

### Future Enhancements
- **Parallel Processing:** Multiple products simultaneously
- **Queue System:** SQS for job management
- **Lambda Functions:** Serverless step execution
- **CDN:** CloudFront for asset delivery
- **Database:** DynamoDB for job tracking

## Error Handling Strategy

### Graceful Degradation
1. **Video Generation:** Optional, continues on failure
2. **Photoshop API:** Falls back to Firefly outputs
3. **Bedrock:** Falls back to simple brief parsing
4. **Expand API:** Continues without billboard format

### Retry Logic
- **Attempts:** 1 retry per API call
- **Backoff:** Exponential (1s, 2s, 4s)
- **Timeout:** 30 seconds per request

### Logging
- **Level:** INFO for progress, ERROR for failures
- **Format:** Timestamp, module, level, message
- **Output:** Console (can redirect to file)

## Performance Metrics

### Measured Performance (Test Run)
- **Total Time:** ~60 seconds
- **S3 Bucket Creation:** 4 seconds
- **Image Upload:** 6 seconds
- **Firefly Generation:** 11 seconds
- **Asset Storage:** 19 seconds
- **Manifest Creation:** <1 second

### Bottlenecks
1. **API Latency:** Firefly generation (10-15s)
2. **Network Transfer:** Large image uploads (5-10s)
3. **Sequential Processing:** No parallelization

### Optimization Opportunities
- Parallel API calls where possible
- Image compression before upload
- CDN caching for repeated assets
- Batch processing for multiple products

## Deployment

### Local Development
```bash
pip3 install -r requirements.txt
python3 pipeline.py --image-url <url> --brief "text"
```

### Production Deployment
1. **AWS Lambda:** Serverless execution
2. **Docker Container:** Consistent environment
3. **EC2 Instance:** Long-running service
4. **ECS/Fargate:** Container orchestration

### CI/CD Pipeline
1. **GitHub Actions:** Automated testing
2. **AWS CodePipeline:** Deployment automation
3. **CloudFormation:** Infrastructure as code

## Monitoring

### Metrics to Track
- **Success Rate:** % of jobs completed
- **Processing Time:** Average duration per job
- **API Errors:** Failed API calls by endpoint
- **Storage Usage:** S3 bucket size growth

### Alerting
- **CloudWatch Alarms:** High error rates
- **SNS Notifications:** Job failures
- **Email Reports:** Daily summaries

## Cost Analysis

### Per-Job Cost (Estimated)
- **S3 Storage:** $0.023/GB/month (~$0.001 per job)
- **S3 Requests:** $0.0004 per 1000 requests (~$0.0001 per job)
- **Firefly API:** Variable (based on Adobe pricing)
- **Bedrock:** $0.003 per 1000 tokens (~$0.001 per brief)

**Total:** ~$0.01-0.05 per product (excluding Firefly)

### Cost Savings vs Manual
- **Designer Time:** $50-100/hour
- **Manual Time:** 2-4 hours per product
- **Manual Cost:** $100-400 per product
- **Automation Savings:** 99% cost reduction

## Compliance

### Data Privacy
- **No PII:** Only product images processed
- **Data Retention:** User-controlled (S3 lifecycle)
- **GDPR:** Not applicable (no personal data)

### Adobe Terms
- **API Usage:** Compliant with Adobe ToS
- **Content Rights:** User owns generated assets
- **Attribution:** Not required for Firefly outputs

### AWS Terms
- **Service Limits:** Within free tier for testing
- **Data Residency:** ap-southeast-1 (Singapore)
- **Compliance:** SOC 2, ISO 27001 certified
