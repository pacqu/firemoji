import soundcloud
import flickrapi

from flask import Flask, redirect, render_template, request, url_for
import utils

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def home():
    if request.method == "GET":
        return render_template("home.html")
    else:
        keyword = request.form['keyword']
        imgset = utils.getImgSet(keyword)
        soundset = utils.getSoundSet(keyword)
        return redirect(url_for('result',keyword=keyword,imgset=imgset,soundset=soundset))

@app.route("/result",methods=["GET","POST"])
def result(keyword="",imgset=[],soundset=[]):
    if request.method == "GET":
        return render_template("newsult.html",keyword=keyword,imgset=imgset,soundset=soundset)
    else:
        #something for back button here
        return render_template("newsult.html",keyword=keyword,imgset=imgset,soundset=soundset)
   
if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0',port=8000)

#I'm testing out branches!
