#!/usr/bin/env python3
"""PMcolours: page colour from shade words in the product name (chameleons get two colours)."""
import json, re, sys, unicodedata
f = sys.argv[1]
d = json.load(open(f))
W = [  # (regex on ascii-lowercased name, hex) – order matters: specific first
 (r'midnight blue|tmave modr|navy', '#0b1f6b'), (r'blood red|apple red|ruby|rubin', '#b3001b'), (r'burgund|vinov', '#6d0f2a'),
 (r'tyrkys|turquois|petrol', '#0aa5a5'), (r'azure|svetle modr|sky', '#2f8fff'), (r'emerald|smaragd', '#0b8f55'),
 (r'lime|limet', '#8fd400'), (r'army', '#4f6b2a'), (r'olive|oliv', '#6b7a1f'), (r'amethyst|ametyst|purpur', '#7a2fbf'),
 (r'lemon|citron', '#f5d90a'), (r'solargold|golden|zlat|gold', '#d4a017'), (r'bronz|bronze|old time', '#8c6a2a'),
 (r'meden|copper|med\b', '#b05a2a'), (r'oranz|orange|tangerin', '#ff6a00'), (r'ruzov|pink|magent|fuchsi', '#e0218a'),
 (r'fialov|purple|violet|lila', '#6a1fb0'), (r'cervena|cerven|red', '#d0101e'), (r'modr|blue', '#1747d1'),
 (r'zelen|green', '#139a3a'), (r'zlut|yellow', '#f2c200'), (r'stribr|silver', '#a9b3bd'), (r'cern|black', '#2a2a2e'),
 (r'bil[aeo]|white', '#d9dde3'), (r'sed[aeo]|grey|gray', '#7d848c'), (r'hned|brown', '#6b3e1f'),
]
def ascii(s): return unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode().lower()
for p in d['products']:
    p.pop('col', None)
    if p['cat'] == 'prislusenstvi': continue
    n = ascii(p['name']['cs'])
    hits = []
    for rx, h in W:
        for m in re.finditer(rx, n):
            hits.append((m.start(), h))
    hits.sort()
    cols = list(dict.fromkeys(h for _, h in hits))
    if cols:
        p['col'] = cols[0]
        if len(cols) > 1: p['col2'] = cols[-1]
json.dump(d, open(f, 'w'), ensure_ascii=False, separators=(',', ':'))
print(sum(1 for p in d['products'] if 'col' in p), 'coloured of', len(d['products']))
