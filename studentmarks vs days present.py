import plotly.express as px
import csv
import numpy as np

def plotFigure(data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df,x="studentmarks", y="dayspresent")
        fig.show()

def getDataSource(data_path):
    ice_cream_sales = []
    cold_drink_sales = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            studentmarks.append(float(row["studentmarks"]))
            dayspresent.append(float(row["dayspresent"]))

    return {"x" : studentmarks, "y": dayspresent}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Student marks vs days present :-  \n--->",correlation[0,1])

def setup():
    data_path  = "Student Marks vs Days Present.csv"

    datasource = getDataSource(data_path)
    findCorrelation(datasource)
    plotFigure(data_path)

setup()