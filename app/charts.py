import plotly as plt
import plotly.offline as plto

class charts():
    '''
    <h1>charts</h1>
    <p>manage the ploting of charts</p>
    <h3>author: D4vsus</h3>
    '''

    def plotChart(chart:plt.graph_objs.Figure):
        '''
        <h1>plotChart()</h1>
        Return a HTML div code from the graph
        <h3>author: <a>D4vsus</a></h3>
        '''
        return plto.plot(chart, include_plotlyjs=False, output_type='div')