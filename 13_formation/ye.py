from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def nothing():
    print(app)
    print(request.headers)
    return render_template('yes.html')

@app.route("/auth")
def authenticate():
    print(app)
    #print(request)
    print(request.args)
    print(request.headers)
    print(request.method)
    print(request.form)
    return request.args['username']
    
    

app.debug = True
app.run()
