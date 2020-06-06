from grafo import Grafo
import csv
import pickle

grafo = Grafo()

table_movies = {}

with open('datasets/movies.csv', 'r') as csvmovies:
    for line in csvmovies:
        data = line.split(',')
        id_movie = data[0]
        name_movie = data[1]
        table_movies[id_movie] = name_movie.strip()


with open('datasets/ratings.csv', 'r') as csvratings:
    for line in csvratings:
        data = line.split(',')
        user = data[0]
        id_movie = data[1]
        rated_movie = table_movies[id_movie]
        rating = float(data[2])

        grafo.adicionar_vertice(user)
        grafo.adicionar_vertice(rated_movie)
        grafo.adicionar_aresta(user, rated_movie, rating)

dados = grafo.grafo

with open('dados_grafo.pkl', mode='wb') as dados_grafo:
    pickle.dump(dados, dados_grafo)