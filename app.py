from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
import locale
from datetime import datetime
from weasyprint import HTML
from flask import Response

app = Flask(__name__)
app.config['SECRET_KEY'] = 'TESTE'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login_page'
login_manager.login_message = "Por favor, faça o login para acessar esta página."

class User(UserMixin):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

users = {
    '1': User(id='1', username='wallace', password='12345'),
    '2': User(id='2', username='teste', password='teste')
}

@login_manager.user_loader
def load_user(user_id):
    return users.get(user_id)
@app.route('/', methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        username = request.form['usuario']
        password = request.form['senha']

        user = next((u for u in users.values() if u.username == username), None)

        if user and user.password == password:
            login_user(user)
            flash('Login realizado com sucesso!', 'success')
            return redirect(url_for('formulario_page'))
        else:
            flash('Usuário ou senha inválidos.', 'danger')

    return render_template('login.html')

@app.route('/formulario')
@login_required
def formulario_page():
    return render_template('formulario.html', nome_prestador=current_user.username.capitalize())

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Você saiu do sistema.', 'info')
    return redirect(url_for('login_page'))

@app.route('/gerar_pdf', methods=['POST'])
@login_required
def gerar_pdf():
    dados = {
        'prestador_nome': request.form.get('prestador_nome'),
        'prestador_cpf': request.form.get('prestador_cpf'),
        'cliente_nome': request.form.get('cliente_nome'),
        'cliente_cnpj_cpf': request.form.get('cliente_cnpj_cpf'),
        'cliente_rua': request.form.get('cliente_rua'),
        'cliente_cep': request.form.get('cliente_cep'),
        'cliente_cidade': request.form.get('cliente_cidade'),
        'cliente_estado': request.form.get('cliente_estado'),
        'valor_total': request.form.get('valor_total'),
        'servicos': [s.strip() for s in request.form.get('servicos').splitlines() if s.strip()],
        'materiais': [m.strip() for m in request.form.get('materiais').splitlines() if m.strip()]
    }

    locale.setlocale(locale.LC_TIME, 'pt_BR.utf-8')
    hoje = datetime.now()
    dados['data_hoje'] = hoje.strftime("%d de %B de %Y")

    html_renderizado = render_template('template_orcamento.html', **dados)

    pdf_bytes = HTML(string=html_renderizado).write_pdf()

    return Response(pdf_bytes,
                    mimetype='application/pdf',
                    headers={'Content-Disposition': 'inline;filename=orcamento.pdf'})

if __name__ == '__main__':
    app.run(debug=True)