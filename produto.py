from conexao import conecta_db
from menu import opcao_menu
 



def menu_produto(titulo):
    opcao_menu(titulo)

    while True: 
        opcao = input("Escolha uma opção: ")
        conexao = conecta_db()

        if opcao == "1": 
            listar(conexao)
            

        elif opcao =="2":
            consultar_produto_por_id(conexao)
            opcao_menu(titulo)

        elif opcao =="3":
            listar(conexao)
            inserir_produto(conexao)
            listar(conexao)
            opcao_menu(titulo)

        elif opcao =="4":
            listar(conexao)
            alterar_produto(conexao)
            listar(conexao)
            opcao_menu(titulo)

        elif opcao =="5":
            listar(conexao)
            deletar_produto(conexao)
            listar(conexao)
            opcao_menu(titulo)
        
        elif opcao =="6":
            print ("Sair")  
            break  
        else :
            print ("Opção invalida, tente novamente. ")    

def listar(conexao):
    cursor = conexao.cursor()
    sql_listar = """select p.id,p.nome,p.valor_venda,p.estoque,
                     p.categoria_id as categoria_id, c.
                     id as id_categoria,
                     c.nome as nome_categoria from produto p
                     inner join categoria c on (p.categoria_id = c.id)
                     order by p.id asc
                 """
     # cursor serve como o sql editor
    # execução de select no banco de dados
    cursor.execute(sql_listar) #recuparar todos os registros order by asc = ascendente e desc = descendente
    registros = cursor.fetchall() # fetchall retorna uma lista no caso dentro da variavel registro
    print("__________________")
    for registro in registros:
        print(f"|  ID: {registro[0]} - Nome: {registro[1]} - valor venda: {registro [2]} - Estoque: {registro[3]} - Categoria: {registro[6]} ")
        print("__________________")

def consultar_produto_por_id(conexao):
    id =  input("Digite o ID : ")
    cursor = conexao.cursor()
    cursor.execute("select id,nome,valor_venda,estoque from produto where id =" + id)
    registro = cursor.fetchone()
    print(registro)
    if registro is None :
        print("Produto não encontrado: ")
    else : 
        print(f"|ID : {registro[0]}")
        print(f"|Nome : {registro[1]}")
        print(f"|Valor venda : {registro[2]}")
        print(f"|Estoque : {registro[3]}")


def inserir_produto(conexao) :
    print("Inserindo o Produto..: ")
    cursor = conexao.cursor()
    nome = input(" Nome : ")
    valor_venda = float(input("Valor Venda :"))
    estoque = float(input("Estoque : "))
    categoria_id = int(input( "ID : categoria : "))
    sql_insert = "insert into produto(nome,valor_venda,estoque, categoria_id) values (%s, %s, %s, %s)"
    dados = (nome,valor_venda,estoque,categoria_id)
    cursor.execute(sql_insert,dados)
    conexao.commit()

def alterar_produto(conexao):
    print("Alterarando a produto...")
    cursor = conexao.cursor()
    id = input("Digite o ID: ")

    nome = input(" Nome : ")
    valor_venda = float(input("Valor Venda :"))
    estoque = float(input("Estoque : "))
    categoria_id = int(input("Categoria : "))
    sql_update = "update produto set nome = %s, valor_venda = %s, estoque = %s, categoria_id = %s where id = %s"
    dados = (nome,valor_venda,estoque,id,categoria_id)
    cursor.execute(sql_update,dados)
    conexao.commit()

def deletar_produto(conexao):
    print("Deletando o produto")
    cursor = conexao.cursor()
    id = input("Digite o ID: ")
    sql_delete = "delete from produto where id = " + id
    cursor.execute(sql_delete)
    conexao.commit()