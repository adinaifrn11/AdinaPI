from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'ola mundo!'
@app.route('/contato')

def contato():
    return  '<h1>aaaann@1746</h1>'

@app.route('/exemplo')
def exemplo():
    return render_template ( 'exemplo.html')




if __name__ == '__main__':
    app.run()