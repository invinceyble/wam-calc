from flask import Flask, render_template, request
from parser import Parser
import pandas as pd

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/results", methods=['POST'])
def results():
    file = request.files.get('uploaded_file')
    if file is None:
        return index()
    data = calc_wam(file)
    return render_template("results.html", data=data)

def calc_wam(file):
    parser = Parser()
    parser.read_transcript(file)
    return {'WAM': parser.calc_wam()}

if __name__ == "__main__":
    app.run(debug=False)
