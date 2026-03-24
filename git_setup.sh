#!/bin/bash

# Git Setup Script for Living Product
# Run this before committing

echo "==================================="
echo "Git Configuration Setup"
echo "==================================="
echo ""

# Prompt for user information
read -p "Enter your name: " git_name
read -p "Enter your email: " git_email

# Configure git
git config user.name "$git_name"
git config user.email "$git_email"

echo ""
echo "Git configured successfully!"
echo "Name: $git_name"
echo "Email: $git_email"
echo ""

# Create initial commit
echo "Creating initial commit..."
git commit -m "Initial commit: Living Product pipeline

- Complete pipeline with 6 processing steps
- Adobe Firefly Services integration
- AWS S3 and Bedrock integration
- Static frontend gallery
- Comprehensive documentation (13 files)
- Test scripts and examples
- Production-ready code with error handling"

echo ""
echo "==================================="
echo "Next Steps:"
echo "==================================="
echo ""
echo "1. Create GitHub repository:"
echo "   Go to: https://github.com/new"
echo "   Name: living-product"
echo "   Description: AI-powered creative production pipeline using Adobe Firefly Services and AWS"
echo "   Visibility: Public"
echo "   Do NOT initialize with README"
echo ""
echo "2. Add remote and push:"
echo "   git remote add origin https://github.com/YOUR_USERNAME/living-product.git"
echo "   git branch -M main"
echo "   git push -u origin main"
echo ""
echo "3. Create release tag:"
echo "   git tag -a v1.0.0-hackathon -m 'Adobe Hackathon Q1 2026 Submission'"
echo "   git push origin v1.0.0-hackathon"
echo ""
echo "Done! Your repository is ready for GitHub."
echo ""
