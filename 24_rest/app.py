from flask import Flask,render_template
import urllib, json
app = Flask(__name__)
url = "https://api.nasa.gov/planetary/apod?api_key=nk5cjMiWmZd6wjtn16QvbO1R4xs1sC1h1t4A7gJd&date=2017-02-02"
@app.route("/")
def root():
    u = urllib.request.urlopen(url)
    response = u.read()
    #print(response)
    data = json.loads(response)
    print(data)

    return render_template('space.html',
                            pic = data['url'],
                            explanation = data['explanation'])





if __name__ == "__main__" :
    app.debug = True
    app.run()
