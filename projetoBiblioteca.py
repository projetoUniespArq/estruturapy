lcategoria = []
ltematica = []
llivro = []
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
            cOrdenado=sorted(lcategoria,key=lambda l:l["Categoria"])
            for i, j in enumerate (cOrdenado,start=1):
                print(f'\n{i}-',end = ' ')
                for k in j.values():
                    print(f'{k}', end=' ')
            numeroCategoria = int(input("\nInforme o numero da categoria: "))
            tematica["Categoria"] = lcategoria[numeroCategoria-1]["Categoria"]
            tematica["Tematica"]= input("Digite a tematica: ").upper()
            if tematica not in ltematica:
                ltematica.append(tematica.copy())
                print("Temática cadastrada com sucesso")
                main()
            else:
                print("Temática já cadastrada")               
        elif (opc==3):
                main()    
def cadastroLivros ():
    print("-----Cadastro de Livros------")
    tOrdenado=sorted(ltematica,key=lambda l:(l["Categoria"],l["Tematica"]))
    for i, j in enumerate (tOrdenado,start=1):
        print(f'\n{i}-',end = ' ')
        for k in j["Categoria"],j["Tematica"]:
            print(f'{k} ',end = '')
    newBook = int(input("\nDigite o numero correspondente a categoria e a tematica: "))
    livro = {
        "Titulo": input("Informe o titulo: "),
        "Autor": input("Informe o Autor: "),
        "Ano": int(input("Digite o ano: ")),
        "Quantidade":int(input("Informe a quantidade de livros: ")),
        "Assunto": input("Digite o Assunto: ")
    }   
    if livro not in llivro:
        llivro.append(livro.copy())
        ltematica[newBook-1]["Livro"]=(llivro)
        print(ltematica)
        print(llivro)
        main()
    else:
        print("Livro já cadastrado")

    

def main ():
    opcao=menu ()
    while opcao != 3:
        if opcao == 1:
            cadastroCategoriasTematicas()
        elif opcao == 2:
            cadastroLivros()
        


 
              
main ()
    

