
#Peter Cwalina
#SoftDev1 pd7
#K08  Fil Yer Flask
#2018-9-18
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    print(__name__)
    return "insert shrek movie script here"

@app.route("/bees")
def bees():
    return "insert bee movie here"

@app.route("/memes")
def memes():
    return "insert memes here"

app.run()
