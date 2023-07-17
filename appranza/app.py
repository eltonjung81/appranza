from flask import Flask, render_template, request, redirect, url_for
from flask_login import login_required
from flask import Flask, render_template, url_for, send_from_directory

app = Flask(__name__, static_url_path='/imagens', static_folder='imagens')

@app.route('/css/<path:filename>')
def serve_css(filename):
    return send_from_directory('css', filename)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastro')
def Cadastro():
    return render_template('cadastro.html')

@app.route('/entrar', methods=['GET'])
def entrar():
    return redirect(url_for('choose_goal'))

@app.route('/choose_goal', methods=['GET'])
@login_required
def choose_goal():
    return render_template('choose_goal.html')

@app.route('/register', methods=['POST'])
def register():
    username = request.form.get('username')
    password = request.form.get('password')
    name = request.form.get('name')
    phone = request.form.get('phone')
    cpf = request.form.get('cpf')
    height = float(request.form.get('height'))
    weight = float(request.form.get('weight'))

    # Lógica para cadastrar o usuário com os dados fornecidos
    # Você pode armazenar os dados em um banco de dados, por exemplo

    # Renderiza o template result.html passando os dados do cadastro como argumentos
    return render_template('result.html', username=username, password=password, name=name, phone=phone, cpf=cpf, height=height, weight=weight)

@app.route('/calculate', methods=['POST'])
def calculate():
    goal = request.form.get('goal')
    bio_type = request.form.get('bio_type')
    num_meals = int(request.form.get('num_meals'))

    # Lógica para calcular calorias diárias, dividir em refeições, recomendar alimentos, etc.

    result = 'Resultado dos cálculos'
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)

