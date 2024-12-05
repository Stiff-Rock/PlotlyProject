from flask import Blueprint, jsonify, render_template
import plotly.graph_objects as go
from .charts import plotChart

routes = Blueprint('routes', __name__)

@routes.route("/")
def home():
    return render_template("index.html")

@routes.route('/generate-graph', methods=['GET'])
def generate_graph():
    ages = [10, 20, 30, 40, 50, 60]  
    incomes = [1000, 2000, 3000, 4000, 5000, 6000] 

    fig = go.Figure(
        data=[
            go.Scatter(
                x=ages, 
                y=incomes, 
                mode='lines+markers', 
                marker=dict(color='blue', size=8), 
                line=dict(color='blue', width=2)
            )
        ],
        layout=go.Layout(
            title="Relación entre Edad e Ingreso",
            xaxis=dict(title="Edad (años)"),
            yaxis=dict(title="Ingreso ($)"),
            template="plotly_white"
        )
    )

    return jsonify({"graph_html": plotChart(fig)})
