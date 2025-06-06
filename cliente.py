from conexao import conecta_db

def opcao_menu():
    print ("|-----------------------------------------------------------------------------------------------------------------|")
    print ("|                                                  Cadastro                                                       |")
    print ("|-----------------------------------------------------------------------------------------------------------------|")
    print ("| 1  -  Listar | 2  -  Consultar um Cliente por ID | 3  -  Inserir | 4  -  Alterar | 5  -  Deletar | 6  -  Voltar |")
    print ("|-----------------------------------------------------------------------------------------------------------------|")

def menu_cliente():
    opcao_menu()   
    
    while True:
        opcao = input("Escolha uma opção: ")
        conexao = conecta_db()


        if opcao ==  "1":
            listar_clientes(conexao)
        elif opcao == "2":
            listar_clientes(conexao)
            consultar_cliente_por_id(conexao)

        elif opcao == "3":
            inserir_cliente(conexao)
            listar_clientes(conexao)

        elif opcao == "4":
            listar_clientes(conexao)
            atualizar_cliente(conexao)

        elif opcao == "5":
            listar_clientes(conexao)
            deletar_cliente(conexao)
            opcao_menu()
            
        elif opcao == "6":
            print("Sair")  
            break
        else:
            print("Opção inválida, tente novamente")   

def listar_clientes(conexao):
    cursor = conexao.cursor()
    #Execução de select no banco de dados
    cursor.execute("select id, nome from cliente order by id desc")
    registros = cursor.fetchall() #recupera todos os registros
    print("--------------------------------------------------")

    for registro in registros:       
        print( str(registro[0]) + "   - " + str(registro[1]))    


def consultar_cliente_por_id(conexao):
    id = input("Digite o ID: ")
    cursor = conexao.cursor()
    cursor.execute("select id, nome from cliente where id = " + id)
    registro = cursor.fetchone()

    if registro is None:
        print("Cliente não encontrado")
    else:
        print(f"| ID ..: {registro[0]}")
        print(f"| Nome : {registro[1]}")
        print("--------------------------------------------")


def inserir_cliente(conexao):
    print("Inserindo cliente ..: ")
    cursor = conexao.cursor()
    nome = input("Nome : ")
    sql_insert = "Insert into cliente (nome) values ('" + nome + "')"
    cursor.execute(sql_insert)
    conexao.commit()


def atualizar_cliente(conexao):
    print("Alterando dados do cliente")
    cursor = conexao.cursor()
    id = input("Digite o ID : ")
    nome = input("Nome : ")
    sql_update = "Update cliente set nome = '" + nome + "'where id = "+ id
    cursor.execute(sql_update)
    conexao.commit()
 
def deletar_cliente(conexao):
    print("Deletando cliente")
    cursor = conexao.cursor()
    id = input("Digite o ID : ")
    sql_delete = "Delete from cliente where id = " + id
    cursor.execute(sql_delete)
    conexao.commit()
