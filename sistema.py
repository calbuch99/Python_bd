from cliente import menu_cliente
from categoria import categoria_menu
from produto import menu_produto
from usuario import menu_usuario, login
from conexao import conecta_db
from venda import menu_vendas

def menu_principal():
    print ("|-----------------------------------------------------|")
    print ("|              Menu  ->  Programa                     |")
    print ("|-----------------------------------------------------|")
    print ("|               1  -  Cliente                         |")
    print ("|               2  -  Categoria                       |")
    print ("|               3  -  Produto                         |")
    print ("|               4  -  Usuario                         |")
    print ("|               5  -  Vendas                          |")
    print ("|               6  -  Sair do Sistema                 |")
    print ("|-----------------------------------------------------|")
    
    while True:
        opcao = input("Escolha uma opção: ")
    

        if opcao ==  "1":
            menu_cliente("Cliente")
        elif opcao == "2":
            categoria_menu("Categoria")

        elif opcao == "3":
            menu_produto("produto")

        elif opcao == "4":
            menu_usuario("Cadastro de Usuario")

        elif opcao == "5":
            menu_vendas()

        elif opcao == "6":
            print("Sair do Sistema")  
            break
        else:
            print("Opção inválida, tente novamente")       # type: ignore

if __name__ == "__main__":  
    conexao = conecta_db()

while True:   
    resultado = login(conexao)  
    if resultado is True:
       menu_principal()
    else:
        login(conexao) 





    