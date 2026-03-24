# Living Product - Example Usage

## Example 1: Beverage Campaign (2D Image)

```bash
python pipeline.py \
  --image-url "https://images.unsplash.com/photo-1629203851122-3726ecdf080e" \
  --brief "refreshing cola on tropical beach at sunset, vibrant colors, summer vibes"
```

This will:
1. Use the 2D product image as starting point
2. Remove background to isolate the product
3. Generate a tropical beach background based on the brief
4. Composite product onto new background
5. Extend to billboard format
6. Generate animated video
7. Create story, square, and banner crops

## Example 2: Luxury Watch (3D Model)

```bash
python pipeline.py \
  --model-url "https://example.com/watch.glb" \
  --brief "luxury timepiece in minimalist desert landscape, golden hour lighting, premium feel"
```

## Example 3: Tech Product (2D Image)

```bash
python pipeline.py \
  --image-url "https://images.unsplash.com/photo-1505740420928-5e560c06d30e" \
  --brief "premium headphones in modern studio environment, sleek and professional"
```

## Adobe Stock Images

If you want to use Adobe Stock images:
1. Download the image from Adobe Stock
2. Upload to a public URL (S3, Imgur, etc.)
3. Use that URL with `--image-url`

Or use the Adobe Stock API to get direct image URLs (requires additional setup).

## Tips for Better Results

**Campaign Brief Best Practices:**
- Be specific about mood and environment
- Include color palette keywords
- Mention lighting conditions
- Add style descriptors (luxury, minimal, energetic, etc.)

**Good briefs:**
- "luxury product in sunset desert, warm golden tones, cinematic lighting"
- "tech gadget in futuristic cityscape, neon blues and purples, cyberpunk aesthetic"
- "organic product in natural forest setting, earthy greens, soft morning light"

**Avoid:**
- Vague briefs like "make it look good"
- Conflicting styles like "minimal but busy"
