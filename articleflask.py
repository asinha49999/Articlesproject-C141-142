from flask import Flask, jsonify, request
from Articles import get_titles
from Articles import most_often
app = Flask(__name__)


@app.route("/")
def fun():
    return jsonify({
        "data": "hello"
    })

@app.route("/articles")
def fun2():
    an = request.args.get("article_name")  #key for param
    numan = int(an)
    data = get_titles(numan)
    return jsonify({
        "data": data
    })
@app.route("/famousarticles")
def fun3():
    re = most_often()
    return jsonify({
       "data": re 
    })


if (__name__ == "__main__"):
    app.run(debug=True)