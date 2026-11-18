# PMcolours – koncept nového e-shopu

Statický frontend (HTML + CSS + vanilla JS, bez buildu) pro pmcolours.cz. Stejný designový jazyk jako koncepty Montana Cans a Autolaky (tmavý rám, zaoblené plochy, plovoucí pill menu, obří „ghost“ nápisy, pozadí stránky se přebarvuje podle vybraného produktu nebo odstínu).

**Jde o neoficiální návrh** – stránka má trvalý pruh „KONCEPT“, vodoznak a `noindex`.

## Co umí
- **Kompletní katalog** – 196 produktů v 10 kategoriích (Chameleon, Candy, Candy Pearl, perleť, Ghost perleť, hologram a třpytky, podklady, renovační sady, laky, příslušenství).
- Carousel ze vzorníků („speed shape“) a stránka se přebarví podle odstínu v názvu produktu – u Chameleonů přechodem dvou barev.
- Shop s kategoriemi, hledáním, řazením, filtrem „jen skladem“, košík s ukazatelem dopravy zdarma nad 2 000 Kč.

## Poctivě
- Barva pozadí se odvozuje ze slov v názvu odstínu (např. „Blood Red“, „Midnight Blue“) – je orientační.

## Spuštění lokálně
```bash
cd pmcolours
python3 -m http.server 8000   # http://localhost:8000
```
Katalog se načítá přes `fetch`, otevření `index.html` přímo ze souboru nefunguje.

## Nasazení
Kořenový `index.html` přesměruje do `pmcolours/`. Settings → Pages → Source: **GitHub Actions** (workflow `.github/workflows/pages.yml` nasazuje při pushi do `main`). Po prvním zapnutí Pages je potřeba workflow jednou spustit ručně (Actions → Run workflow).

## Struktura
- `index.html`, `css/style.css`, `js/app.js` – sdílená šablona (router `#/`, `#/shop/:kat/:podkat`, `#/p/:id?v=varianta`, `#/o-nas`, `#/kontakt`)
- `js/shop.js` – vše specifické pro obchod (kontakty, carousel, barvy kategorií, texty)
- `data/catalog.json` – katalog; `assets/img/p/` – fotky (WebP), `assets/img/hero/` – výřezy pro carousel

## Co ještě chybí do ostrého provozu
- Platby, sklad a objednávky v reálném čase – statický web nic nesynchronizuje, ceny a sklad jsou snímek ze 18. 11. 2026. Objednávka zatím odchází e-mailem (mailto).
- Napojení na stávající platformu (nebo jinou) rozhodne majitel.

Data se generují skripty v `tools/pmcolours/`.
