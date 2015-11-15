import urllib2,json
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/w")
@app.route("/w/<word>")
def w(word="test"):
    key="a2a73e7b926c924fad7001ca3111acd55af2ffabf50eb4ae5"
    url="http://api.wordnik.com:80/v4/word.json/%s/etymologies?useCanonical=true&api_key=%s"
    url = url%(word,key)
    request = urllib2.urlopen(url)
    result = request.read()
    r = json.loads(result)

    return render_template("etymology.html",link = url)

if __name__=="__main__":
    app.debug = True
    app.run(host='0.0.0.0',port=8000)
