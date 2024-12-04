import plotly as plt
import plotly.offline as plto

def plotChart(chart:plt.graph_objs.Figure):
    '''
    <h1>plotChart()</h1>
    Return a HTML div code from the graph
    <h3>author: <a>D4vsus</a></h3>
    '''
    return plto.plot(chart, include_plotlyjs=False, output_type='div')
