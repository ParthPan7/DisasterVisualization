import json

import flask
import pandas as pd

app = flask.Flask(__name__)

@app.route("/")
def index():

    return flask.render_template("index.html")


@app.route("/requestRadialStackBar")
def radialStackBar():
    stackBarData = pd.read_csv("stackBarData.csv")
    stackBarData = stackBarData.to_dict(orient='record')
    stackBarData = json.dumps(stackBarData)
    dataFrameCountryMapping = pd.read_csv("countryMapping.csv")
    dataFrameCountryMapping = dataFrameCountryMapping.to_dict(orient='record')
    dataFrameCountryMapping = json.dumps(dataFrameCountryMapping)
    data = {'stack_bar_data':stackBarData,'country_mapping_data':dataFrameCountryMapping}
    return flask.render_template("radialStackBar.html",data=data)

if __name__ == "__main__":
    app.run(debug=True)
