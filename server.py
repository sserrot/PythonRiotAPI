# all the imports
from flask import Flask, request, redirect, url_for, render_template
from cassiopeia import riotapi

# setup

app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

api_key = str(input())
riotapi.set_region("NA")
riotapi.set_api_key(api_key)
globalSummoner = ' '

# Index Initialized


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/display.html", methods=['GET', 'POST'])
def display():
    if request.method == 'POST':
        summoner_name = request.form['summoner_name']
        summoner = riotapi.get_summoner_by_name(summoner_name)
        globalSummoner = "{name} is a level {level} summoner on the NA server.".format(name=summoner.name, level=summoner.level)
        return render_template('display.html', result=globalSummoner)


if __name__ == "__main__":
    app.run()
