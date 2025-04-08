#Matteo Domiciano Varnier
#Andre Akio Morita Osakawa
#Rafael de Souza Oliveira Cerqueira Tinoco

import sys
from Grafos_Matriz import TGrafoND  # type: ignore

g = TGrafoND()

def menu():
    while True:
        print("\n--- Menu de Opções ---")
        print("1. Ler dados do arquivo de entrada")
        print("2. Gravar dados no arquivo de saída")
        print("3. Inserir vértice")
        print("4. Inserir aresta")
        print("5. Remover vértice")
        print("6. Remover aresta")
        print("7. Mostrar conteúdo do arquivo")
        print("8. Mostrar grafo")
        print("9. Verificar conexividade do grafo")
        print("10. Coloracao")
        print("11. Dijkstra")
        print("12. Caminho Euleriano")
        print("13. Caminho Hamiltoniano")
        print("14. Encerrar a aplicação")
        print("-----------------------")
        opcao = input("Escolha uma opção: ")
        print("\n")

        if opcao == '1':
            arquivo = input("Digite o nome do arquivo de entrada: ")
            if not arquivo:
                print("Nenhum nome de arquivo foi digitado.")
                continue
            g = TGrafoND(0)
            g.carregarDoArquivo(arquivo)
            print("Agora carregue o arquivo de saida, que ira salvar o grafo")

        elif opcao == '2':
            if g:
                nome_arquivo_saida = input("Carregue o arquivo de saida: ")
                if not nome_arquivo_saida:
                    print("Nenhum nome de arquivo foi digitado.")
                    continue
                g.salvarEmArquivo(nome_arquivo_saida)
            else:
                print("Não há grafo para salvar.")

        elif opcao == '3':
            if g:
                nome = input("Nome do aeroporto desejado: ")
                if not nome:
                    print("Nenhum nome de aeroporto foi digitado.")
                    continue
                nome_normalizado = {nome.lower(): nome for nome in g.nome_para_indice}
                if nome.lower() in nome_normalizado:
                    print(f"Aeroporto {nome} já existe.")
                else:
                    g.insereV(nome)
                    g.salvarEmArquivo(nome_arquivo_saida)
                    print(f"{nome} Adicionado")
            else:
                print("Não há grafo para adicionar vértice.")

        elif opcao == '4':
            if g:
                print("Nomes dos aeroportos das arestas e valor do peso:")
                nome_aeroporto_1 = input("Nome do aeroporto 1: ")
                if not nome_aeroporto_1:
                    print("Nenhum nome de aeroporto foi digitado.")
                    continue
                nome_aeroporto_2 = input("Nome do aeroporto 2: ")
                if not nome_aeroporto_2:
                    print("Nenhum nome de aeroporto foi digitado.")
                    continue
                peso_inserir = input("Peso da aresta: ")
                if not peso_inserir:
                    print("Nenhum peso foi digitado.")
                    continue
                peso_inserir = int(peso_inserir)

                # Normaliza os nomes para comparação insensível a maiúsculas/minúsculas
                nome_normalizado = {nome.lower(): indice for nome, indice in g.nome_para_indice.items()}

                if nome_aeroporto_1.lower() not in nome_normalizado:
                    print(f"Aeroporto {nome_aeroporto_1} não encontrado.")
                    continue

                if nome_aeroporto_2.lower() not in nome_normalizado:
                    print(f"Aeroporto {nome_aeroporto_2} não encontrado.")
                    continue

                valor_1 = nome_normalizado[nome_aeroporto_1.lower()]
                valor_2 = nome_normalizado[nome_aeroporto_2.lower()]

                g.insereA(valor_1, valor_2, peso_inserir)
                g.salvarEmArquivo(nome_arquivo_saida)
                print("Aresta adicionada com sucesso")
            else:
                print("Não há grafo para adicionar aresta.")

        elif opcao == '5':
            nome_aeroporto_1 = input("Nome do aeroporto: ")
            if not nome_aeroporto_1:
                print("Nenhum nome de aeroporto foi digitado.")
                continue

            nome_normalizado = {nome.lower(): indice for nome, indice in g.nome_para_indice.items()}

            if nome_aeroporto_1.lower() not in nome_normalizado:
                print(f"Aeroporto {nome_aeroporto_1} não encontrado.")
                continue

            valor_1 = nome_normalizado[nome_aeroporto_1.lower()]

            g.removeV(valor_1)
            g.salvarEmArquivo(nome_arquivo_saida)
            print("Vértice removido com sucesso")

        elif opcao == '6':
            if g:
                nome_aeroporto_1 = input("Nome do aeroporto 1: ")
                if not nome_aeroporto_1:
                    print("Nenhum nome de aeroporto foi digitado.")
                    continue
                nome_aeroporto_2 = input("Nome do aeroporto 2: ")
                if not nome_aeroporto_2:
                    print("Nenhum nome de aeroporto foi digitado.")
                    continue

                nome_normalizado = {nome.lower(): indice for nome, indice in g.nome_para_indice.items()}

                if nome_aeroporto_1.lower() not in nome_normalizado:
                    print(f"Aeroporto {nome_aeroporto_1} não encontrado.")
                    continue

                if nome_aeroporto_2.lower() not in nome_normalizado:
                    print(f"Aeroporto {nome_aeroporto_2} não encontrado.")
                    continue

                valor_1 = nome_normalizado[nome_aeroporto_1.lower()]
                valor_2 = nome_normalizado[nome_aeroporto_2.lower()]

                g.removeA(valor_1, valor_2)
                g.salvarEmArquivo(nome_arquivo_saida)
                print("Aresta removida com sucesso")

            else:
                print("Não há grafo para remover aresta.")

        elif opcao == '7':
            if g:
                print("Conteúdo do arquivo:")
                g.show(nome_arquivo_saida)
            else:
                print("Arquivo não existe.")

        elif opcao == '8':
            if g:
                print("Grafo:")
                g.mostrarGrafo()
            else:
                print("Grafo não existe.")

        elif opcao == '9':
            if g.isConexo():
                print("Grafo conexo\n")
            else:
                print("Grafo não conexo\n")

        elif opcao == '10':
            g.coloracao()

        elif opcao == '11':
            g.mostrarCaminhoMinimo()

        elif opcao == '12':
            tem_caminho_euleriano, vertices_impares = g.temCaminhoEuleriano()
            if tem_caminho_euleriano:
                print("O grafo tem um caminho euleriano.")
                print(f"Vértices com grau ímpar: {vertices_impares}")
            else:
                print("O grafo não tem um caminho euleriano.")

        elif opcao == '13':
            tem_caminho_hamiltoniano, caminho_hamiltoniano = g.temCaminhoHamiltoniano()
            if tem_caminho_hamiltoniano:
                print("O grafo tem um caminho hamiltoniano.")
            else:
                print("O grafo não tem um caminho hamiltoniano.")

        elif opcao == '14':
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()