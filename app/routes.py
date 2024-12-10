from flask import Blueprint, jsonify, render_template, request

import plotly.express as px
from .charts import charts
from .FormatNotSupportedError import FormatNotSupportedError

routes = Blueprint('routes', __name__)

@routes.route("/")
def home():
    return render_template("index.html")

@routes.route('/generate-graph', methods=['GET','POST'])
def generate_graph():

     # Check if a file is part of the request
    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400

    file = request.files['file']

    # Check if a file was actually uploaded
    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400
    
    try:
        dataframe = charts.importDataFrame(file)
    except FormatNotSupportedError as e:
        return jsonify({"error": f"{e}"}), e.code 

    # Create the chart
    fig = px.scatter(
    data_frame=dataframe,

    # TODO: use a "select" from the html to get the columns x and y, for the chart
    x=list(dataframe.columns)[0], y=(dataframe.columns)[1],

    title=file.filename,
)

    # Return the chart
    return jsonify({"graph_html": charts.plotChart(fig)})
