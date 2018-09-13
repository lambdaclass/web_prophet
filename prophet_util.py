from io import BytesIO
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
from fbprophet import Prophet
from fbprophet.plot import add_changepoints_to_plot
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg


def create_plots(filepath):
    fig1, fig2 = get_figures(filepath)
    canvas1 = FigureCanvasAgg(fig1)
    canvas2 = FigureCanvasAgg(fig2)
    buf1 = BytesIO()
    buf2 = BytesIO()

    with open('static/img/img1.png', 'wb') as file1:
        canvas1.print_png(buf1)
        file1.write(buf1.getvalue())
    with open('static/img/img2.png', 'wb') as file2:
        canvas2.print_png(buf2)
        file2.write(buf2.getvalue())


def get_figures(filepath):
    df = pd.read_csv(filepath)
    df.columns = ['ds', 'y']
    m = Prophet().fit(df)
    future = m.make_future_dataframe(periods=365)
    forecast = m.predict(future)
    fig1 = m.plot(forecast)
    a = add_changepoints_to_plot(fig1.gca(), m, forecast)
    print(a)
    fig2 = m.plot_components(forecast)
    return fig1, fig2
