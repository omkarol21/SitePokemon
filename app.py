from flask import Flask, render_template, request, redirect

#--- REQUIREMENTS ---
#Informa para o servidor o que é necessário para que o site funcione, ou seja, as bibliotecas

#Armazena os Pokemons que serão cadastrados
lista = []

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('Home.html', Titulo='Bem-vindo ao site Pokémon')

@app.route('/pokemon')
def pokemon():
    return render_template('Pokemon.html', Banana='Melhores Pokémons')

@app.route('/sobre')
def sobre():
    return render_template('Sobre.html', Banana2='Sobre o nosso site')

@app.route('/cadastro')
def cadastro():
    return render_template('Cadastro.html', Titulo='Cadastro de Pokémon')

@app.route('/exibir')
def exibir():
    return render_template('Exibir.html', Titulo='Pokémons Cadastrados', lista=lista)

@app.route('/criar', methods=['POST'])
def criar():
    numero = request.form['numero']
    nome = request.form['nome']
    tipo = request.form['tipo']
    altura = request.form['altura']
    peso = request.form['peso']
    pokemon = [numero, nome, tipo, altura, peso]
    lista.append(pokemon)
    return redirect('/exibir')



if __name__ == '__main__':
    app.run()
