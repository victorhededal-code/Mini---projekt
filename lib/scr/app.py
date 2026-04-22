from flask import Flask, render_template, redirect, url_for, request

# pip install Flask
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/create_character', methods =['POST', 'GET'])
def create_character():
    render_template('/create_character.html')

@app.route('/saved_characters', methods =['POST', 'GET'])
def saved_characters():
    render_template('/saved_characters.html')

@app.route('/about_us', methods =['POST', 'GET'])
def about_us():
    render_template('/about_us.html')