def criar_grafo():
    print("\n--- CONFIGURAÇÃO DO GRAFO ---")
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


def inserir_vertice(grafo, vertice):
    if vertice not in grafo:
        grafo[vertice] = []
        print(f"Vertice '{vertice}' foi inserido.")
    else:
        print(f"O vertice '{vertice}' ja existe.")


def inserir_aresta(grafo, origem, destino, nao_direcionado=False):
    if origem not in grafo or destino not in grafo:
        print(f"❌ Erro: Não é possível inserir a aresta. O(s) vértice(s) '{origem}' e/ou '{destino}' não existem.")
        return 
    
    if destino not in grafo[origem]:
        grafo[origem].append(destino)

    if nao_direcionado:
        if origem not in grafo[destino]:
            grafo[destino].append(origem)
    print(f"Aresta entre '{origem}' e '{destino}' foi adicionado!")


def vizinhos(grafo, vertice):
    if vertice in grafo:
        return grafo[vertice]
    return []


def listar_vizinhos(grafo, vertice):
    if vertice in grafo:
        lista = vizinhos(grafo, vertice)
        print(f"Vizinhos do vertice '{vertice}': {lista}")
        return lista
    else:
        print(f"O vertice '{vertice}' nao existe.")
        return []


def exibir_grafo(grafo):
    if not grafo:
        print("O GRAFO ESTÁ VAZIO!!.")
        return
    for v, lista_vizinhos in grafo.items():
        print(f"Vertice {v} --> {vizinhos(grafo, v)}")


def remover_aresta(grafo, origem, destino, nao_direcionado=True):
    removido = False
    if origem in grafo and destino in grafo[origem]:
        grafo[origem].remove(destino)
        removido = True

    if nao_direcionado:
        if destino in grafo and origem in grafo[destino]:
            grafo[destino].remove(origem)
            removido = True

    if removido:
        print(f"A aresta entre '{origem}' e '{destino}' foi removida!")
    else:
        print(f"A aresta entre '{origem}' e '{destino}' não existe.")


def existe_aresta(grafo, origem, destino):
    if origem in grafo and destino in grafo[origem]:
        return True
    return False


def remover_vertice(grafo, vertice):
    if vertice in grafo:
        for outro in list(grafo.keys()):
            if vertice in grafo[outro]:
                grafo[outro].remove(vertice)
        del grafo[vertice]
        print(f"Vertice '{vertice}' foi removido.")
    else:
        print(f"O vertice '{vertice}' nao existe no grafo.")


def grau_vertices(grafo):
    graus = {}
    for v in grafo:
        graus[v] = {'out': len(grafo[v]), 'in': 0, 'total': 0}
        
    for u in grafo:
        for v in grafo[u]:
            if v in graus:
                graus[v]['in'] += 1

    for v in graus:
        graus[v]['total'] = graus[v]['out'] + graus[v]['in']
        
    return graus

def percurso_valido(grafo, caminho):
    if len(caminho) < 2:
        print(f"O percurso {caminho} é válido (trivial).")
        return True
        
    for i in range(len(caminho) - 1):
        origem = caminho[i]
        destino = caminho[i + 1]
        if not existe_aresta(grafo, origem, destino):
            print(f"O percurso {caminho} não é possível (falha com os vértices '{origem}' e '{destino}').")
            return False
            
    print(f"O percurso {caminho} é possível.")
    return True


def main():
    grafo, eh_direcionado = criar_grafo()

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
            op = int(input("Escolha: ").strip())
        except ValueError:
            print("Opcao invalida. Por favor, insira um numero inteiro.")
            continue

        match op:
            case 0:
                print("SAINDO...")
                break
            case 1:
                v = input("Insira um VERTICE: ").strip()
                inserir_vertice(grafo, v)
            case 2:
                u = input("Insira o 1º ARESTA: ").strip()
                v = input("Insira o 2º ARESTA: ").strip()
                inserir_aresta(grafo, u,v, nao_direcionado=not eh_direcionado)
            case 3:
                v = input("Digite o nome do vertice para ser removido: ").strip()
                remover_vertice(grafo, v)
            case 4:
                u = input("Insira o 1° vertice da aresta a remover: ").strip()
                v = input("Insira o 2° vertice da aresta a remover:").strip()
                remover_aresta(grafo, u, v, nao_direcionado=not eh_direcionado)
            case 5:
                graus = grau_vertices(grafo)
                print("\n--- GRAU DOS VÉRTICES ---")
                for v, g in graus.items():
                    print(f"Vértice '{v}' -> Entrada: {g['in']} | Saída: {g['out']} | Total: {g['total']}")
            case 6:
                u = input("Digite o 1° vertice: ").strip()
                v = input("Digite o 2° vertice: ").strip()
                if existe_aresta(grafo, u, v):
                    print("A aresta em questão EXISTE!")
                else:
                    print("A aresta em questão NÃO EXISTE!")
            case 7:
                u = input("Digite o vertice para listar os vizinhos: ").strip()
                listar_vizinhos(grafo, u)
            case 8:
                entrada = input("Digite o percurso, separado por virgulas (A,B,C etc): ").strip()
                percurso = [x.strip() for x in entrada.split(",")]
                percurso_valido(grafo, percurso)
            case 9:
                exibir_grafo(grafo)
            case _:
                print("OPÇÃO INCORRETA. TENTE NOVAMENTE!!")

if __name__ == "__main__":
    main()