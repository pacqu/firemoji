import soundcloud
import flickrapi

from flask import Flask, redirect, render_template, request, session

app = Flask(__name__)

@app.route("/")#methods=['GET','POST'])
def home():
    #if (request.method == 'post'):
    #   return render_template("home.html")
   # else:
    return render_template("home.html")

if __name__ == '__main__':
    app.dbug = True
    app.run(host='0.0.0.0',port=8000)

#I'm testing out branches!
