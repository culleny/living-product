#!/bin/bash

# Push to GitHub Script
# Run this after creating your GitHub repository

echo "=================================="
echo "Pushing to GitHub"
echo "=================================="
echo ""

# Add remote
echo "Adding remote..."
git remote add origin https://github.com/Culleny/living-product.git

# Push to main branch
echo "Pushing to main branch..."
git branch -M main
git push -u origin main

# Create and push release tag
echo "Creating release tag..."
git tag -a v1.0.0-hackathon -m "Adobe Hackathon Q1 2026 Submission

Living Product - AI-powered creative production pipeline

Features:
- 6-step automated pipeline
- Adobe Firefly image generation
- AWS S3 storage
- Static gallery frontend
- Comprehensive error handling
- Production-ready code

Demo: Generate fresh URL with: python3 test_pipeline.py
"

echo "Pushing tag..."
git push origin v1.0.0-hackathon

echo ""
echo "=================================="
echo "✅ Success!"
echo "=================================="
echo ""
echo "Your repository is now live at:"
echo "https://github.com/Culleny/living-product"
echo ""
echo "Next steps:"
echo "1. Visit your repository to verify"
echo "2. Generate fresh demo URL: python3 test_pipeline.py"
echo "3. Create PowerPoint slide: Open POWERPOINT_SLIDE.txt"
echo "4. Fill submission form: Use content from SUBMISSION.md"
echo ""
