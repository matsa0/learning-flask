from flask import Flask, render_template #para retornar o template HTML da pasta templates

#setx FLASK_ENV development
#flask run


#criando a aplicação Flask
app = Flask(__name__) 


#criando a rota principal para rodar a aplicação
@app.route('/')
def main():
    nome = "Matheus"
    idade = 20
    return render_template("index.html", nome=nome, idade=idade) #o primeiro nome é uma variável


#criando outra rota(url) com sobre
@app.route('/sobre') 
def sobre():
    return render_template("sobre.html") 

if __name__ == "__main__":
    app.run(debug=True)
    