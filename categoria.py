from conexao import conecta_db
from cliente import opcao_menu 
from menu import opcao_menu



def categoria_menu(titulo):
    opcao_menu(titulo)

    while True:
        opcao = input("Escolha uma opção: ")
        conexao = conecta_db()


        if opcao ==  "1":
            listar_categoria(conexao)

        elif opcao == "2":
            
            consultar_categoria_por_id(conexao)
            opcao_menu(titulo)

        elif opcao == "3":
            
            inserir_categoria(conexao)
            listar_categoria(conexao)
            opcao_menu(titulo)

        elif opcao == "4":
            
            atualizar_categoria(conexao)
            listar_categoria(conexao)
            opcao_menu(titulo)

        elif opcao == "5":
            
            deletar_categoria(conexao)
            listar_categoria(conexao)
            opcao_menu(titulo)
            
            
        elif opcao == "6":
            print("Sair")  
            break
        else:
            print("Opção inválida, tente novamente")   

def listar_categoria(conexao):
    cursor = conexao.cursor()
    #Execução de select no banco de dados
    cursor.execute("select id, nome, valor_venda, estoque  from produto order by id desc")
    registros = cursor.fetchall() #recupera todos os registros
    print("--------------------------------------------------")

    for registro in registros:       
        print( str(registro[0]) + "   - " + str(registro[1]))    


def consultar_categoria_por_id(conexao):
    id = input("Digite o ID: ")
    cursor = conexao.cursor()
    cursor.execute("select id, nome from categoria where id = " + id)
    registro = cursor.fetchone()

    if registro is None:
        print("Cliente não encontrado")
    else:
        print(f"| ID ..: {registro[0]}")
        print(f"| Nome : {registro[1]}")
        print("--------------------------------------------")


def inserir_categoria(conexao):
    print("Inserindo categoria ..: ")
    cursor = conexao.cursor()
    nome = input("Nome : ")
    sql_insert = "Insert into categoria (nome) values ('" + nome + "')"
    cursor.execute(sql_insert)
    conexao.commit()


def atualizar_categoria(conexao):
    print("Alterando dados da categoria")
    cursor = conexao.cursor()
    id = input("Digite o ID : ")
    nome = input("Nome : ")
    sql_update = "Update categoria set nome = '" + nome + "'where id = "+ id
    cursor.execute(sql_update)
    conexao.commit()
 
def deletar_categoria(conexao):
    print("Deletando categoria")
    cursor = conexao.cursor()
    id = input("Digite o ID : ")
    sql_delete = "Delete from categoria where id = " + id
    cursor.execute(sql_delete)
    conexao.commit()