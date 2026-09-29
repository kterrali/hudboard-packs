#!/usr/bin/env python3
"""Generate the 3 demo panels for the template pack."""
from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATHS = [
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
]

def font(size):
    for p in FONT_PATHS:
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()

OUT = os.path.dirname(os.path.abspath(__file__)) + "/.."

# ────────────────────────────────────────────────────────
# Panel 1: welcome-lobby.png (3×1 = 384×128)
# ────────────────────────────────────────────────────────
def welcome_lobby():
    W, H = 384, 128
    img = Image.new("RGB", (W, H), (24, 28, 36))
    d = ImageDraw.Draw(img)
    # Subtle gradient
    for y in range(H):
        c = 24 + (y / H) * 8
        d.line([(0, y), (W, y)], fill=(int(c), int(c+4), int(c+12)))
    # Border
    d.rectangle([0, 0, W-1, H-1], outline=(80, 100, 130), width=2)
    # Inner panel
    d.rectangle([6, 6, W-7, H-7], outline=(50, 60, 80), width=1)
    # Text
    d.text((20, 22), "WELCOME", font=font(28), fill=(255, 215, 0))
    d.text((20, 60), "to the server", font=font(18), fill=(220, 220, 230))
    d.text((20, 92), "%player_name%", font=font(14), fill=(120, 180, 255))
    # Right-side decoration
    for x in range(W-60, W-20, 4):
        d.rectangle([x, 30, x+2, H-30], fill=(80, 100, 130))
    img.save(os.path.join(OUT, "panels/png/welcome-lobby.png"))

# ────────────────────────────────────────────────────────
# Panel 2: server-status.png (2×2 = 256×256)
# ────────────────────────────────────────────────────────
def server_status():
    W, H = 256, 256
    img = Image.new("RGB", (W, H), (20, 24, 32))
    d = ImageDraw.Draw(img)
    # Tile separator
    for i in range(1, 2):
        d.line([(i*128, 0), (i*128, H)], fill=(60, 60, 80), width=1)
        d.line([(0, i*128), (W, i*128)], fill=(60, 60, 80), width=1)
    # Border
    d.rectangle([0, 0, W-1, H-1], outline=(80, 100, 130), width=2)
    # Tile (0,0): title
    d.text((16, 30), "SERVER", font=font(20), fill=(255, 215, 0))
    d.text((16, 60), "STATUS", font=font(20), fill=(255, 215, 0))
    # Tile (1,0): TPS
    d.text((144, 28), "TPS", font=font(12), fill=(150, 150, 160))
    d.text((144, 50), "20.0", font=font(22), fill=(100, 255, 100))
    # Tile (0,1): Players
    d.text((16, 144), "Players", font=font(12), fill=(150, 150, 160))
    d.text((16, 165), "%server_online%", font=font(18), fill=(255, 255, 255))
    # Tile (1,1): Balance
    d.text((144, 144), "Balance", font=font(12), fill=(150, 150, 160))
    d.text((144, 168), "$1,250", font=font(16), fill=(100, 255, 100))
    img.save(os.path.join(OUT, "panels/png/server-status.png"))

# ────────────────────────────────────────────────────────
# Panel 3: loading.gif (1×1 = 128×128, animated)
# ────────────────────────────────────────────────────────
def loading_gif():
    W, H = 128, 128
    frames = []
    n_frames = 8
    for i in range(n_frames):
        img = Image.new("RGB", (W, H), (20, 24, 32))
        d = ImageDraw.Draw(img)
        d.rectangle([0, 0, W-1, H-1], outline=(80, 100, 130), width=2)
        # Rotating arc
        import math
        angle = (i / n_frames) * 360
        cx, cy = W//2, H//2
        for r in range(15, 35, 2):
            a = math.radians(angle - r * 4)
            x1 = int(cx + r * math.cos(a))
            y1 = int(cy + r * math.sin(a))
            d.ellipse([x1-3, y1-3, x1+3, y1+3], fill=(120, 180, 255))
        d.text((32, 100), "Loading...", font=font(10), fill=(180, 180, 200))
        frames.append(img)
    frames[0].save(
        os.path.join(OUT, "panels/gif/loading.gif"),
        save_all=True, append_images=frames[1:],
        duration=100, loop=0, optimize=True,
    )

if __name__ == "__main__":
    os.makedirs(os.path.join(OUT, "panels/png"), exist_ok=True)
    os.makedirs(os.path.join(OUT, "panels/gif"), exist_ok=True)
    welcome_lobby()
    server_status()
    loading_gif()
    print("Generated demo panels in", os.path.join(OUT, "panels"))
    for root, dirs, files in os.walk(os.path.join(OUT, "panels")):
        for f in files:
            p = os.path.join(root, f)
            print(f"  {p.replace(OUT + '/', '')}  ({os.path.getsize(p)//1024} KB)")
