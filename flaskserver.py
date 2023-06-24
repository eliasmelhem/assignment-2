import flask
from flask import Flask, render_template
app = flask.Flask(__name__)
@app.route('/')
def home():
   return render_template("index.html")
@app.route('/main.html')
def f1():
   return render_template("main.html")
@app.route('/page1.html')
def f2():
   return render_template("page1.html")
@app.route('/page3.html')
def f3():
   return render_template("page2.html")
if __name__ == '__main__':
   app.run(port=8888)