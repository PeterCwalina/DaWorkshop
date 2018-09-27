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
    print(request)
    print(request.args)
    print(request.headers)
    print(request.method)
    print(request.form)
    if request.args['username'] == '3l1t3 H4X0r':
        greet = 'Greetings Master'
    else:
        greet = 'Greetings pleb'
    return render_template('greet.html',
                           user = request.args['username'],
                           requestM = request.method,
                           greeting = greet
                           )
    
    
if __name__ == "__main__" :
    app.debug = True
    app.run()
