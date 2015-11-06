import soundcloud

@app.route("/", methods=['GET'])
def home():
    return render_template("home.html")
