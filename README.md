# Novel Signature Homes — 360 Tours

**Repository purpose**: This repository hosts the static frontend assets for Novel Signature Homes' proprietary 360° property tours (HTML/CSS/JS). The repository is public only to enable GitHub Pages hosting of the tours; the content and assets are proprietary to Novel Signature Homes and not intended for reuse outside the organization.

**Repository scope**
- **What this contains:** static tour folders (each tour has an `index.html`, `pano.xml`, images, tiles, and player scripts).
- **What this does not contain:** backend services, private customer data, or third-party non-public assets.

**Project layout (top-level)**
- `amherst/`, `potomac-large-house/`, `potomac-small-house_a/`, `potomac-small-house_b/`, ... — individual tour folders
- `README.md` — this file
- `LICENSE` — project license and usage restrictions
- `CONTRIBUTING.md` — contribution policy (internal only)

**Previewing locally**
1. From the repo root run a simple static server in your shell (example):

```bash
python3 -m http.server 8000
# then open http://localhost:8000/amherst/ (or any tour folder)
```

or use any static server you prefer (e.g., `live-server`, `http-server`).

**GitHub Pages**
- This repository is public so GitHub Pages can serve the static tours. All assets served from GitHub Pages are publicly accessible; do not store private or sensitive data in this repo.

**License & usage**
- The tours, images, tiles, scripts and other assets are proprietary to Novel Signature Homes. See `LICENSE` for full terms. External reuse, redistribution, or modification of these assets is prohibited without express written permission.

**Contributions**
- External contributions are not accepted. See `CONTRIBUTING.md` for the internal contributor workflow and rules.

**Security and reporting**
- If you discover a security issue or accidental leak related to these tours, report it through internal security channels — do not open a public issue that may expose details.

**Contact / Owners**
- Maintained by Novel Signature Homes engineering. For access, deployment, or questions use your internal org channels.

Thank you — this repo hosts the company's official 360° tour frontends and is managed internally.
