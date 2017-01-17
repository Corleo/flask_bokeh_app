import numpy as np

from bokeh.layouts import column
from bokeh.models import ColumnDataSource, Slider
from bokeh.plotting import figure


def _slider_func(doc):
    x = np.linspace(0, 10, 1000)
    y = np.log(x) * np.sin(x)

    source = ColumnDataSource(data=dict(x=x, y=y))

    plot = figure()
    plot.line('x', 'y', source=source)

    slider = Slider(start=1, end=10, value=1, step=0.1)

    def callback(attr, old, new):
        y = np.log(x) * np.sin(x*new)
        source.data = dict(x=x, y=y)
    slider.on_change('value', callback)

    doc.add_root(column(slider, plot))
