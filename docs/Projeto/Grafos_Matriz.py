#Matteo Domiciano Varnier
#Andre Akio Morita Osakawa
#Rafael de Souza Oliveira Cerqueira Tinoco

class TGrafoND:
    TAM_MAX_DEFAULT = 1000

    def __init__(self, n=TAM_MAX_DEFAULT):
        self.n = n
        self.m = 0
        self.adj = [[0.0 for _ in range(n)] for _ in range(n)]
        self.nomes_vertices = [f"V{i}" for i in range(n)]  # Nomes padrão para os vértices
        self.nome_para_indice = {f"V{i}": i for i in range(n)}
        self.indice_para_nome = {i: f"V{i}" for i in range(n)}

    def insereA(self, v, w, peso=1.0):
        if v >= self.n or w >= self.n:
            print("Um ou ambos os vértices não existem.")
            return  # Retorna ao menu
        if self.adj[v][w] == 0.0 and self.adj[w][v] == 0.0:
            self.adj[v][w] = peso
            self.adj[w][v] = peso
            self.m += 1
        else:
            print("Aresta já existe.")

    def insereV(self, nome_vertice):
        if nome_vertice in self.nome_para_indice:
            print(f"Vértice {nome_vertice} já existe.")
            return

        self.n += 1
        self.nomes_vertices.append(nome_vertice)  # Adiciona o nome do novo vértice
        self.nome_para_indice[nome_vertice] = self.n - 1
        self.indice_para_nome[self.n - 1] = nome_vertice
        nova_linha = [0.0] * self.n
        self.adj.append(nova_linha)

        for i in range(self.n - 1):
            self.adj[i].append(0.0)

    def removeA(self, v, w):
        if v >= self.n or w >= self.n:
            print("Um ou ambos os vértices não existem.")
            return  # Retorna ao menu
        if self.adj[v][w] != 0.0 and self.adj[w][v] != 0.0:
            self.adj[v][w] = 0.0
            self.adj[w][v] = 0.0
            self.m -= 1
        else:
            print("Aresta não existe.")

    def removeV(self, v):
        if v >= self.n:
            print("Vértice inválido!")
            return

        # Remover todas as arestas conectadas ao vértice v
        for i in range(self.n):
            if self.adj[v][i] != 0.0:  # Verifica se existe aresta entre v e i
                self.removeA(v, i)  # Remove a aresta v <-> i

        # Remove o vértice da matriz de adjacência
        self.adj.pop(v)  # Remove a linha correspondente ao vértice v
        for i in range(len(self.adj)):
            self.adj[i].pop(v)  # Remove a coluna correspondente ao vértice v

        # Remove o nome do vértice da lista de nomes
        nome_removido = self.nomes_vertices.pop(v)
        self.nome_para_indice.pop(nome_removido)
        self.indice_para_nome.pop(v)

        # Atualiza o número de vértices
        self.n -= 1

        print(f"Vértice {nome_removido} removido com sucesso.")

    def dfs(self, v, visitados):
        visitados[v] = True
        for i in range(self.n):
            if self.adj[v][i] != 0.0 and not visitados[i]:
                self.dfs(i, visitados)

    def isConexo(self):
        visitados = [False] * self.n

        # Encontra um vértice inicial para iniciar a DFS
        start_vertex = -1
        for i in range(self.n):
            if any(self.adj[i][j] != 0.0 for j in range(self.n)):
                start_vertex = i
                break

        # Se não houver vértices com arestas, o grafo é conexo (vazio)
        if start_vertex == -1:
            return True

        # Executa a DFS a partir do vértice inicial
        self.dfs(start_vertex, visitados)

        # Verifica se todos os vértices que têm arestas foram visitados
        for i in range(self.n):
            if any(self.adj[i][j] != 0.0 for j in range(self.n)) and not visitados[i]:
                return False  # Se algum vértice não foi visitado e tem arestas, o grafo é desconexo

        return True  # Se todos os vértices foram visitados, o grafo é conexo

    def show(self, nome_arquivo):
        with open(nome_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                print(linha.strip())

    def mostrarGrafo(self):
        for i in range(self.n):
            # Formate cada linha da matriz como uma string de elementos dentro de colchetes
            linha = [f"{peso:.1f}" if peso != 0.0 else "0.0" for peso in self.adj[i]]
            print(f"Matriz {i}: {linha}")

    def carregarDoArquivo(self, nome_arquivo):
        try:
            with open(nome_arquivo, 'r') as arquivo:
                linhas = arquivo.readlines()
                tipo_grafo = int(linhas[0].strip())
                num_vertices = int(linhas[1].strip())
                self.nomes_vertices = []
                self.nome_para_indice = {}
                self.indice_para_nome = {}
                for i in range(2, 2 + num_vertices):
                    descricao, indice = linhas[i].strip().rsplit(maxsplit=1)
                    self.nomes_vertices.append(descricao)
                    self.nome_para_indice[descricao] = int(indice)
                    self.indice_para_nome[int(indice)] = descricao

                num_arestas_index = 2 + num_vertices
                num_arestas = int(linhas[num_arestas_index].strip())
                self.n = num_vertices
                self.adj = [[0.0 for _ in range(self.n)] for _ in range(self.n)]
                self.m = 0
                for i in range(num_arestas_index + 1, num_arestas_index + 1 + num_arestas):
                    v, w, peso = map(int, linhas[i].strip().split())
                    self.insereA(v, w, peso)
        except FileNotFoundError:
            print(f"Erro: Arquivo '{nome_arquivo}' não foi encontrado.")

    def salvarEmArquivo(self, nome_arquivo):
        with open(nome_arquivo, 'w') as arquivo:
            arquivo.write(f"2\n{self.n}\n")

            # Escreve os vértices e seus índices
            for i in range(self.n):
                arquivo.write(f"{self.nomes_vertices[i]} {i}\n")

            # Conta e escreve o número de arestas
            num_arestas = 0
            for i in range(self.n):
                for j in range(i + 1, self.n):
                    if self.adj[i][j] != 0.0:
                        num_arestas += 1
            arquivo.write(f"{num_arestas}\n")

            # Escreve as arestas com seus pesos
            for i in range(self.n):
                for j in range(i + 1, self.n):
                    if self.adj[i][j] != 0.0:
                        arquivo.write(f"{i} {j} {int(self.adj[i][j])}\n")

    def dijkstra(self, origem):
        # Inicialização
        d1 = [float('inf')] * self.n
        d1[origem] = 0
        S = {origem}
        A = set(range(self.n))
        F = set()
        rot = [None] * self.n
        k = 0

        while A:
            k += 1
            # Encontra o vértice mais próximo da origem
            r = min(A, key=lambda i: d1[i])
            F.add(r)
            A.remove(r)
            S = A.intersection(self.get_sucessores(r))

            for i in S:
                p = min(d1[i], d1[r] + self.adj[r][i])
                if p < d1[i]:
                    d1[i] = p
                    rot[i] = r

        return d1, rot

    def get_sucessores(self, v):
        return {i for i in range(self.n) if self.adj[v][i] != 0.0}

    def mostrarCaminhoMinimo(self):
        # Exibe a lista de aeroportos disponíveis
        print("Aeroportos disponíveis:")
        for nome in self.nomes_vertices:
            print(nome)
        print("\n")
        # Solicita ao usuário o nome do aeroporto de origem
        nome_origem = input("Digite o nome do aeroporto de origem: ").strip().lower()

        # Normaliza os nomes para comparação insensível a maiúsculas/minúsculas
        nome_normalizado = {nome.lower(): indice for nome, indice in self.nome_para_indice.items()}

        if nome_origem not in nome_normalizado:
            print(f"Aeroporto {nome_origem} não encontrado.")
            return

        origem = nome_normalizado[nome_origem]

        # Solicita ao usuário o nome do aeroporto de destino
        nome_destino = input("Digite o nome do aeroporto de destino: ").strip().lower()

        if nome_destino not in nome_normalizado:
            print(f"Aeroporto {nome_destino} não encontrado.")
            return

        destino = nome_normalizado[nome_destino]

        d1, rot = self.dijkstra(origem)

        if d1[destino] == float('inf'):
            print(f"Aeroporto {self.indice_para_nome[destino]} não é alcançável a partir de {self.indice_para_nome[origem]}.")
        else:
            print(f"Distância mínima de {self.indice_para_nome[origem]} para {self.indice_para_nome[destino]}: {d1[destino]} km")
            caminho = []
            j = destino
            while j is not None:
                caminho.append(self.indice_para_nome[j])
                j = rot[j]
            caminho.reverse()
            print(f"Caminho: {caminho}")

    def coloracao(self):
        n = self.n
        C = [None] * n  # Lista de cores dos vértices (None indica não colorido)
        k = 1  # Cor inicial

        # Iterando por cada vértice
        for v in range(n):
            # Tenta encontrar a menor cor que não é usada por nenhum vizinho
            cor_usada = [False] * (k + 1)  # Mantém as cores usadas pelos vizinhos de v

            # Marca as cores usadas pelos vizinhos
            for w in range(n):
                if self.adj[v][w] != 0.0 and C[w] is not None:
                    cor_usada[C[w]] = True

            # Encontra a menor cor não usada
            for cor in range(1, k + 1):
                if not cor_usada[cor]:
                    C[v] = cor
                    break
            else:
                # Se todas as cores até k foram usadas, incrementa k
                k += 1
                C[v] = k

        # Exibir a cor atribuída a cada vértice
        for v in range(n):
            print(f"Vértice {self.indice_para_nome[v]} -> Cor {C[v]}")

        print(f"\nNúmero total de cores usadas: {k}")

    def temCaminhoEuleriano(self):
        if not self.isConexo():
            return False, []

        graus_impares = 0
        vertices_impares = []
        for i in range(self.n):
            grau = sum(self.adj[i])
            if grau % 2 != 0:
                graus_impares += 1
                vertices_impares.append(i)

        if graus_impares == 2:
            return True, vertices_impares
        else:
            return False, []

    def temCaminhoHamiltoniano(self):
        # Função auxiliar para verificar se um caminho é válido
        def caminho_valido(caminho, pos):
            if pos == self.n:
                # Verifica se há uma aresta entre o último e o primeiro vértice
                return self.adj[caminho[pos - 1]][caminho[0]] != 0.0
            for i in range(pos):
                if caminho[i] == caminho[pos]:
                    return False
            return True

        # Função auxiliar para encontrar um caminho hamiltoniano
        def encontrar_caminho_hamiltoniano(caminho, pos):
            if pos == self.n:
                return caminho_valido(caminho, pos)

            for v in range(self.n):
                caminho[pos] = v
                if caminho_valido(caminho, pos):
                    if encontrar_caminho_hamiltoniano(caminho, pos + 1):
                        return True
                caminho[pos] = -1

            return False

        caminho = [-1] * self.n
        caminho[0] = 0  # Começa do vértice 0

        if not encontrar_caminho_hamiltoniano(caminho, 1):
            return False, []

        return True, caminho