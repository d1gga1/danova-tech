#!/bin/bash
# 24/10/2026 - Rigenera tutta la sezione Danova Real Estate e la catena post-build. Uso: bash seo-tools/real-estate-tutto.sh
set -e
cd "$(dirname "$0")/.."
python3 seo-tools/real-estate-media.py
python3 seo-tools/real-estate-build.py | tail -1
for s in post-build-contatti post-build-velocita schema-licenza-eventi org-descrizione patch-2026-10-17-facebook patch-2026-10-17-instagram patch-2026-10-17-tiktok whatsapp-2026-10-23 menu-video-2026-10-23 real-estate-sito real-estate-guide real-estate-llms real-estate-tema genera-sitemap genera-feed-e-llms; do
  [ -f seo-tools/$s.py ] && { echo "== $s"; python3 seo-tools/$s.py | tail -2; }
done
