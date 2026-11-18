# Aktualizace dat

```bash
# 1) seznam URL produktů ze sitemapy -> urls.txt, pak šetrné stažení (4 paralelně, cache v raw/)
python3 tools/pmcolours/fetch_pages.py urls.txt raw/pages
# 2) parsování stránek (upgates | shoptet)
python3 tools/pmcolours/parse_shop.py upgates raw/pages raw/parsed.json
# 3) katalog + WebP fotky
python3 tools/pmcolours/build_catalog.py raw/parsed.json pmcolours tools/pmcolours/config.json
# 4) výřezy pro carousel
python3 tools/pmcolours/make_hero.py pmcolours <id produktu> ...
```
Potřeba: Python 3, Pillow, BeautifulSoup4, lxml, curl. Stahování respektuje robots.txt.
Po kroku 3: `python3 tools/pmcolours/pm_colors.py pmcolours/data/catalog.json` (barvy podle názvu odstínu).
