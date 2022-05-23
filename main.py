from flask import Flask,jsonify,request
import csv 

all_articles =[]
with open('shared_articles.csv') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_articles = data[1:]

like_articles = []
notlike_articles = []

app = Flask(__name__)
@app.route("/get-articles")
def get_articles():
    return jsonify({
        "data": all_articles[0],
        "status": "success"
    })

@app.route("/like-articles",methods=["POST"])
def likearticles():
    articles = all_articles[0]
    all_articles = all_articles[1:]
    like_articles.append(articles)
    return jsonify({
        "status": "success"
    }),201

@app.route("/notlikearticles",methods=["POST"])
def notlikearticles():
    articles = all_articles[0]
    all_articles = all_articles[1:]
    notlike_articles.append(articles)
    return jsonify({
        "status": "success"
    }),201

if __name__ =="__main__":
    app.run()
    