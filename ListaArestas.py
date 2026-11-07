def criar_grafo():
    print("--- CONFIGURAÇÃO DO LISTA DE ADJACÊNCIA ---")
    print("[1] GRAFO NÃO DIRECIONADO")
    print("[2] GRAFO DIRECIONADO")
    opcao = input("Escolha o tipo de grafo: ").strip()
    
    if opcao == '2':
        direcionado = True
        print("\n✅ GRAFO DIRECIONADO CRIADO COM SUCESSO!!")
    else:
        direcionado = False
        print("\n✅ GRAFO NÃO DIRECIONADO CRIADO COM SUCESSO!!")
        
    return {}, direcionado

grafo, eh_direcionado = criar_grafo()

def inserir_vertice(v):
    if v in grafo:
        print(f"\nO vértice {v} adicionado já EXISTE!")
        return
    grafo[v] = []
    print(f"\nVértice {v} foi ADICIONADO!")

def remover_vertice(v):
    if v not in grafo:
        print(f"\nO vértice {v} NÃO EXISTE.")
        return
    del grafo[v]

    for u in grafo:
        if v in grafo[u]:
            grafo[u].remove(v)
    print(f"\nVértice {v} foi REMOVIDO!")

def inserir_aresta(u, v):
    if u not in grafo:
        inserir_vertice(u)
    if v not in grafo:
        inserir_vertice(v)

    if v in grafo[u]:
        print(f"\nA aresta entre '{u}' e '{v}' já EXISTE!")
    else:
        grafo[u].append(v)
        if not eh_direcionado:
            grafo[v].append(u)
        print(f"\nA aresta entre '{u}' e '{v}' foi ADICIONADA!")


def remover_aresta(u, v):
    removido = False
    if u in grafo and v in grafo[u]:
        grafo[u].remove(v)
        removido = True

    if not eh_direcionado and v in grafo and u in grafo[v]:
        grafo[u].remove(v)
        removido = True

    if removido:
        print(f"\nA aresta entre '{u}' e '{v}' foi REMOVIDA!")
    else:
        print(f"\nA aresta entre '{u}' e '{v}' NÃO EXISTE.")


def calcular_grau(v):
    if v not in grafo:
        print(f"\nO vértice '{v}' NÃO EXISTE.")
        return 0
    
    if eh_direcionado:
        grau_saida = len(grafo[v])
        grau_entrada = sum(1 for u in grafo if v in grafo[u])
        print(f"O grau de saída do vértice '{v}' é {grau_saida}")
        print(f"\nO grau de entrada do vértice '{v}' é {grau_entrada}")
        print(f"\nO grau de entrada do vértice '{v}' é {grau_saida + grau_entrada}")
        return grau_entrada + grau_saida
    else:
        grau = len(grafo[v])
        print(f"\nO grau total do vértice '{v}' é {grau}")
        return grau

def verificar_aresta(u, v):
    existe = (u in grafo and v in grafo[u]) or (not eh_direcionado and v in grafo and u in grafo[v])
    if existe:
        print(f"\nA aresta entre '{u}' e '{v}' EXISTE!")
        return True
    print(f"\nA aresta entre '{u}' e '{v}' NÃO EXISTE!")
    return False

def listar_vizinho(v):
    if v not in grafo:
        print(f"\nO vértice '{v}' NÃO EXISTE.")
        return
    vizinhos = grafo[v]
    print(f"\nVizinhos do vértice '{v}': {vizinhos}")


def verificar_percurso(percurso):
    for i in range(len(percurso) - 1):
        u = percurso[i]
        v = percurso[i + 1]
        if u not in grafo or v not in grafo:
            print(f"\nO percurso {percurso} não é possível (vértice inexistente).")
            return False
        if not (v in grafo[u] or (not eh_direcionado and u in grafo[v])):
            print(f"\nO percurso {percurso} não é possível (falha entre '{u}' e '{v}').")
            return False
    print(f"\nO percurso {percurso} é POSSÍVEL.")
    return True

def exibir_grafo():
    if not grafo:
        print("\nO grafo está VAZIO.")
        return
    print("\n--- LISTA DE ADJACÊNCIA ---")
    for v, vizinhos in grafo.items():
        print(f"{v}: {vizinhos}")


def main():
    while True:
        print("""
            -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
            [1] - Inserir Vertice
            [2] - Inserir Aresta
            [3] - Remover Vertice
            [4] - Remover Aresta
            [5] - Calcular Grau
            [6] - Verificar Aresta
            [7] - Verificar Vizinhos
            [8] - Verificar Percurso
            [9] - Exibir Grafo
            [0] - Sair
            -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
            """)

        try:
            escolha = int(input("Escolha: "))
        except ValueError:
            print("Opcao invalida. Por favor, insira um numero inteiro.")
            continue

        if escolha == 1:
            v = input("Digite o nome do vértice a ser inserido: ")
            inserir_vertice(v)
        elif escolha == 2:
            u = input("Digite o primeiro vértice: ")
            v = input("Digite o segundo vértice: ")
            inserir_aresta(u, v)
        elif escolha == 3:
            v = input("Digite o nome do vértice a ser removido: ")
            remover_vertice(v)
        elif escolha == 4:
            u = input("Digite o primeiro vértice: ")
            v = input("Digite o segundo vértice: ")
            remover_aresta(u, v)
        elif escolha == 5:
            v = input("Digite o nome do vértice para calcular o grau: ")
            calcular_grau(v)
        elif escolha == 6:
            u = input("Digite o primeiro vértice: ")
            v = input("Digite o segundo vértice: ")
            verificar_aresta(u, v)
        elif escolha == 7:
            u = input("Digite o vértice para listar os vizinhos: ")
            listar_vizinho(u)
        elif escolha == 8:
            entrada = input(
                "Digite o percurso, separado por vírgulas (A,B,C etc): "
            ).strip()
            percurso = [x.strip() for x in entrada.split(",")]
            verificar_percurso(percurso)
        elif escolha == 9:
            exibir_grafo()
        elif escolha == 0:
            print("SAINDO DO PROGRAMA...")
            break
        else:
            print("OPÇÃO INVÁLIDA! TENTE NOVAMENTE.")

if __name__ == "__main__":
    main()