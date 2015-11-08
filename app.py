import soundcloud
import flickrapi

from flask import Flask, redirect, render_template, request, session

app = Flask(__name__)

@app.route("/", methods=['GET,POST'])
def home():
    return render_template("home.html")

if __name__ == '__main__':
    app.dbug = True
    app.run(host='0.0.0.0',port=8000)
