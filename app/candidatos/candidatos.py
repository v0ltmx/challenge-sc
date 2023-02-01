from flask import Blueprint, render_template, request
from app.model.model import Candidatos, Vingadores, Equipe
from app import db

candidatos_blueprint = Blueprint('candidatos', __name__, template_folder='templates')

@candidatos_blueprint.route("/candidatos/", methods=['GET', 'POST'])
def candidatos():
    msg = ''
    if request.method == 'POST':
        all_heros = request.form.getlist('mycheckbox')
        select = request.form.get('check')
        for heros in all_heros:
            info = heros.split('~')
            n_hero = info[0]
            i_hero = info[1]
            if select == 'vingadores':
                hero = Vingadores(n_hero,i_hero)
                db.session.add(hero)
                db.session.commit()
                msg = 'Enviado para os Vingadores'
                candidate = Candidatos.query.filter_by(nome=n_hero).first()
                if candidate:
                    db.session.delete(candidate)
                    db.session.commit()
            if select == 'equipe':
                hero = Equipe(n_hero, i_hero)
                db.session.add(hero)
                msg = 'Enviados para a Equipe'
                candidate = Candidatos.query.filter_by(nome=n_hero).first()
                if candidate:
                    db.session.delete(candidate)
                    db.session.commit()
    all_results = Candidatos.query.all()
    return render_template("candidatos.html", all_results=all_results, mensagem=msg)


@candidatos_blueprint.route("/candidatos/vingadores", methods=['GET', 'POST'])
def vingadores():
    msg = ''
    list_heros = request.form.getlist('mycheckbox')
    if request.method == 'POST':
        for heros in list_heros:
            vingador = Vingadores.query.filter_by(nome=heros).first()
            db.session.delete(vingador)
            db.session.commit()
            msg = 'Operação realizada'
    all_results = Vingadores.query.all()
    return render_template("vingadores.html", all_results=all_results, mensagem=msg)


@candidatos_blueprint.route("/candidatos/equipe", methods=['GET', 'POST'])
def equipe():
    msg = ''
    list_heros = request.form.getlist('mycheckbox')
    if request.method == 'POST':
        for heros in list_heros:
            hero = Equipe.query.filter_by(nome=heros).first()
            db.session.delete(hero)
            db.session.commit()
            msg = 'Operação realizada'
    all_results = Equipe.query.all()
    return render_template("equipe.html", all_results=all_results, mensagem=msg)