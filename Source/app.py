from flask import Flask, render_template
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')

app = Flask(__name__, template_folder=TEMPLATES_DIR)

@app.route("/") 
def index():
    return "Hello World"

@app.route("/menu")
def menu():
    return render_template("menu.html")

if __name__ == "__main__": 
    app.run(host="0.0.0.0", port=80) 