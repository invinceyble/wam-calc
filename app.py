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
    text = request.form['uploaded_text']

    if file:
        data = calc_wam_file(file)
    elif text:
        data = calc_wam_text(text)
    else:
        return index()

    return render_template("results.html", data=data)

def calc_wam_file(file):
    parser = Parser()
    parser.read_transcript(file)
    return {'WAM': parser.calc_wam()}

def calc_wam_text(text):
    parser = Parser()
    parser.read_text(text)
    return {'WAM': parser.calc_wam()}

if __name__ == "__main__":
    app.run(debug=False)
