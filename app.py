from grafo import Grafo
import csv
import pickle
import random


print('''
        =====================================
                SISTEMA DE RECOMENDAÇÃO
        =====================================

''')

user_id = str(input('Informe o ID do usuário: '))


g = Grafo()

with open('dados_grafo.pkl', 'rb') as dados_grafo:
        dicionario = pickle.load(dados_grafo)





def filmesBemAvaliadosPorUsuario(grafo, userId):
    dicionario_filmes = grafo[str(userId)]

    lista_filmes = []
    for filme in dicionario_filmes:
        if int(dicionario_filmes[filme]) >= 4:
            lista_filmes.append(filme)

    return lista_filmes


def verificarAdjacentes(grafo, filmes):

    lista_users = []

    for movieName in filmes:
        for vertice in grafo.keys():
            if movieName in grafo[vertice].keys():
                for key in grafo[movieName].keys():
                    if key not in lista_users:
                        lista_users.append(key)
    return lista_users

def recomendar(grafo, user_id):
        recomendacao_final = []
        filmes_para_recomendar = []
        count = 0
        filmes = filmesBemAvaliadosPorUsuario(grafo, user_id)   
        usuarios_similares = verificarAdjacentes(grafo, filmes)

     
        for usuario in usuarios_similares:
                filmes_para_recomendar.append(filmesBemAvaliadosPorUsuario(grafo, usuario))

        
        random.shuffle(filmes_para_recomendar)
        for filmes in filmes_para_recomendar:
                random.shuffle(filmes)
        
        for lista in filmes_para_recomendar:
                for filme in lista:
                        if filme not in filmes and count <= 27:
                                recomendacao_final.append(filme)
                                count += 1

        return recomendacao_final
           

g.grafo = dicionario

recomendacao = recomendar(g.grafo, user_id)
print('\n | Recomendados para você \n')
for filme in recomendacao:
        print(filme)
