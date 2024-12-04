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
    fig = px.scatter(
    x=[1, 2, 3, 4], y=[10, 15, 13, 17],
    title='Scatter Plot with Customized Markers',
    labels={'x': 'X-axis', 'y': 'Y-axis'},
    color=["red", "blue", "green", "purple"],  # Marker colors
    size=[10, 20, 30, 40]  # Marker sizes
)
    fig = px.scatter_3d(
    x=[1, 2, 3, 4],
    y=[10, 15, 13, 17],
    z=[5, 7, 9, 11],
    color=["red", "blue", "green", "purple"],
    title='3D Scatter Plot',
    labels={'x': 'X-axis', 'y': 'Y-axis', 'z': 'Z-axis'}
)
    graph_html = pyo.plot(fig, include_plotlyjs=False, output_type='div')

    return jsonify({"graph_html": charts.plotChart(fig)})
