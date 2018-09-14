from io import BytesIO
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from fbprophet import Prophet
from fbprophet.plot import add_changepoints_to_plot
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg


def create_plots(filepath):
    forecast_fig, components_fig = get_figures(filepath)
    forecast_canvas = FigureCanvasAgg(forecast_fig)
    components_canvas = FigureCanvasAgg(components_fig)
    buf1 = BytesIO()
    buf2 = BytesIO()

    with open('static/img/img1.png', 'wb') as forecast_file:
        forecast_canvas.print_png(buf1)
        forecast_file.write(buf1.getvalue())
    with open('static/img/img2.png', 'wb') as components_file:
        components_canvas.print_png(buf2)
        components_file.write(buf2.getvalue())


def get_figures(filepath):
    df = pd.read_csv(filepath)
    df.columns = ['ds', 'y']
    m = Prophet().fit(df)
    future = m.make_future_dataframe(periods=365)
    forecast = m.predict(future)
    forecast_fig = m.plot(forecast)
    add_changepoints_to_plot(forecast_fig.gca(), m, forecast)
    components_fig = m.plot_components(forecast)
    return forecast_fig, components_fig
