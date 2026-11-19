#!/usr/bin/env python3
"""Optimise les photos du site Lugaz & Fils.

Entrée  : assets/img/originals/<nom>.jpg|jpeg|png|webp  (originaux, jamais modifiés)
Sortie  : assets/img/gen/<nom>-<largeur>.webp           (versions responsives)
          _data/images.yml                              (dimensions, lues par Jekyll)

Lancé automatiquement par GitHub Actions à chaque envoi. Les fichiers générés
ne sont pas commités : ils existent seulement pendant la construction du site.
Usage local (facultatif) : python tools/optimize_images.py
"""
import re
import sys
from pathlib import Path

from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "assets" / "img" / "originals"
OUT = ROOT / "assets" / "img" / "gen"
DATA = ROOT / "_data" / "images.yml"
WIDTHS = [480, 800, 1200, 1600]
QUALITY = 76
EXTS = {".jpg", ".jpeg", ".png", ".webp"}


def slug(name: str) -> str:
    return re.sub(r"[^a-z0-9-]+", "-", name.lower()).strip("-")


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    files = sorted(p for p in SRC.glob("*") if p.suffix.lower() in EXTS)
    entries = {}
    for path in files:
        name = slug(path.stem)
        try:
            im = ImageOps.exif_transpose(Image.open(path))
        except Exception as exc:  # image illisible : on continue
            print(f"! {path.name} ignorée ({exc})")
            continue
        if im.mode not in ("RGB", "RGBA"):
            im = im.convert("RGB")
        w, h = im.size
        sizes = [x for x in WIDTHS if x < w] + ([w] if w <= WIDTHS[-1] else [])
        if not sizes:
            sizes = [w]
        sizes = sorted(set(sizes))
        for target in sizes:
            th = round(h * target / w)
            out = im if target == w else im.resize((target, th), Image.LANCZOS)
            out.save(OUT / f"{name}-{target}.webp", "WEBP", quality=QUALITY, method=6)
        entries[name] = {"w": w, "h": h, "ws": sizes}
        print(f"✓ {name}: {w}x{h} -> {sizes}")

    lines = ["# Fichier généré par tools/optimize_images.py : ne pas modifier à la main."]
    if not entries:
        lines.append("{}")
    for name, d in entries.items():
        lines.append(f"{name}:")
        lines.append(f"  w: {d['w']}")
        lines.append(f"  h: {d['h']}")
        lines.append(f"  ws: [{', '.join(str(x) for x in d['ws'])}]")
    DATA.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"{len(entries)} image(s) traitée(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
