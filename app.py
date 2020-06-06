from grafo import Grafo
import csv
import pickle


print('''
        =====================================
                SISTEMA DE RECOMENDAÇÃO
        =====================================
''')

g = Grafo()

with open('dados_grafo.pkl', 'rb') as dados_grafo:
        dicionario = pickle.load(dados_grafo)

g.grafo = dicionario

