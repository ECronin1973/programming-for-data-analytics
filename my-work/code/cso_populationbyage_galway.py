#!/usr/bin/env python3
"""Plot Galway population by single-year age and save a timestamped PNG.

Author: Edward Cronin

Filters `cso-populationbyage.csv` for CensusYear 2022 and the two Galway
councils (Galway City Council and Galway County Council), aggregates their
populations by single-year age, plots a bar chart (Age vs Population), adds
a small ledger box with summary stats, and saves a timestamped PNG to
`my-work/generated_charts/`.
"""

import re
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from datetime import datetime
import sys

FNAME = 'cso-populationbyage.csv'
OUT_DIR_NAME = 'generated_charts'
SEARCH_LEVELS = 4


def find_data_file(start: Path, name: str, levels: int = SEARCH_LEVELS) -> Path | None:
    p = start
    for _ in range(levels):
        if (p / 'data' / name).exists():
            return p / 'data' / name
        if (p / 'code' / 'data' / name).exists():
            return p / 'code' / 'data' / name
        p = p.parent
    return None


def parse_age_label(label: str) -> int | None:
    if not isinstance(label, str):
        return None
    s = label.strip()
    if s.lower().startswith('under'):
        return 0
    if s.lower() == 'all ages':
        return None
    m = re.search(r"(\d+)", s)
    return int(m.group(1)) if m else None


def resolve_out_dir(csv_path: Path, here: Path) -> Path:
    p = Path(csv_path)
    for anc in p.parents:
        if anc.name == 'my-work':
            return anc / OUT_DIR_NAME
    if len(p.parents) >= 2:
        return p.parents[1] / OUT_DIR_NAME
    return here.parent / OUT_DIR_NAME


def main() -> None:
    HERE = Path(__file__).resolve().parent
    csv_path = find_data_file(HERE, FNAME) or find_data_file(Path.cwd(), FNAME)
    if csv_path is None:
        raise FileNotFoundError(f"Put '{FNAME}' in a nearby data/ folder (tried up to {SEARCH_LEVELS} parents).")

    df = pd.read_csv(csv_path)

    # Filter for CensusYear 2022 and Galway councils
    df['CensusYear'] = pd.to_numeric(df['CensusYear'], errors='coerce') if 'CensusYear' in df.columns else None
    mask = pd.Series(True, index=df.index)
    if 'CensusYear' in df.columns:
        mask = mask & (pd.to_numeric(df['CensusYear'], errors='coerce') == 2022)
    # Keep only Galway City and Galway County councils
    galway_names = ['Galway City Council', 'Galway County Council']
    if 'Administrative Counties' in df.columns:
        mask = mask & df['Administrative Counties'].isin(galway_names)
    # Also prefer both sexes
    if 'Sex' in df.columns:
        mask = mask & (df['Sex'].astype(str) == 'Both sexes')

    df_gal = df[mask].copy()
    if df_gal.empty:
        raise RuntimeError('No Galway rows found for CensusYear 2022')

    # Parse ages
    df_gal['AgeNum'] = df_gal['Single Year of Age'].apply(parse_age_label)
    df_gal = df_gal.dropna(subset=['AgeNum']).copy()
    df_gal['AgeNum'] = df_gal['AgeNum'].astype(int)
    df_gal['VALUE'] = pd.to_numeric(df_gal['VALUE'], errors='coerce')
    df_gal = df_gal.dropna(subset=['VALUE'])

    # Aggregate Galway City + County by age
    agg = df_gal.groupby('AgeNum', sort=True)['VALUE'].sum().reset_index()

    # Plot: color each age using a colormap
    fig, ax = plt.subplots(figsize=(12,6))
    ages = agg['AgeNum'].to_numpy()
    vals = agg['VALUE'].to_numpy()
    # Use a continuous colormap so each age has its own color
    cmap = plt.get_cmap('viridis')
    norm = plt.Normalize(vmin=ages.min(), vmax=ages.max())
    colors = cmap(norm(ages))
    bars = ax.bar(ages, vals, color=colors, width=0.8)
    ax.set_xlabel('Age (years)')
    ax.set_ylabel('Population')
    ax.set_title('Galway County (Galway City Council and Galway County Council)')
    ax.grid(axis='y', linestyle='--', alpha=0.4)
    # Add a colorbar showing the age mapping
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])
    cbar = fig.colorbar(sm, ax=ax, orientation='vertical', pad=0.02)
    cbar.set_label('Age (years)')

    # Ledger: simple box with totals and a few stats
    total_pop = int(agg['VALUE'].sum())
    median_age = float(agg.loc[agg['VALUE'].cumsum() >= total_pop/2, 'AgeNum'].iloc[0]) if not agg.empty else None
    top_ages = agg.nlargest(5, 'VALUE')
    ledger_lines = [f'Total pop: {total_pop:,}', f'Median age (approx): {median_age:.1f}' if median_age is not None else 'Median age: N/A', '', 'Top ages:']
    ledger_lines += [f"{int(r['AgeNum'])}: {int(r['VALUE']):,}" for _, r in top_ages.iterrows()]
    # Draw ledger box on the plot
    props = dict(boxstyle='round', facecolor='white', alpha=0.85)
    ax.text(0.98, 0.98, '\n'.join(ledger_lines), transform=ax.transAxes, fontsize=9,
            va='top', ha='right', bbox=props)

    # Annotate values above bars every 10 years (0,10,20,...)
    y_min, y_max = ax.get_ylim()
    y_span = y_max - y_min
    y_offset = y_span * 0.01
    for age, val, bar in zip(ages, vals, bars):
        if int(age) % 10 == 0:
            ax.text(age, val + y_offset, f'{int(val):,}', ha='center', va='bottom', fontsize=8)

    # Add a linear trend (slope) line to show age-related change
    if len(ages) >= 2:
        coeffs = np.polyfit(ages, vals, 1)
        fitted = np.polyval(coeffs, ages)
        ax.plot(ages, fitted, color='red', linestyle='--', linewidth=2, label=f'Trend (slope={coeffs[0]:.1f} pop/yr)')
        ax.legend(loc='upper right')

    # Save
    out_dir = resolve_out_dir(csv_path, HERE)
    out_dir.mkdir(parents=True, exist_ok=True)
    ts = datetime.now().strftime('%Y-%m-%d_%H%M%S')
    outfile = out_dir / f'cso-populationbyage_galway_{ts}.png'
    fig.savefig(outfile, dpi=150, bbox_inches='tight')
    print('Saved:', outfile.resolve())
    plt.show()


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print('Error:', e)
        sys.exit(1)
