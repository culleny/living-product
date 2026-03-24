#!/usr/bin/env python3
"""
Helper script to open the gallery with the latest job manifest.
Usage: python view_gallery.py <manifest_url>
"""

import sys
import webbrowser
import os
from urllib.parse import quote

def main():
    if len(sys.argv) < 2:
        print("Usage: python view_gallery.py <manifest_url>")
        sys.exit(1)
    
    manifest_url = sys.argv[1]
    gallery_path = os.path.abspath('frontend/index.html')
    
    # Open browser with manifest URL
    url = f"file://{gallery_path}?manifest={quote(manifest_url)}"
    print(f"Opening gallery: {url}")
    webbrowser.open(url)

if __name__ == "__main__":
    main()
