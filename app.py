from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'ola mundo!'

@app.route('/contato')
def contato():
    return render_template('conato.html', nome = 'adina',email = 'adina@gmail.com')



@app.route('/exemplo')
def exemplo():
    return render_template ( 'exemplo.html')

@app.route('/exemplo2')
def exemplo2():
    return render_template('exemplo2.html')

@app.route('/perfil', defaults={'nome': 'adina'})
@app.route ('/perfil/<nome>')
def perfil (nome):
    return render_template('perfil.html')

@app.route('/semestre/<int:x>')
def semestre(x):
    y = x = 1
    return render_template('semestre.html', x=x, y=y)


@app.route('/login.hml')
def login():
    return render_template('login.html')

    
@app.route('/verificarlogin', methods=['post'])
def verificarlogin():
    login = request.form ['login']
    senha = request.form['senha']
    if login == 'admim' and senha == '12345':
        return 'seja bem vindo admim'
    else:
        return 'voce não tem permissão de acessar essa pagina'
    
@app.route('/verificaridade/<int:idade>')
def verificaridade(idade):
    return render_template("verificar.html", idade=idade)

@app.route('/usuario/<nome>')
def usuario(nome):
    return render_template('usuario.html', nome=nome)	


@app.route('/produtos/<int:qtd')
def produtos (qtd):
    return render_template('produtos.html', qtd=qtd)

@app.rourte('/compras')
def compras():
    items=['arroz','feijão','farinha','macrrao','acucar']
    return render_template("compras.html", items=items)

    
	
if __name__ == '__main__':
    app.run()