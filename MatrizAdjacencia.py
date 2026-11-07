def criar_matriz():
    print("--- CONFIGURAÇÃO DA MATRIZ ---")
    print("[1] MATRIZ Não Direcionado")
    print("[2] MATRIZ Direcionado")
    opcao = input("Escolha o tipo de matriz: ").strip()
    
    if opcao == '2':
        direcionado = True
        print("\n✅ MATRIZ DIRECIONADA CRIADA COM SUCESSO!!")
    else:
        direcionado = False
        print("\n✅ MATRIZ NÃO DIRECIONADA CRIADA COM SUCESSO!!")
    
    return {'vertices': [], 'matriz': [],'direcionado': direcionado}


def inserir_vertice(grafo, v):
    if v in grafo['vertices']:
        print(f"\nO vértice '{v}' já existe!")
        return
    
    grafo['vertices'].append(v)

    for linha in grafo['matriz']:
        linha.append(0)
        
    nova_linha = [0] * len(grafo['vertices'])
    grafo['matriz'].append(nova_linha)
    
    print(f"\nVértice '{v}' foi adicionado!")


def remover_vertice(grafo, v):
    if v not in grafo['vertices']:
        print(f"\nO vértice '{v}' não existe.")
        return
        
    idx = grafo['vertices'].index(v)
    grafo['vertices'].pop(idx)
    grafo['matriz'].pop(idx)
    
    for linha in grafo['matriz']:
        linha.pop(idx)
        
    print(f"\nVértice '{v}' foi removido!")


def inserir_aresta(grafo, u, v):
    if u not in grafo['vertices']:
        inserir_vertice(grafo, u)
    if v not in grafo['vertices']:
        inserir_vertice(grafo, v)

    i = grafo['vertices'].index(u)
    j = grafo['vertices'].index(v)

    grafo['matriz'][i][j] = 1
    
    if not grafo['direcionado']:
        grafo['matriz'][j][i] = 1
        
    print(f"\nA aresta entre '{u}' e '{v}' foi adicionada!")


def remover_aresta(grafo, u, v):
    if u in grafo['vertices'] and v in grafo['vertices']:
        i = grafo['vertices'].index(u)
        j = grafo['vertices'].index(v)
        
        grafo['matriz'][i][j] = 0
        if not grafo['direcionado']:
            grafo['matriz'][j][i] = 0
            
        print(f"\nA aresta entre '{u}' e '{v}' foi removida!")
    else:
        print("\nUm ou ambos os vértices não existem.")


def calcular_grau(grafo, v):
    if v in grafo['vertices']:
        idx = grafo['vertices'].index(v)
        
        if grafo['direcionado']:
            saida = sum(grafo['matriz'][idx])
            entrada = sum(grafo['matriz'][linha][idx] for linha in range(len(grafo['vertices'])))
            print(f"\nO vértice '{v}' tem Grau de Saída: {saida}, Entrada: {entrada} e Total: {saida + entrada}")
            return saida + entrada
        else:
            grau = sum(grafo['matriz'][idx])
            print(f"\nO grau do vértice '{v}' é {grau}")
            return grau
    else:
        print(f"\nO vértice '{v}' não existe.")
        return 0


def verificar_aresta(grafo, u, v):
    if u in grafo['vertices'] and v in grafo['vertices']:
        i = grafo['vertices'].index(u)
        j = grafo['vertices'].index(v)
        if grafo['matriz'][i][j] == 1:
            print("\nA aresta em questão EXISTE!")
            return True
    print("\nA aresta em questão NÃO EXISTE!")
    return False


def listar_vizinho(grafo, v):
    if v in grafo['vertices']:
        idx = grafo['vertices'].index(v)
        vizinhos = [grafo['vertices'][j] for j in range(len(grafo['vertices'])) if grafo['matriz'][idx][j] == 1]
        print(f"\nVizinhos do vértice '{v}': {vizinhos}")
    else:
        print(f"\nO vértice '{v}' não existe.")


def verificar_percurso(grafo, percurso):
    for i in range(len(percurso) - 1):
        u = percurso[i]
        v = percurso[i + 1]
        if u not in grafo['vertices'] or v not in grafo['vertices']:
            print(f"\nO percurso {percurso} não é possível (vértice inexistente).")
            return False
        
        iu = grafo['vertices'].index(u)
        iv = grafo['vertices'].index(v)
        if grafo['matriz'][iu][iv] == 0:
            print(f"\nO percurso {percurso} não é possível (falha com os vértices '{u}' e '{v}').")
            return False
            
    print(f"\nO percurso {percurso} é POSSÍVEL.")
    return True


def exibir_grafo(grafo):
    vertices = grafo['vertices']
    matriz = grafo['matriz']
    
    if not vertices:
        print("\nO grafo está VAZIO.")
        return

    print("\n--- MATRIZ DE ADJACÊNCIA ---")
    print("      " + "   ".join(str(v) for v in vertices))
    for i, v in enumerate(vertices):
        linha_str = "   ".join(str(val) for val in matriz[i])
        print(f" {v} |  {linha_str}")


def main():
    grafo = criar_matriz()

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

        escolha = input("Digite o número da opção desejada: ").strip()

        if escolha == "1":
            v = input("Digite o nome do vértice a ser inserido: ").strip()
            inserir_vertice(grafo,v)
        elif escolha == "2":
            u = input("Digite o primeiro vértice: ").strip()
            v = input("Digite o segundo vértice: ").strip()
            inserir_aresta(grafo, u, v)
        elif escolha == "3":
            v = input("Digite o nome do vértice a ser removido: ").strip()
            remover_vertice(grafo, v)
        elif escolha == "4":
            u = input("Digite o primeiro vértice: ").strip()
            v = input("Digite o segundo vértice: ").strip()
            remover_aresta(grafo, u, v)
        elif escolha == "5":
            v = input("Digite o nome do vértice para calcular o grau: ").strip()
            calcular_grau(grafo, v)
        elif escolha == "6":
            u = input("Digite o primeiro vértice: ").strip()
            v = input("Digite o segundo vértice: ").strip()
            verificar_aresta(grafo, u, v)
        elif escolha == "7":
            u = input("Digite o vértice para listar os vizinhos: ").strip()
            listar_vizinho(grafo, u)
        elif escolha == "8":
            entrada = input("Digite o percurso, separado por vírgulas (A,B,C etc): ").strip()
            percurso = [x.strip() for x in entrada.split(",")]
            verificar_percurso(grafo,percurso)
        elif escolha == "9":
            exibir_grafo(grafo)
        elif escolha == "0":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()