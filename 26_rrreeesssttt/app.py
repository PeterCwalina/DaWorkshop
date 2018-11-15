from flask import Flask,render_template
import urllib,json
from urllib.request import Request
app = Flask(__name__)

@app.route("/")
def root():
    #dog api shenanigans
    u = urllib.request.urlopen("https://dog.ceo/api/breeds/image/random")
    response = u.read()
    print(response)
    data = json.loads(response)

    #SWAPI shenanigans
    req = Request('https://swapi.co/api/people/1/',headers = {'User-Agent': 'Mozilla/5.0'})
    u = urllib.request.urlopen(req)
    response = u.read()
    data2 = json.loads(response)

    #Chuck norris shenanigans
    req = Request('https://api.chucknorris.io/jokes/random',headers = {'User-Agent': 'Mozilla/5.0'})
    u = urllib.request.urlopen(req)
    response = u.read()
    data3 = json.loads(response)

    return render_template('space.html',
                            pic = data['message'],
                            dict = data2,
                            explanation = data3['value'])







if __name__ == "__main__" :
    app.debug = True
    app.run()
