from flask import Flask
app = Flask(__name__)

@app.route("/")
def nothing():
    return 'public/idontexist.html'

@app.route("/o")
def noting():
    x = 2
    while x > 1:
        x +=1

        
    return 'public/yes.html'



app.run()
app.debug = True
