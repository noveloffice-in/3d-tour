#!/usr/bin/env python3

import json
import os
import re
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT_PATH = ROOT / "assets" / "data" / "tours.json"


EXCLUDE_DIRS = {
    ".git",
    "assets",
    "media",
    "tiles",
}


def title_from_slug(slug: str) -> str:
    cleaned = slug.replace("_", " ").replace("-", " ")
    cleaned = re.sub(r"\s+", " ", cleaned).strip()
    return " ".join(w[:1].upper() + w[1:] for w in cleaned.split(" ") if w)


@dataclass(frozen=True)
class Tour:
    slug: str
    title: str
    href: str
    preview: str | None


def is_tour_dir(path: Path) -> bool:
    if not path.is_dir():
        return False
    if path.name in EXCLUDE_DIRS or path.name.startswith("."):
        return False

    # Heuristic: a Pano2VR export folder generally has these.
    return (path / "gginfo.json").is_file() and (path / "index.html").is_file()


def get_preview(path: Path) -> str | None:
    gginfo = path / "gginfo.json"
    if gginfo.is_file():
        try:
            data = json.loads(gginfo.read_text(encoding="utf-8"))
            img = (data.get("preview") or {}).get("img")
            if isinstance(img, str) and img:
                candidate = path / img
                if candidate.is_file():
                    return f"{path.name}/{img}"
        except Exception:
            pass

    # Common fallback names
    for name in ("preview.jpg", "preview.png", "thumb.jpg", "thumb.png"):
        candidate = path / name
        if candidate.is_file():
            return f"{path.name}/{name}"

    return None


def main() -> int:
    tours: list[Tour] = []

    for child in sorted(ROOT.iterdir(), key=lambda p: p.name.lower()):
        if not is_tour_dir(child):
            continue

        slug = child.name
        tours.append(
            Tour(
                slug=slug,
                title=title_from_slug(slug),
                href=f"{slug}/",
                preview=get_preview(child),
            )
        )

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    from datetime import datetime, timezone

    payload = {
        "generatedAt": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "count": len(tours),
        "tours": [
            {
                "slug": t.slug,
                "title": t.title,
                "href": t.href,
                "preview": t.preview,
            }
            for t in tours
        ],
    }

    OUT_PATH.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(f"Wrote {OUT_PATH.relative_to(ROOT)} with {len(tours)} tours")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
