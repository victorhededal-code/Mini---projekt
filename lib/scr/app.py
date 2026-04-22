from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)


@app.route("/")
def landing():
    return render_template("index.html")   

@app.route("/create", methods=['POST', 'GET']) 
def create():
    return render_template("create_character.html")


app.run(debug=True)