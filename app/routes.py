from flask import Blueprint, jsonify, render_template
import plotly.express as px

routes = Blueprint('routes', __name__)

@routes.route("/")
def home():
    return render_template("index.html")

@routes.route('/generate-graph', methods=['GET'])
def generate_graph():
    fig = px.bar(x=["a", "b", "c"], y=[1, 3, 2])
    graph_html = fig.to_html()   

    with open('graph.html', 'w') as f:
        f.write(graph_html)

    return jsonify({"graph_html": graph_html})
