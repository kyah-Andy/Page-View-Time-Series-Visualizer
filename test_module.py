import matplotlib as mpl
import pandas as pd
import unittest

import time_series_visualizer


def test_draw_line_plot():
    fig = time_series_visualizer.draw_line_plot()
    assert isinstance(fig, mpl.figure.Figure)


def test_draw_bar_plot():
    fig = time_series_visualizer.draw_bar_plot()
    assert isinstance(fig, mpl.figure.Figure)


def test_draw_box_plot():
    fig = time_series_visualizer.draw_box_plot()
    assert isinstance(fig, mpl.figure.Figure)