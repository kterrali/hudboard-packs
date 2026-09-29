# Template Pack

A starter template showing how HudBoard content packs are structured.

This pack contains 3 demo panels (2 PNG + 1 GIF placeholder) that you can use as a starting point for your own themed packs.

## Contents

| File | Type | Description |
|------|------|-------------|
| `welcome-lobby.png` + `.yml` | 3×1 PNG | Static welcome panel with placeholders |
| `server-status.png` + `.yml` | 2×2 PNG | Static server info (TPS, players, balance) |
| `loading.gif` + `.yml` | 1×1 GIF | Animated loading indicator (placeholder) |

## Usage

1. Download the ZIP from [Releases](https://github.com/Kterrali/hudboard-packs/releases)
2. Extract into `plugins/HudBoard/panels/`
3. `/hudboard reload`
4. `/hudboard panel place welcome-lobby`

## Customizing for your own pack

1. Replace the PNG/GIF files with your own artwork
2. Update the yml sidecars to match your new art (x/y/size/text per data point)
3. Update `manifest.json` (name, slug, version, description, panels count)
4. Open a PR or push to your fork

## Tips

- Recommended panel size: **3×1 tiles** (384×128 px) — fits standard lobbies
- Keep GIFs under 500 KB for smooth rendering
- Use MiniMessage tags in data-point text for colors: `<gold>...</gold>`, `<gradient:red:blue>...</gradient>`
- See the [main plugin README](https://github.com/Kterrali/hudboard) for the full data-point spec

## License

Apache-2.0
