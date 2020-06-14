# movie-recommender-system
...

- O sistema de recomendação implementado se baseia na seguinte teoria:

A recomendação é baseada em similaridade de avaliações entre usuários. Selecionamos o usuário e capturamos os filmes em que ele avaliou de forma excelente. Com esse filmes, capturamos usuários que também avaliaram esse filme, e indicamos ao usuário que queremos fazer a recomendação, os filmes mais bem avaliados por esses usuários.


- Para executar o sistema:

Caso não exista o arquivo dado_grafo.pkl, deve-se executar o arquivo leitura.py, para gerar um novo grafo serializado.
Para realizar a recomendação, execute o arquivo app.py, em linha de console, insira o id do usuario.
Será retornada uma lista com os filmes recomendados para o mesmo.

Caso queira saber quais os filmes o usuário avaliou de forma positiva, crie uma variavel em que armazene nela a execução do metodo filmesBemAvaliadosPorUsuario(grafo, idUser), inserindo como parametro os grafo e o id do usuário. Utilize a função print para imprimir os nomes dos filmes que o usuário avaliou de forma positiva.
