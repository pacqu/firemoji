import soundcloud
import flickrapi

from flask import Flask, redirect, render_template, request, session, utils

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def home():
    if request.method == "GET":
        return render_template("home.html")
    else:
        keyword = request.form['keyword']
        return redirect('/result', keyword=keyword)

@app.route("/result",methods=["GET","POST"])
def result():
    if request.method == "GET":
        return redirect("/")
    else:
        imgset = getPic(keyword)
        img1 = imgset[0]
        img2 = imgset[1]
        img3 = imgset[2]
        img4 = imgset[3]
        widget = getWidget(findTrack(keyword))
        return render_template("result.html", img_1 = img1, img_2 = img2, img_3 = img3, img_4 = img4, tags = keyword, sWidget = widget)
if __name__ == '__main__':
    app.dbug = True
    app.run(host='0.0.0.0',port=8000)

#I'm testing out branches!
