import plotly as plt
import plotly.offline as plto
from flask import Blueprint, jsonify, render_template, request
import pandas as pd
from werkzeug.datastructures import FileStorage
from pathlib import Path
from .FormatNotSupportedError import FormatNotSupportedError

class charts():
    '''
    <h1>charts</h1>
    <p>manage the ploting of charts</p>
    <h3>author: D4vsus</h3>
    '''

    def plotChart(chart:plt.graph_objs.Figure):
        '''
        # plotChart()
        Return a HTML div code from the graph
        ### author: D4vsus
        '''
        return plto.plot(chart, include_plotlyjs=False, output_type='div')
    
    def importDataFrame(file: FileStorage):
        '''
        # importDataFrame()
        Return a pandas dataframe from a file with the extension:
        csv,xslx,json or xml
        ### author: D4vsus
        '''
        dataframe: pd.DataFrame
    
        match(Path(file.filename.lower()).suffix):

            case ".csv":
                return pd.read_csv(file)
            
            case ".xlsx":
                return pd.read_excel(file)
            
            case ".xml":
                return pd.read_xml(file)
            
            case ".json":
                return pd.read_json(file)
            
            case _:
                
                # If the format is not supported, raise an exception
                raise FormatNotSupportedError("Not supported file format",400)