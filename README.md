<h2><a href= "https://www.mackenzie.br">Universidade Presbiteriana Mackenzie</a></h2>
<h3><a href= "https://www.mackenzie.br/graduacao/sao-paulo-higienopolis/sistemas-de-informacao">Ciencia da Computação</a></h3>

<font size="+1"><center>
## Projeto linhas aereas
</center></font>

# Autores

* Matteo Domiciano Varnier
* Andre Akio Morita Osakawa
* Rafael de Souza Oliveira Cerqueira Tinoco

# Descricao do Projeto:

Observamos que os aeroportos frequentemente não fornecem uma lista completa de todos os destinos disponíveis diretamente em seus sites. Isso significa que, muitas vezes, é necessário pesquisar individualmente em cada companhia aérea para descobrir se é possível voar de um aeroporto para outro.

Para facilitar a busca e planejamento de viagens, decidimos desenvolver uma ferramenta que permita identificar de forma mais eficiente quais aeroportos podem ser alcançados a partir de um determinado ponto de partida. Além disso, a ferramenta vai ajudar a determinar quais aeroportos precisam ser incluídos em uma conexão para atingir um destino desejado, caso o aeroporto inicial não ofereça voos diretos para o destino final.

Com essa abordagem, você poderá rapidamente encontrar rotas diretas e conexões necessárias, simplificando o planejamento de suas viagens.

# Ambientes e Pacotes Utilizados
 Durante o projeto foram utilizados os seguintes softwares:
 - Visual Studio Code (ultima atualizacao)
 - Extensao para Python dentro do Visual Studio Code
 - Python 3.12
 - Arquivos de texto para salvar as informaçoes dos grafos

# Modelagem dos grafos

A modelagem das linhas aéreas do país como grafo tem como objetivo transformar os aeroportos e
rotas em um modelo que facilite as buscas e análises de rotas.
Os aeroportos escolhidos foram baseados nos 20 mais visitados do país e o restante foram pegos,
por ordem alfabética, aeroportos menores de cidades menores, para mostrar as melhores rotas que
pessoas que moram nesses lugares mais isolados devem pegar para viajar, totalizando 50
aeroportos.

Para a modelagem foi construído um grafo não orientado com peso nas arestas utilizando o
aplicativo graphonline.com, que foi mostrado durante aula para a turma, seguindo as seguintes
representações:

- Vértice: Na modelagem do grafo, cada aeroporto é um vértice, identificado por seu nome.

- Arestas: No grafo, cada aresta é uma rota de um aeroporto para o outro, com peso nelas
representando a distância entre cada aeroporto.

# Imagens do Grafico
![alt](/assets/Grafos.png)
**Esta no formato do territorio brasileiro**

![alt](/assets/image.png)
**Esta em um escopo reduzido para melhor visualização**

Link para o grafo: https://graphonline.top/en/?graph=oxVCifgSuTfFjTzr


# Como compilar o codigo

1.  Certifique que o Python esta instalado na maquina e esta inserido nas variaveis de ambiente.

2. Instale o Visual Code

3. Apos a instalacao do Vscode, instale a extensao para python da propria Microsoft

4. Abra nosso codigo no Visual Code e procura pelo arquivo Teste_matriz.py. Clique nele para que abri-lo

5. Apos abrir o arquivo, tera um botao de play no canto direito superior. Ao clicar nesse botao ele ira rodar o codigo

6. Apos iniciar o programa, voce ira digitar 1 que fara com que carregue o arquivo de leitura, que é o arquivo que esta todas as informacoes do grafo

7. Apos carregar o arquivo de entrada, digite 2 para inserir o arquivo de gravacao.

8. Apos carregar os dois arquivos, o usuario esta livre para testar o codigo.



