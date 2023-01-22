from flask import Flask, render_template, request
from algorithm import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/index.html')
def main():
    return render_template("index.html")

@app.route('/findMatch.html')
def findMatch():
    return render_template("findMatch.html")

@app.route('/findMatch.html', methods=['POST'])
def formPost():
    puid = request.form['text'].upper()
    output = ""
    for element in calculateMatch(puid):
        output += "<div><h1>"
        output += element[0] + " " + element[1] + " " + element[2] + " " + element[3] + "</h1></div>"

    return output; 

if __name__ == "__main__":
    app.run(debug=True)