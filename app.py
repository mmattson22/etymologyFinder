import urllib2,json
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/answer")
@app.route("/answer/<word>")
def answer(word=""):
    """ 
    gets word that user entered in home page and uses etymology api to 
    display its etymology
    """
    key="a2a73e7b926c924fad7001ca3111acd55af2ffabf50eb4ae5"
    url="http://api.wordnik.com:80/v4/word.json/%s/etymologies?useCanonical=true&api_key=%s"
    url = url%(word,key)
    request = urllib2.urlopen(url)
    result = request.read()
    r = json.loads(result)
    try:
        return render_template("answer.html",word=word, etymology=r[0], error=False)
      
    except:
        return render_template("etymology.html",error=True, word="bad word", etymology="none :(")
if __name__=="__main__":
    app.debug = True
    app.run(host='0.0.0.0',port=8000)
