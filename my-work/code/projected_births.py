#!/usr/bin/env python3
"""Plot projected births and save a PNG.

Author: Edward Cronin

Place the CSV in a nearby `data/` folder (see code). Saves to ../generated_charts.
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from pathlib import Path
from datetime import datetime
import sys

# Config
FNAME = 'projectedbirths-cso.csv'
OUT_DIR_NAME = 'generated_charts'
SEARCH_LEVELS = 4


def find_data_file(start: Path, name: str, levels: int = SEARCH_LEVELS) -> Path | None:
	"""Look for data/<name> or code/data/<name>, moving up 'levels' parents."""
	p = start
	for _ in range(levels):
		if (p / 'data' / name).exists():
			return p / 'data' / name
		if (p / 'code' / 'data' / name).exists():
			return p / 'code' / 'data' / name
		p = p.parent
	return None


def main() -> None:
	HERE = Path(__file__).resolve().parent

	csv_path = find_data_file(HERE, FNAME) or find_data_file(Path.cwd(), FNAME)
	if csv_path is None:
		raise FileNotFoundError(f"Put '{FNAME}' in a nearby data/ folder (tried up to {SEARCH_LEVELS} parents).")

	df = pd.read_csv(csv_path)

	# Choose y column
	if 'VALUE' in df.columns:
		y_col, ylabel = 'VALUE', 'Projected Annual Births'
	elif 'BirthRate' in df.columns:
		y_col, ylabel = 'BirthRate', 'Birth Rate (per 1,000 population)'
	else:
		nums = df.select_dtypes(include=['number']).columns.tolist()
		if not nums:
			raise KeyError('No numeric column found to plot')
		y_col, ylabel = nums[-1], nums[-1]

	# Ensure numeric
	df['Year'] = pd.to_numeric(df['Year'], errors='coerce')
	df[y_col] = pd.to_numeric(df[y_col], errors='coerce')
	df_plot = df.dropna(subset=['Year', y_col]).sort_values('Year')

	# Fit a simple linear model on t = Year - min(Year)
	yr0 = int(df_plot['Year'].min())
	df_plot['t'] = df_plot['Year'] - yr0
	X = df_plot[['t']].values
	y_vals = df_plot[y_col].values
	model = LinearRegression().fit(X, y_vals)

	# Prepare future projection using the fitted model
	future_years = np.arange(df_plot['Year'].max() + 1, df_plot['Year'].max() + 31)
	t_future = (future_years - yr0).reshape(-1, 1)
	pred_future = model.predict(t_future)

	# Plot historical and projection on same axes
	fig, ax = plt.subplots(figsize=(9, 5))
	# Historical points
	ax.plot(df_plot['Year'], df_plot[y_col], 'o', color='C0', label='Historical')

	# Build a continuous fitted line over historical+future years, but draw it in two colors
	hist_years = df_plot['Year'].values
	last_hist_year = int(hist_years.max())
	combined_years = np.concatenate([hist_years, future_years])
	# Ensure strictly increasing
	combined_years = np.sort(np.unique(combined_years))
	t_combined = (combined_years - yr0).reshape(-1, 1)
	pred_combined = model.predict(t_combined)

	# Split indices for historic vs projected
	hist_mask = combined_years <= last_hist_year
	proj_mask = combined_years > last_hist_year

	# Fitted line over historical period (solid/dotted to preference)
	ax.plot(combined_years[hist_mask], pred_combined[hist_mask], linestyle=':', color='C0', label='Fitted (historical)')
	# Projection line (solid, different color) continuing from the end of historical fit
	ax.plot(combined_years[proj_mask], pred_combined[proj_mask], linestyle='-', color='C1', label='Projection (linear)')

	ax.set_title(f'Projected {ylabel} in Ireland ({yr0}–{int(future_years.max())})')
	ax.set_xlabel('Year')
	ax.set_ylabel(ylabel)
	ax.grid(True)
	ax.legend()

	# Compute combined y-limits from historical and projected values
	all_y = np.concatenate([y_vals, pred_future])
	y_min, y_max = float(all_y.min()), float(all_y.max())
	y_margin = max(1e-6, 0.05 * (y_max - y_min))
	ax.set_xlim(int(df_plot['Year'].min()) - 1, int(future_years.max()) + 1)
	ax.set_ylim(y_min - y_margin, y_max + y_margin)

	# Save (to parent my-work/generated_charts)
	out_dir = HERE.parent / OUT_DIR_NAME
	out_dir.mkdir(parents=True, exist_ok=True)
	date_only = datetime.now().strftime('%Y-%m-%d')
	outfile = out_dir / f'projected_births_{date_only}.png'
	fig.savefig(outfile, dpi=150, bbox_inches='tight')
	print(outfile.name)
	plt.show()


if __name__ == '__main__':
	try:
		main()
	except Exception as e:
		print('Error:', e)
		sys.exit(1)

