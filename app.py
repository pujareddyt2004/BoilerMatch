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
    output = """
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {
                padding: 0;
                margin: 0;
                text-align: center;
                background-color: gray;
            }
            .top {
                background-color: white;
            }
            .match {
                background-color: #d5f4e6;
            }
            h1 {
                color: blue;
            }
            h2 {
                color: red;
            }
        </style>
    </head>
    """
    output += "<body><div class='top'><h1>MATCHES</h1></div><br><br>"
    index = 1

    for element in calculateMatch(puid):
        output += "<div class='match'><h2>" + str(index) + ". Name: "
        output += element[0] + " | Compatibility: " + element[2] + " | Gender: " + element[3] + "</h2></div>"
        index+=1
    output += "</body></html>"

    return output; 

if __name__ == "__main__":
    app.run(debug=True)