from flask import Flask, render_template, request
from calc import CSVParser
import pandas as pd


app = Flask(__name__)

@app.route("/")
def index():
    data = {'WAM': 85.345}
    return render_template("index.html", data=data)

@app.route("/", methods=['POST'])
def upload():
    file = request.files.get('uploaded_file')
    data = calc_wam(file)
    return render_template("index.html", data=data)

def calc_wam(file):
    parser = CSVParser()
    parser.read_transcript(file)
    return {'WAM': parser.calc_wam()}

if __name__ == "__main__":
    app.run(debug=True)
