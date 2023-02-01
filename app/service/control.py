import json
from app import app
from app.model.model import Candidatos, Herois
from flask import render_template, request
from app import db
import requests
from config import hash, ts, apikey
from app.candidatos.candidatos import candidatos_blueprint


app.register_blueprint(candidatos_blueprint)


##Documentação Marvel: https://developer.marvel.com/
def manage_hero():
    URL = f"https://gateway.marvel.com/v1/public/characters?ts={ts}&apikey={apikey}&hash={hash}&limit=100"
    getreq = requests.get(f"{URL}")
    convert = json.loads(getreq.content)
    resp = convert['data']['results']
    for results in resp:
        hero = Herois(results['name'],results['description'],
        f"{results['thumbnail']['path']}.{results['thumbnail']['extension']}")
        equal = Herois.query.filter_by(nome=results['name']).first()
        if not equal:
            db.session.add(hero)
            db.session.commit()


@app.route("/", methods=['GET', 'POST'])
@app.route("/home/", methods=['GET', 'POST'])
def home():
    manage_hero()
    msg=''
      
    if request.method == 'POST':
            all_heros = request.form.getlist('mycheckbox')
            for candidates in all_heros:
                info = candidates.split('~')
                n_hero = info[0]
                i_hero = info[1]
                exists = Candidatos.query.filter_by(nome=n_hero).first()
                if exists:
                    msg = 'Esse herói já foi cadastrado'
                else:
                    candidate = Candidatos(n_hero, i_hero)
                    db.session.add(candidate)
                    db.session.commit()
                    msg = 'Operação realizada.'
    page = request.args.get('page', 1, type=int)
    all_results = Herois.query.paginate(page=page, per_page=20)
    return render_template("index.html", mensagem=msg, all_results=all_results)



