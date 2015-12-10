import soundcloud
import flickrapi

from flask import Flask, redirect, render_template, request, url_for
import utils

app = Flask(__name__)

#Home Page, will send keyword to result page when user submits
@app.route("/",methods=["GET","POST"])
def home():
    if request.method == "GET":
        return render_template("home.html")
    else:
        keyword = request.form['keyword']
        return redirect(url_for('result',keyword=keyword))

#Using keyword from home page, will retrive images, sounds from utils and display 
#Submit acts as a "back" button, sending user backhome
@app.route("/result/<keyword>",methods=["GET","POST"])
def result(keyword="default"):
    if request.method == "GET":
        imgset = utils.getImgSet(keyword)
        soundset = utils.getSoundSet(keyword)
        return render_template("result.html",keyword=keyword,imgset=imgset,soundset=soundset)
    else:
        return redirect(url_for('home'))
          
if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0',port=8000)

