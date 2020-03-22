import json

import flask
import pandas as pd

app = flask.Flask(__name__)
@app.route("/map")
@app.route("/")
def map():
    sourceDataFrame = pd.read_csv("disaster.csv")
    dataFrameCountryMapping = pd.read_csv("countryMapping.csv")
    dataFrameCountryMapping = dataFrameCountryMapping.to_dict(orient='record')
    dataFrameCountryMapping = json.dumps(dataFrameCountryMapping)
    disasterData = sourceDataFrame.to_dict(orient='records')
    disasterData =  json.dumps(disasterData,indent=2)
    data = {'plot_data':disasterData,'country_mapping_data':dataFrameCountryMapping}
    return flask.render_template("worldmap.html", data=data)
@app.route("/requestRadialStackBar")
def radialStackBar():
    stackBarData = pd.read_csv("stackBarData.csv")
    stackBarData = stackBarData.to_dict(orient='record')
    stackBarData = json.dumps(stackBarData)
    dataFrameCountryMapping = pd.read_csv("countryMapping.csv")
    dataFrameCountryMapping = dataFrameCountryMapping.to_dict(orient='record')
    dataFrameCountryMapping = json.dumps(dataFrameCountryMapping)
    data = {'stack_bar_data':stackBarData,'country_mapping_data':dataFrameCountryMapping}
    return flask.render_template("radialStackBar.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)
