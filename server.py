# all the imports
from flask import Flask, request, redirect, url_for, render_template
from cassiopeia import riotapi

# setup

app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

riotapi.set_region("NA")
riotapi.set_api_key("2af3426a-6e8a-4138-8eab-d88c430852c1")
globalSummoner = ''

# Index Initialized


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        summoner_name = request.form['summoner_name']
        summoner = riotapi.get_summoner_by_name(summoner_name)
        print("{name} is a level {level} summoner on the NA server.".format(name=summoner.name, level=summoner.level))
    return render_template('index.html')


# @app.route('/display')
# def summoner_test():
#     if request.method == 'POST':
#         summoner_name = request.form['summoner_name']
#         summoner = riotapi.get_summoner_by_name(summoner_name)
#         print("{name} is a level {level} summoner on the NA server.".format(name=summoner.name, level=summoner.level))
#     return "{name} is a level {level} summoner on the NA server.".format(name=summoner.name, level=summoner.level)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
