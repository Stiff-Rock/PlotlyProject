import plotly as plt
import plotly.offline as plto
import plotly.graph_objects as go
import plotly.express as px
from flask import Blueprint, request
import pandas as pd
from werkzeug.datastructures import FileStorage
from pathlib import Path
from .FormatNotSupportedError import FormatNotSupportedError

class charts():
    '''
    # charts
    manage the ploting of charts
    ### author: [D4vsus](https://github.com/D4vsus)
    '''

    def plotChart(chart:plt.graph_objs.Figure):
        '''
        # plotChart()
        Return a HTML div code from the graph
        ### author: [D4vsus](https://github.com/D4vsus)
        '''
        return plto.plot(chart, include_plotlyjs=False, output_type='div')
    
    def importDataFrame(file: FileStorage):
        '''
        # importDataFrame()
        Return a pandas dataframe from a file with the extension:
        csv,xslx,json or xml
        ### author: [D4vsus](https://github.com/D4vsus)
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
    
    def buildChart(dataframe:pd.DataFrame,type_chart:str,titel='') -> go.Figure:
        '''
        # buidChart()
        Create the chart.
        possible values of \'type_chart\': 
        scatter and bar
        ### author: [D4vsus](https://github.com/D4vsus)
        '''
        bar:go.Figure
        
        match type_chart:
            case "scatter":
                bar = px.scatter(data_frame=dataframe,                     
                        # TODO: use a "select" from the html to get the columns x and y, for the chart
                        x=dataframe.columns[0],
                        y=dataframe.columns[1],
                        title=titel)
            case "bar":
                bar = px.bar(data_frame=dataframe,
                            # TODO: use a "select" from the html to get the columns x and y, for the chart
                            x=dataframe.columns[0],
                            y=dataframe.columns[1],
                            title=titel)      
            case _:
                  bar = px.scatter(data_frame=dataframe,                     
                        # TODO: use a "select" from the html to get the columns x and y, for the chart
                        x=dataframe.columns[0],
                        y=dataframe.columns[1],
                        title=titel)
        return bar 
         