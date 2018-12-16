import os
import json
import secrets
from flask import render_template, url_for, flash, redirect, session, request, jsonify, make_response
from loggathon import app, db, UPLOAD_FOLDER, ALLOWED_EXTENSIONS
from tinydb import Query
from loggathon.forms import RegistrationForm, LoginForm, SellForm
from datetime import datetime
import pdfkit
from werkzeug.utils import secure_filename


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/mark_store/<store>')
def mark_store(store):

    user = get_user()
    if user:
        sells_data = db.table('sells').search(Query().store == user['email'])
        if len(sells_data) > 0:
            sells_data = {**sells_data[0]}
            sells = sells_data.get('sells')
            for sell in sells:
                sell['status'] = 'Recolhido'
                try:
                    sell['sell_date'] = int(sell['sell_date'])
                except:
                    pass

            db.table('sells').upsert(sells_data, Query().store == user['email'])

    return redirect(url_for('home'))

@app.route('/pdf')
def pdf_template():
    user = get_user()
    rendered = render_template('pdf_template.html', user=user)
    pdf = pdfkit.from_string(rendered, False)
    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline; filename=output.pdf'
    return response


@app.route("/")
@app.route("/home")
def home():
    user = get_user()
    if user:
        sells_data = db.table('sells').search(Query().store == user['email'])
        if len(sells_data) > 0:
            sells_data = {**sells_data[0]}
            sells = sells_data.get('sells')
            for sell in sells:
                try:
                    sell['sell_date'] = datetime.fromtimestamp(sell['sell_date'])
                except:
                    pass
    else:
        sells = None

    return render_template('home.html', user=user, sells=sells)

@app.route("/make_route")
def stores():
    amount = 0
    sells = db.table('sells').all()
    for sell in sells:
        amount += len(sell['sells'])
        user = db.table('users').search(Query().email == sell['store'])[0]
        user.pop('password', None)
        sell['store_info'] = user

    return jsonify({'amount': amount, 'price': 20, 'distance': 5.2, 'eta': 15, 'stores': sells})

@app.route("/post_sell", methods=['GET', 'POST'])
def post_sell():
    form = SellForm()
    user = get_user()
    if request.method == 'POST':
        if form.validate_on_submit():

            file = request.files['image']
            if file and allowed_file(file.filename):
                filename = secrets.token_hex(4) + '_' + secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            if user:
                product = {k: form.data[k] for k in ['title', 'volume', 'weight', ]}
                product['image'] = filename
                product['sell_date'] = int(datetime.now().timestamp())
                product['status'] = 'Não recolhido'
                sells_data = db.table('sells').search(Query().store == user['email'])
                if len(sells_data) > 0:
                    sells_data = {**sells_data[0]}
                    sells_data['sells'].append(product)
                    for sell in sells_data['sells']:
                        try:
                            sell['sell_date'] = sell['sell_date'].timestamp()
                        except:
                            pass

                    db.table('sells').upsert(sells_data, Query().store == user['email'])

                return redirect(url_for('home'))
        else:
            flash('Problema ao submeter venda, tente novamente', 'danger')

    return render_template('post_sell.html', title='Postar Venda', form=form, user=user)


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Conta criada com o usuário {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        users = db.table('users').search(Query().email == form.email.data.lower())
        if len(users) > 0:
            user = dict(users[0])
            if form.password.data == user.get('password'):
                flash('Você entrou com sucesso!', 'success')
                user.pop('password', None)
                session['user'] = json.dumps(user)
                return redirect(url_for('home'))
        else:
            flash('Erro no login. Confira seu email e senha e tente novamente', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    session.pop('user', None)
    return redirect(url_for('home'))


def get_user():
    user = session.get('user', None)
    if user:
        return json.loads(user)

    return None

