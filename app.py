from grafo import Grafo
import csv
import pickle


print('''
        =====================================
                SISTEMA DE RECOMENDAÇÃO
        =====================================

''')

user_id = str(input('Informe o ID do usuário: '))
print('\n | Recomendados para você \n')

g = Grafo()

with open('dados_grafo.pkl', 'rb') as dados_grafo:
        dicionario = pickle.load(dados_grafo)

g.grafo = dicionario

g.recomendar(user_id)