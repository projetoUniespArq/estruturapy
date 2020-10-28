lcategoria = []
ltematica = []
newTematica = []
llivro = []
tipolivro=[]
livro = dict()
categoria = dict ()
tematica = dict ()


def menu ():
    print("Menu:")
    print("    1-Cadastro de categorias e temáticas")
    print("    2-Cadastro de novos livros")
    print("    3-Editar quantidade de um titulo")
    print("    4-Excluir livros")
    print("    5-Busca por exemplares")
    print("    6-Importar informações de um livro por arquivo")
    print("    7-Status de livros")
    print("    8-Gerar relatorios")
    print('    9-Sair do sistema')
    opc = int(input('    Digite sua opção: '))
    return opc
    
def cadastroCategoriasTematicas ():
    print("-----Cadastro de Categorias e Temáticas------")
    opc = int(input("Deseja cadastrar uma categoria nova?\n1-SIM\n2-Cadastro de Temáticas\n3-NÃO(Volta ao menu principal): ")) 
    while (opc != 4):
        if (opc==1):
            categoria["Categoria"] = input("Digite a categoria: ").upper()
            if categoria in lcategoria:
                print("Essa categoria já esta cadastrada!")
                main()
            else:
                lcategoria.append(categoria.copy())
                print(lcategoria)
                print("Categoria cadastrada com sucesso!")
                main()           
        elif (opc==2): 
            for i, j in enumerate (lcategoria):
                print(f'\n{i}-',end = ' ')
                for k in j.values():
                    print(f'{k}', end=' ')
            procuraCategoria = int(input("\nDigite o numero da categoria: "))
            recebendoCategoria = lcategoria[procuraCategoria]["Categoria"]
            newTematica.clear()
            if ltematica == []:
                tematica["Categoria"]=recebendoCategoria
                novaTematica=input("Digite a tematica: ").upper()
                newTematica.append(novaTematica)
                tematica["Tematica"]=newTematica[:]
                ltematica.append(tematica.copy())
                print(ltematica)
                main()
            a=0
            for m in range (len(ltematica)):
                if ltematica[m]["Categoria"]==recebendoCategoria:
                    print(f"no for {m}")
                    print(ltematica[m]["Categoria"])
                    print(recebendoCategoria)
                    a=m
            if ltematica[a]["Categoria"]==recebendoCategoria:
                novaTematica = input("Digite a tematica: ").upper()
                ltematica[a]["Tematica"].append(novaTematica)
                print(ltematica)
                main()
            else: 
                tematica["Categoria"]=recebendoCategoria
                novaTematica = input("Digite a tematica: ").upper()
                newTematica.append(novaTematica)
                tematica["Tematica"]=newTematica[:]
                ltematica.append(tematica.copy())
                print(ltematica)
                main()
                    
        elif (opc==3):
                main()    
def cadastroLivros ():
    print("-----Cadastro de Livros------")
    informeCategoria = input("Digite a categoria: ")
    informeTematica= input("Digite a temática: ")

    livro = {
        "Categoria":informeCategoria,
        "Tematica":informeTematica,
        "Titulo": input("Informe o titulo: "),
        "Autor": input("Informe o Autor: "),
        "Ano": int(input("Digite o ano: ")),
        "Assunto": input("Digite o Assunto: ")
    }
    
    print(livro)
def main ():
    opcao=menu ()
    while opcao != 3:
        if opcao == 1:
            cadastroCategoriasTematicas()
        elif opcao == 2:
            cadastroLivros()

 
              
main ()
    

