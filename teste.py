import urllib.request, json #requisição da api e leitura(conversão) para json

url = "http://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=3a3e0df066e2569710e9564721db87a8"

response = urllib.request.urlopen(url)

data = response.read() #leitura dos dados

jsonData = json.loads(data) #conversão para json

print(jsonData['results']) #os dados estão dentro dos "results"


