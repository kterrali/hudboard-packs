# 🟧 HudBoard — Content Packs
 packs for **[HudBoard](https://github.com/Kterrali/hudboard)** — PNG/GIF info panels for Paper 1.21.11+ Minecraft servers.

Each pack is a themed bundle of panels ready to drop into `plugins/HudBoard/panels/`. No plugin update needed.

---

## 📦 Available packs

| Pack | Theme | Panels | Released |
|------|-------|--------|----------|
| [`template`](packs/template/) | Sample template (3 panels) | 3 | v1.0.0 |

More packs coming .

---

## 🚀 Install a pack

### Option A — Download the ZIP

1. Go to [Releases](https://github.com/Kterrali/hudboard-packs/releases)
2. Download the pack ZIP you want (e.g. `halloween-2026.zip`)
3. Extract into your server's `plugins/HudBoard/panels/` directory
4. `/hudboard reload`
5. `/hudboard panel place <panel-name>`

### Option B — Manual install (single files)

Browse [`packs/`](packs/), download individual PNG + sidecar yml, drop into `plugins/HudBoard/panels/png/`.

---

## 📁 Pack format

Every pack is a folder with this structure:

```
<pack-name>/
├── manifest.json          # pack metadata
├── README.md              # what the pack contains
└── panels/
    ├── png/               # static panels
    │   ├── panel-name.png
    │   ├── panel-name.yml  # sidecar with data-points
    │   └── ...
    └── gif/               # animated panels (optional)
        ├── anim-panel.gif
        ├── anim-panel.yml
        └── ...
```

### `manifest.json` schema

```json
{
  "name": "Halloween 2026",
  "slug": "halloween-2026",
  "version": "1.0.0",
  "hudboard_version": ">=2.7.0",
  "description": "Spooky panels with pumpkins, ghosts, and fog",
  "panels": 12,
  "tags": ["halloween", "spooky", "lobby"],
  "author": "Kterrali",
  "license": "Apache-2.0",
  "min_paper_version": "1.21.11"
}
```

---

## 🛠 Create your own pack

Want to contribute or make your own? Here's how:

### 1. Create the folder

```bash
mkdir packs/<your-pack-slug>
cd packs/<your-pack-slug>
mkdir panels/png panels/gif
```

### 2. Write `manifest.json`

See the schema above. Pick a slug like `christmas-2026` or `cyberpunk-2099`.

### 3. Create panels

**Static PNG** (recommended for info panels):
- Use **Aseprite**, **Photoshop**, **GIMP**, or any image editor
- Recommended dimensions: **384×128** (3×1 tiles, fits standard server lobbies)
- Each tile is **128×128**, so 3×1 = 3 tiles wide, 1 tile tall
- Use clean borders and readable fonts

**Animated GIF**:
- Same tool, animate at 8-15 FPS
- Keep file size under **500 KB** per GIF (will be sent over the network to all viewers)
- Use looping animations (bobbing, pulsing, scrolling)

**Sidecar YML** (required):
```yaml
name: "Welcome Lobby"
description: "Animated Halloween-themed lobby welcome"
tiles-w: 3
tiles-h: 1
permission: ""
user-placeholders: {}

data-points:
  title:
    tile-x: 0
    tile-y: 0
    x: 8
    y: 30
    size: 22
    text: "<gold><bold>Welcome</bold></gold>"

  subtitle:
    tile-x: 0
    tile-y: 0
    x: 8
    y: 80
    size: 12
    text: "<gray>%player_name%, enjoy your stay</gray>"

  footer:
    tile-x: 0
    tile-y: 0
    x: 8
    y: 105
    size: 10
    text: "<dark_gray>TPS: %server_tps% · Players: %server_online%</dark_gray>"
```

See the [main plugin README](https://github.com/Kterrali/hudboard#-data-point-format) for the full data-point spec.

### 4. Add a `README.md`

Brief description of what's in the pack, screenshots, credits.

### 5. Tag a release

```bash
git add packs/<your-pack-slug>/
git commit -m "Pack: <Your Pack Name>"
git tag v1.0.0-<pack-slug>   # this triggers the CI
git push origin main --tags
```

The CI will:
1. Build a ZIP of your pack
2. Attach it to a GitHub Release
3. (Optional) Update the [main plugin repo's](https://github.com/Kterrali/hudboard) README to list your pack

---

## 📤 Submit a pack

Want your pack listed here? Open a PR with:
- The pack folder in `packs/<your-slug>/`
- A `manifest.json`
- 1-2 screenshots

Maintainer (Kterrali) reviews for:
- Quality of art
- YML validity
- License (must be Apache-2.0 or compatible)

---

## 🐛 Issues

Pack not loading? Panel looks broken? → https://github.com/Kterrali/hudboard-packs/issues

---

## 📜 License

Apache License 2.0 — see [LICENSE](LICENSE).

Each pack may have additional credits in its own README.md.
