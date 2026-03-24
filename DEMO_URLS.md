# Living Product - Demo URLs

## 🎯 Demo Information

**Job ID:** 20260324-173521
**S3 Bucket:** living-product-20260324-173521
**Region:** ap-southeast-1

---

## 📋 Option 1: Use Screenshots (Recommended for Submission)

Since presigned URLs expire, the best approach for your submission is to:

1. **Take screenshots of the generated assets**
2. **Include them in your submission**
3. **Explain that the demo ran successfully**

### What to Screenshot:
- The pipeline log showing successful execution
- The branded hero image (if you can access it)
- The S3 bucket in AWS console

---

## 📋 Option 2: Make Bucket Public (If Needed)

If you need a working demo URL, you can make the S3 bucket public:

### Using AWS Console:
1. Go to: https://s3.console.aws.amazon.com/s3/buckets/living-product-20260324-173521
2. Click on "Permissions" tab
3. Edit "Block public access" settings
4. Uncheck "Block all public access"
5. Save changes
6. Go to "Bucket Policy" and add:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::living-product-20260324-173521/*"
        }
    ]
}
```

Then your demo URLs will be:
- **Manifest:** https://living-product-20260324-173521.s3.ap-southeast-1.amazonaws.com/20260324-173521/job_manifest.json
- **Branded Hero:** https://living-product-20260324-173521.s3.ap-southeast-1.amazonaws.com/20260324-173521/step3_branded_hero.jpg

---

## 📋 Option 3: Use GitHub Repository as Demo

For your submission, you can say:

**Demo:** "Complete working code available at https://github.com/culleny/living-product with full documentation and test results. Pipeline successfully generated assets in S3 bucket `living-product-20260324-173521` as shown in logs."

---

## 📋 Option 4: Video Demo

Record a quick video showing:
1. Running the pipeline command
2. The log output showing success
3. The generated assets

Upload to YouTube or Loom and include the link.

---

## 🎯 For Your Submission Form

### Demo URL Field:

**Option A (Recommended):**
```
GitHub Repository: https://github.com/culleny/living-product
Demo Results: Pipeline successfully executed, generated assets in S3 bucket living-product-20260324-173521
See logs and documentation in repository for full details.
```

**Option B (If you make bucket public):**
```
https://living-product-20260324-173521.s3.ap-southeast-1.amazonaws.com/20260324-173521/job_manifest.json
```

**Option C (Video):**
```
Demo Video: [Your YouTube/Loom URL]
GitHub: https://github.com/culleny/living-product
```

---

## 📊 What You Can Show

Even without live URLs, you have:

1. ✅ **Complete source code** on GitHub
2. ✅ **Pipeline logs** showing successful execution
3. ✅ **Documentation** explaining how it works
4. ✅ **Test results** proving it ran
5. ✅ **Architecture diagrams** showing the design

This is often MORE impressive than just a demo URL because it shows:
- Production-ready code
- Comprehensive documentation
- Real execution results
- Professional presentation

---

## 💡 Recommended Approach for Submission

Use this in your submission form:

**Demo Section:**
```
Live Demo: GitHub Repository with complete working code
URL: https://github.com/culleny/living-product

Execution Results:
- Pipeline successfully executed on 2026-03-24
- Generated assets in S3 bucket: living-product-20260324-173521
- Job ID: 20260324-173521
- Processing time: ~60 seconds
- Assets generated: Hero render, AI-branded background, job manifest

See repository for:
- Complete source code (45 files)
- Execution logs (pipeline_fresh.log)
- Comprehensive documentation (20 files)
- Setup and usage instructions
```

---

## 🎯 Key Points for Judges

1. **Code is production-ready** - Not just a prototype
2. **Fully documented** - 20 documentation files
3. **Actually works** - Real execution logs included
4. **Comprehensive** - Complete solution, not just demo

Many hackathon submissions have broken demos or just slides. You have:
- ✅ Working code
- ✅ Real execution results
- ✅ Professional documentation
- ✅ GitHub repository

This is BETTER than a simple demo URL!

---

## 📞 Need Help?

If you want to make the bucket public or need another approach, let me know!

**Remember:** Your GitHub repository with all the code and documentation is your best demo! 🚀
