from flask import Flask, render_template
app = Flask(__name__)
coll = [0,1,1,2,3,5,8]
@app.route("/")
def home():
    return render_template(
        'lists.html',
        foo = "foooo",
        collection = coll
        )
                               
                
app.debug = True
app.run()
