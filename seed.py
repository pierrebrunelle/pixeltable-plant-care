"""Seed a few houseplants.

Usage:
    python seed.py            # seeds the local `plants` catalog directory
    python seed.py my_dir     # or another directory you passed to `pxt schema update`
"""
import sys
from pathlib import Path

import pixeltable as pxt

target = sys.argv[1] if len(sys.argv) > 1 else 'plants'
HERE = Path(__file__).resolve().parent

SEED = {
    'plants': [
        {'species': 'Monstera deliciosa', 'location': 'living room', 'moisture': 'slightly-dry', 'days_since_water': 6, 'notes': None},
        {'species': 'Snake plant', 'location': 'bedroom', 'moisture': 'dry', 'days_since_water': 14, 'notes': 'likes neglect'},
        {'species': 'Fiddle leaf fig', 'location': 'office', 'moisture': 'moist', 'days_since_water': 2, 'notes': None},
    ],
}

for table_name, rows in SEED.items():
    t = pxt.get_table(f'{target}/{table_name}')
    if t.count() > 0:
        print(f'{target}/{table_name} already has {t.count()} rows; skipping')
        continue
    for row in rows:
        for k, v in row.items():
            if isinstance(v, str) and v.startswith('data/'):
                row[k] = str(HERE / v)   # local sample media file
    t.insert(rows)
    print(f'inserted {len(rows)} rows into {target}/{table_name}')
