"""Adds xkcd font to `matplotlib`."""

from __future__ import annotations

import pathlib

import matplotlib.font_manager

if __name__ == '__main__':
    font_path = pathlib.Path('/usr/share/fonts/OTF/xkcd.otf')
    matplotlib.font_manager.fontManager.addfont('/usr/share/fonts/OTF/xkcd.otf')
