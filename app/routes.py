from flask import Blueprint, jsonify, render_template
import plotly.express as px
import plotly.offline as pyo
import plotly.graph_objects as go
from .charts import charts
routes = Blueprint('routes', __name__)

@routes.route("/")
def home():
    return render_template("index.html")

@routes.route('/generate-graph', methods=['GET'])
def generate_graph():
    fig = go.Figure(
    data=[go.Scatter(x=[1, 2, 3, 4], y=[10, 20, 15, 30], mode='lines+markers')],
    layout=go.Layout(title="Scatter Plot Example")
)
    graph_html = pyo.plot(fig, include_plotlyjs=False, output_type='div')

    return jsonify({"graph_html": charts.plotChart(fig)})
