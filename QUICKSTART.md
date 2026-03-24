# Living Product - Quick Start

## 1. Setup (One-time)

```bash
# Install dependencies
pip3 install -r requirements.txt

# Configure AWS credentials
bash setup_aws.sh
```

## 2. Run Pipeline

```bash
python3 pipeline.py \
  --image-url "https://images.unsplash.com/photo-1629203851122-3726ecdf080e" \
  --brief "refreshing beverage on tropical beach at sunset, vibrant colors"
```

## 3. View Results

The pipeline will output a manifest URL. Open the gallery:

```bash
python3 view_gallery.py <MANIFEST_URL>
```

## What You'll Get

8 marketing assets in one run:
1. **Hero Render** - Product in photorealistic scene
2. **Product Cutout** - Clean PNG with background removed
3. **Branded Hero** - Product on generated background
4. **Billboard** - 1920x1080 extended format
5. **Video** - 5-second animated version
6. **Story** - 9:16 vertical format
7. **Square** - 1:1 format
8. **Banner** - 16:9 format

## Example Briefs

**Beverage:**
```bash
--brief "refreshing cola on sandy beach, summer vibes, ocean waves, vibrant colors"
```

**Tech Product:**
```bash
--brief "premium headphones in modern studio, sleek and professional, minimalist"
```

**Luxury Product:**
```bash
--brief "luxury watch in desert landscape, golden hour lighting, warm tones, cinematic"
```

## Troubleshooting

**No AWS credentials:**
Run `bash setup_aws.sh` and enter your AWS access keys.

**Adobe API errors:**
Check `config/config.json` has correct client_id and client_secret.

**Need help?**
See `SETUP.md` for detailed instructions.
