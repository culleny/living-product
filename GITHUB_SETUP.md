# GitHub Repository Setup Guide

## Repository Information

**Repository Name:** `living-product`
**Description:** AI-powered creative production pipeline that transforms product images into complete marketing campaigns using Adobe Firefly Services
**Topics:** `adobe-firefly`, `ai`, `creative-automation`, `aws`, `python`, `hackathon`, `marketing`, `image-generation`

---

## Step 1: Create Repository

### On GitHub.com

1. Go to https://github.com/new
2. Fill in repository details:
   - **Name:** `living-product`
   - **Description:** AI-powered creative production pipeline using Adobe Firefly Services and AWS
   - **Visibility:** Public (for hackathon submission)
   - **Initialize:** Do NOT add README, .gitignore, or license (we have them)

3. Click "Create repository"

---

## Step 2: Prepare Local Repository

### Create .gitignore

Your project already has a `.gitignore`. Verify it includes:

```gitignore
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
ENV/
build/
dist/
*.egg-info/

# AWS
.aws/
*.pem

# Config
config/config.json
*.log

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Temporary
*.tmp
temp/
```

### Create README Badge Section

Add badges to the top of your README.md:

```markdown
# Living Product Pipeline

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Adobe Firefly](https://img.shields.io/badge/Adobe-Firefly-FF0000.svg)](https://www.adobe.com/products/firefly.html)
[![AWS](https://img.shields.io/badge/AWS-S3%20%7C%20Bedrock-FF9900.svg)](https://aws.amazon.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Hackathon](https://img.shields.io/badge/Adobe%20Hackathon-Q1%202026-red.svg)](https://adobe.com)

AI-powered creative production pipeline that transforms a 3D product model into a complete marketing campaign pack in one run.

[Rest of your README content...]
```

---

## Step 3: Initialize Git

```bash
# Navigate to project directory
cd ~/living-product

# Initialize git (if not already done)
git init

# Add all files
git add .

# Create initial commit
git commit -m "Initial commit: Living Product pipeline

- Complete pipeline with 6 processing steps
- Adobe Firefly Services integration
- AWS S3 and Bedrock integration
- Static frontend gallery
- Comprehensive documentation
- Test scripts and examples"

# Add remote (replace with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/living-product.git

# Push to GitHub
git branch -M main
git push -u origin main
```

---

## Step 4: Create GitHub Releases

### Tag the Hackathon Submission

```bash
# Create a tag for the hackathon submission
git tag -a v1.0.0-hackathon -m "Adobe Hackathon Q1 2026 Submission

Living Product - AI-powered creative production pipeline

Features:
- 6-step automated pipeline
- Adobe Firefly image generation
- AWS S3 storage
- Static gallery frontend
- Comprehensive error handling
- Production-ready code

Demo: [Add your gallery URL here]
"

# Push the tag
git push origin v1.0.0-hackathon
```

### Create Release on GitHub

1. Go to your repository on GitHub
2. Click "Releases" → "Create a new release"
3. Select tag: `v1.0.0-hackathon`
4. Release title: "Living Product - Adobe Hackathon Q1 2026 Submission"
5. Description:

```markdown
## Living Product - Hackathon Submission

AI-powered creative production pipeline that transforms product images into complete marketing campaigns.

### 🎯 What It Does

Input: Product image + campaign brief
Output: 8 marketing-ready assets in 60 seconds

### ✨ Key Features

- **AI-Powered:** Adobe Firefly for intelligent background generation
- **Automated:** One command generates all assets
- **Scalable:** Cloud-based infrastructure
- **Production-Ready:** Comprehensive error handling

### 📦 Deliverables

- ✅ Complete source code
- ✅ Documentation (README, SETUP, QUICKSTART, EXAMPLES)
- ✅ Presentation materials (SUBMISSION, PRESENTATION_SCRIPT)
- ✅ Architecture diagrams
- ✅ Demo scripts
- ✅ Test suite

### 🚀 Quick Start

```bash
pip3 install -r requirements.txt
python3 pipeline.py --image-url <url> --brief "your campaign"
```

### 📊 Demo Results

**Job ID:** 20260324-152042
**Processing Time:** ~60 seconds
**Assets Generated:** 8 formats
**S3 Bucket:** living-product-20260324-152042

### 🏆 Innovation Highlights

- First to combine Firefly + Photoshop + AWS in one pipeline
- Natural language campaign briefs
- Graceful degradation for reliability
- 120x faster than manual work

### 📚 Documentation

- [README.md](README.md) - Overview and usage
- [QUICKSTART.md](QUICKSTART.md) - Get started in 5 minutes
- [SETUP.md](SETUP.md) - Detailed setup instructions
- [EXAMPLES.md](EXAMPLES.md) - Usage examples
- [SUBMISSION.md](SUBMISSION.md) - Full hackathon submission
- [ARCHITECTURE.md](ARCHITECTURE.md) - Technical architecture
- [DEMO_SCRIPT.md](DEMO_SCRIPT.md) - Presentation guide

### 🎥 Demo

[Add your gallery URL or demo video here]

### 👥 Team

Dentsu International - Adobe Hackathon Q1 2026

### 📄 License

MIT License - See LICENSE file for details
```

6. Attach files (optional):
   - Screenshots of generated assets
   - Demo video
   - Architecture diagram image

7. Click "Publish release"

---

## Step 5: Add LICENSE

Create a LICENSE file:

```bash
cat > LICENSE << 'EOF'
MIT License

Copyright (c) 2026 Dentsu International

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
EOF

git add LICENSE
git commit -m "Add MIT License"
git push
```

---

## Step 6: Configure Repository Settings

### On GitHub Repository Settings

1. **About Section** (top right):
   - Description: "AI-powered creative production pipeline using Adobe Firefly Services and AWS"
   - Website: [Your demo URL or documentation site]
   - Topics: `adobe-firefly`, `ai`, `creative-automation`, `aws`, `python`, `hackathon`

2. **Features:**
   - ✅ Issues
   - ✅ Projects (optional)
   - ✅ Wiki (optional for extended docs)
   - ✅ Discussions (optional for community)

3. **Social Preview:**
   - Upload a preview image (screenshot of gallery or architecture diagram)

---

## Step 7: Create GitHub Pages (Optional)

Host the gallery on GitHub Pages:

```bash
# Create gh-pages branch
git checkout -b gh-pages

# Copy frontend files to root
cp frontend/* .

# Commit and push
git add .
git commit -m "Setup GitHub Pages for gallery"
git push origin gh-pages

# Switch back to main
git checkout main
```

Then enable GitHub Pages in repository settings:
- Settings → Pages
- Source: Deploy from branch
- Branch: gh-pages, / (root)
- Save

Your gallery will be available at: `https://YOUR_USERNAME.github.io/living-product/`

---

## Step 8: Add Repository Metadata

### Create CITATION.cff

```yaml
cff-version: 1.2.0
title: Living Product
message: "If you use this software, please cite it as below."
type: software
authors:
  - name: Dentsu International
    website: https://www.dentsu.com
repository-code: "https://github.com/YOUR_USERNAME/living-product"
url: "https://github.com/YOUR_USERNAME/living-product"
abstract: "AI-powered creative production pipeline that transforms product images into complete marketing campaigns using Adobe Firefly Services and AWS."
keywords:
  - adobe-firefly
  - ai
  - creative-automation
  - aws
  - python
  - marketing
  - image-generation
license: MIT
version: 1.0.0
date-released: 2026-03-24
```

### Create CONTRIBUTING.md

```markdown
# Contributing to Living Product

Thank you for your interest in contributing!

## Development Setup

1. Fork the repository
2. Clone your fork: `git clone https://github.com/YOUR_USERNAME/living-product.git`
3. Install dependencies: `pip3 install -r requirements.txt`
4. Configure AWS and Adobe credentials
5. Run tests: `python3 test_setup.py`

## Making Changes

1. Create a feature branch: `git checkout -b feature/your-feature`
2. Make your changes
3. Test thoroughly
4. Commit with clear messages
5. Push to your fork
6. Open a Pull Request

## Code Style

- Follow PEP 8 for Python code
- Add docstrings to all functions
- Include type hints where appropriate
- Write clear commit messages

## Testing

- Test all changes locally before submitting
- Ensure existing tests pass
- Add new tests for new features

## Questions?

Open an issue or discussion on GitHub.
```

---

## Step 9: Create Project Documentation Site (Optional)

### Using GitHub Wiki

1. Go to your repository → Wiki
2. Create pages:
   - Home (overview)
   - Installation
   - Usage Guide
   - API Reference
   - Troubleshooting
   - FAQ

### Using MkDocs (Advanced)

```bash
# Install MkDocs
pip3 install mkdocs mkdocs-material

# Create docs structure
mkdocs new .

# Edit mkdocs.yml
cat > mkdocs.yml << 'EOF'
site_name: Living Product Documentation
site_description: AI-powered creative production pipeline
site_author: Dentsu International
repo_url: https://github.com/YOUR_USERNAME/living-product

theme:
  name: material
  palette:
    primary: red
    accent: orange

nav:
  - Home: index.md
  - Quick Start: quickstart.md
  - Setup: setup.md
  - Examples: examples.md
  - Architecture: architecture.md
  - API Reference: api.md
  - Troubleshooting: troubleshooting.md

markdown_extensions:
  - codehilite
  - admonition
  - toc:
      permalink: true
EOF

# Build and deploy
mkdocs gh-deploy
```

---

## Step 10: Add Continuous Integration (Optional)

### Create .github/workflows/test.yml

```yaml
name: Test Pipeline

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.9'
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    
    - name: Lint with flake8
      run: |
        pip install flake8
        flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
    
    - name: Test imports
      run: |
        python -c "import pipeline"
        python -c "from utils import adobe_client, s3_client, bedrock_client"
```

---

## Step 11: Prepare for Submission

### Create Submission Package

```bash
# Create a clean export
git archive --format=zip --output=living-product-submission.zip HEAD

# Or create a tarball
git archive --format=tar.gz --output=living-product-submission.tar.gz HEAD
```

### Submission Checklist

- [ ] Repository is public
- [ ] README is comprehensive
- [ ] All documentation files included
- [ ] LICENSE file added
- [ ] .gitignore properly configured
- [ ] No sensitive credentials in code
- [ ] Release tagged and published
- [ ] Demo URLs are working
- [ ] Screenshots/videos included
- [ ] Repository URL ready to share

---

## Step 12: Share Your Work

### Repository URL Format

```
https://github.com/YOUR_USERNAME/living-product
```

### Share On

- **Hackathon Submission Form:** Include repository URL
- **Social Media:** Tweet about your project
- **LinkedIn:** Share your achievement
- **Dev.to / Medium:** Write a blog post
- **Hacker News:** Share for feedback

### Social Media Template

```
🚀 Just built "Living Product" for the Adobe Hackathon!

AI-powered pipeline that transforms product images into 8 marketing assets in 60 seconds using Adobe Firefly Services.

✨ Features:
- Automated AI generation
- 120x faster than manual work
- Production-ready code

Check it out: https://github.com/YOUR_USERNAME/living-product

#AdobeFirefly #AI #Hackathon #CreativeAutomation
```

---

## Maintenance

### Keep Repository Updated

```bash
# Regular updates
git add .
git commit -m "Update: [description]"
git push

# Create new releases for major updates
git tag -a v1.1.0 -m "Version 1.1.0: [features]"
git push origin v1.1.0
```

### Monitor Issues

- Respond to issues promptly
- Label issues appropriately
- Close resolved issues
- Thank contributors

### Update Documentation

- Keep README current
- Update examples as needed
- Add new features to docs
- Fix typos and errors

---

## Troubleshooting

### Push Rejected

```bash
# Pull latest changes first
git pull origin main --rebase
git push
```

### Large Files

```bash
# Remove large files from history
git filter-branch --tree-filter 'rm -f large_file.bin' HEAD
git push --force
```

### Sensitive Data Committed

```bash
# Remove from history
git filter-branch --force --index-filter \
  "git rm --cached --ignore-unmatch config/config.json" \
  --prune-empty --tag-name-filter cat -- --all

# Force push
git push --force --all
```

---

## Resources

- [GitHub Docs](https://docs.github.com)
- [Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf)
- [Markdown Guide](https://www.markdownguide.org)
- [Semantic Versioning](https://semver.org)
- [Keep a Changelog](https://keepachangelog.com)

---

## Final Notes

- Keep your repository clean and organized
- Write clear commit messages
- Document everything
- Respond to community feedback
- Have fun and be proud of your work!

**Good luck with your submission! 🎉**
