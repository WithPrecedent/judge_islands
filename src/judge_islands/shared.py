"""Makes visuals for the Northwestern University Law Review Symposium."""

from __future__ import annotations

from typing import TYPE_CHECKING

import matplotlib.pyplot as plt
import pandas as pd

if TYPE_CHECKING:
    import pathlib


def import_data(path: str | pathlib.Path) -> pd.DataFrame:
    """Imports data into a `pandas` dataframe.

    Args:
        path: path where data in a `.csv` file is located.

    Returns:
        dataframe with loaded data.

    """
    return pd.read_csv(path)

def export_visual(path: str | pathlib.Path) -> None:
    """Exports visualization as a `.png` file.

    Args:
        path: path where file should be saved.

    """
    plt.savefig(path, bbox_inches = 'tight')
    return

def add_stick_figure(
    axes: plt.axes.Axes, 
    x: float = .5, 
    y: float = .5, 
    radius: float = .03, 
    quote: str | None = None, 
    color: str = 'k', 
    lw: int = 2, 
    xytext: tuple(int, int) = (0, 20)):
    """Adds an xkcd-style stick figure to a chart.

    This function is adapted from Alistair Miles at:
    https://alimanfoo.github.io/2016/05/31/matplotlib-xkcd.html

    Args:
        axes: _description_
        x: _description_. Defaults to .5.
        y: _description_. Defaults to .5.
        radius: _description_. Defaults to .03.
        quote: _description_. Defaults to None.
        color: _description_. Defaults to 'k'.
        lw: _description_. Defaults to 2.
        xytext: _description_. Defaults to (0, 20).

    """
    # draw the head
    head = plt.Circle(
        (x, y), 
        radius=radius, 
        transform = axes.transAxes, 
        edgecolor = color, 
        lw = lw, 
        facecolor = 'none', 
        zorder = 10)
    axes.add_patch(head)

    # Common keyword arguments for remaining calls
    kwargs = {'color': color, 'lw': lw, 'transform': axes.transAxes}

    # draw the body
    body = plt.Line2D([x, x], [y-radius, y-(radius * 4)], **kwargs)
    axes.add_line(body)

    # draw the arms
    arm1 = plt.Line2D([x, x+(radius)], [y-(radius * 1.5), y-(radius*5)], **kwargs)
    axes.add_line(arm1)
    arm2 = plt.Line2D([x, x-(radius * .8)], [y-(radius * 1.5), y-(radius*5)], **kwargs)
    axes.add_line(arm2)

    # draw the legs
    leg1 = plt.Line2D([x, x+(radius)], [y-(radius * 4), y-(radius*8)], **kwargs)
    axes.add_line(leg1)
    leg2 = plt.Line2D([x, x-(radius*.5)], [y-(radius * 4), y-(radius*8)], **kwargs)
    axes.add_line(leg2)

    # say something
    if quote is not None:
        axes.annotate(
            quote,
            xy = (x + radius, y + radius),
            xytext = xytext,
            xycoords = 'axes fraction',
            textcoords = 'offset points',
            arrowprops = {'arrowstyle': '-', 'lw': 1})
