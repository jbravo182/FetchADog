import importlib
from flask import request, render_template
from webApp import app, apiFunction, routes

print(apiFunction.getDog())

@app.route("/", methods=['GET'])
def baseIndex():

    dogs = apiFunction.getDog()
    url = dogs[0]["message"]
    return render_template("indexPage.html", dogUrl=url)

@app.route("/", methods=['GET', 'POST'], endpoint='getNewDog')
def getNewDog():

    if request.form.get('Get New Dog') == "Get new Dog":
        importlib.reload()
        newDog = apiFunction.getDog()
        dogurl = newDog[0]["message"]


        return render_template("indexPage.html", dogUrl=dogurl)
    return baseIndex()
