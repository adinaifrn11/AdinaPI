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
    


if __name__ == '__main__':
    app.run()