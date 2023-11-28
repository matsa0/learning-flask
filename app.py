from flask import Flask, render_template, request


#criando a aplicação Flask
app = Flask(__name__) 


#criando a rota principal para rodar a aplicação
frutas = []
registros = []

@app.route('/', methods=["GET", "POST"]) #aceita solicitações GET e POST
def main():
    if request.method == "POST": #verifica se a requsição feita é do tipo POST, ou seja, se o usuário submeteu o formulário
        if request.form.get("fruta"): #verifica se há algum dado enviado pelo formulário name
            frutas.append(request.form.get("fruta"))
    return render_template("index.html", frutas=frutas) #o primeiro nome é uma variável


    
'''
   Quando um formulário é submetido por método POST, verifica-se se há dados válidos para "aluno" e "nota" no formulário. 
   Se sim, esses dados são usados para criar um novo dicionário contendo as chaves "aluno" e "nota" e seus respectivos valores. 
   Esse dicionário é então adicionado à lista registros.
'''
#criando outra rota(url) com sobre
@app.route('/sobre', methods=["GET", "POST"]) 
def sobre():
    if request.method == "POST":
        if request.form.get("aluno") and request.form.get("nota"):
            registros.append({"aluno": request.form.get("aluno"), "nota": request.form.get("nota")}) 



    return render_template("sobre.html", registros=registros) 

if __name__ == "__main__":
    app.run(debug=True) #rodar a aplicação com debug=true e invés de utilizar 'flask run', 'pyhton3 app.py'
    