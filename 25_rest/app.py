from flask import Flask,render_template
import urllib, json
app = Flask(__name__)
url = "https://api.chucknorris.io/jokes/random?category=science"
@app.route("/")
def root():
    u = urllib.request.urlopen("http://numbersapi.com/random/math")
    response = u.read()
    print(response)


    return render_template('space.html',
                            explanation = response)







if __name__ == "__main__" :
    app.debug = True
    app.run()
