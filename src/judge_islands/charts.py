"""Makes visuals for the Northwestern University Law Review Symposium."""

from __future__ import annotations

import pathlib

import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import ticker

import judge_islands


def visualize_panel_effects(
    import_path: str | pathlib.Path,
    export_path: str | pathlib.Path) -> None:
    """Loads data, creates visualization, and exports image.

    Args:
        import_path: path to load data from.
        export_path: path to export visualization to.

    """
    colors_list = ['Blue', 'Skyblue', 'Salmon', 'Red']
    data = judge_islands.import_data(path = import_path)
    data['Criminal Defendant Win %'] = data['Criminal Defendant Win %'] * 100
    data_labels = data['Criminal Defendant Win %'].round(1).astype('str') + '%'
    axes = data.plot.bar(
        x = 'Number of Democrats on Panel', 
        y = 'Criminal Defendant Win %', 
        ylabel = 'Criminal Defendant Win %',
        title = 'Panel Effects in Federal Criminal Defendant\nAppeals 2008-2016 (n = 28,564)',
        rot = 0,
        edgecolor = colors_list,
        color = 'White',
        legend = False,
        ylim = (0, 15))
    judge_islands.add_stick_figure(
        axes,
        x = .3,
        y = .21,
        quote = 'No big deal',
        xytext = (-10, 10))
    for container in axes.containers:
        axes.bar_label(container, labels = data_labels)
        axes.yaxis.set_major_formatter(ticker.PercentFormatter())
    judge_islands.export_visual(path = export_path)
    plt.show()
    return

def create_visualizations() -> None:
    """Creates all visualizations"""
    sns.set_style('white')
    plt.xkcd()
    visualize_panel_effects(
        import_path = pathlib.Path(
            'data/external/panel_effects_criminal_appeals.csv'),
        export_path = pathlib.Path('results/visualizations/panel_effects.png'))

if __name__ == '__main__':
    create_visualizations()
