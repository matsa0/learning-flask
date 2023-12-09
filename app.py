from flask import Flask, render_template, request
import urllib.request, json

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


#rota dinâmica
@app.route('/filmes/<parameter>', methods=["GET", "POST"])
def filmes(parameter):
    if parameter == "popular":
        url = "http://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=3a3e0df066e2569710e9564721db87a8"
    elif parameter == "kids":
        url = "http://api.themoviedb.org/3/discover/movie?certification_country=US&certification.lte=G&sort_by=popularity.desc&api_key=3a3e0df066e2569710e9564721db87a8"
    elif parameter == "2010":
        url = "http://api.themoviedb.org/3/discover/movie?primary_release_year=2010&sort_by=vote_average.desc&api_key=3a3e0df066e2569710e9564721db87a8"
    elif parameter == "drama":
        url = "http://api.themoviedb.org/3/discover/movie?with_genres=18&sort_by=vote_average.desc&vote_count.gte=10&api_key=3a3e0df066e2569710e9564721db87a8"
    elif parameter == "tom_cruise":
        url = "http://api.themoviedb.org/3/discover/movie?with_genres=878&with_cast=500&sort_by=vote_average.desc&api_key=3a3e0df066e2569710e9564721db87a8"
    
    response = urllib.request.urlopen(url) #requisição da api

    data = response.read() #leitura dos dados
    jsonData = json.loads(data) #conversão para json

    return render_template("filmes.html", filmes=jsonData['results'])#os dados estão dentro dos "results"


@app.route('/filmesJson', methods=["GET", "POST"])
def filmesJson():
    url = "http://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=3a3e0df066e2569710e9564721db87a8" #url da api
    response = urllib.request.urlopen(url) #requisição da api

    data = response.read() #leitura dos dados
    jsonData = json.loads(data) #conversão para json

    return jsonData['results']


if __name__ == "__main__":
    app.run(debug=True) #rodar a aplicação com debug=true e invés de utilizar 'flask run', 'pyhton3 app.py'
    
