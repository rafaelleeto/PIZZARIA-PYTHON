import mysql.connector

class  Pizza:
    def __init__(self):
        self.__conexao = mysql.connector.connect(
            host='localhost',
            user='leeto',
            password='root',
            database='pizaria',
        )
        self.__cursor = self.__conexao.cursor()
        self.criar_tabela()
        
    def criar_tabela(self):
        query=(""" create table if not exists pizzas(id int auto_increment primary key,
               nome varchar(255) not null,tamanho varchar(255) not null default 'grande',
               preco decimal(10,2))
               """)
        self.__cursor.execute(query)
        self.__conexao.commit()
        
    def inserir_pizza(self,nome,tamanho,preco):

        query=("""insert into pizzas(nome,tamanho,preco) values (%s,%s,%s)""")
        self.__cursor.execute(query,(nome,tamanho,preco))
        self.__conexao.commit()
        
    def listar_pizzas(self):
        query = ("select * from pizzas")
        self.__cursor.execute(query)
        lista_de_pizzas =  self.__cursor.fetchall()
        
        if not lista_de_pizzas:
            print("Pizza não cadastrada")
        else:
            for pizza in lista_de_pizzas:
                print(f"ID: {pizza[0]} | nome: {pizza[1]} | tamanho: {pizza[2]} | preço: {pizza[3]}")
    
    def excluir_pizza(self,id):
        query= ("""DELETE FROM pizzas WHERE id = %s """)
        self.__cursor.execute(query,(id,))
        self.__conexao.commit()
    
    def alterar_pizza(self,id,nome,tamanho,preço):
        
        query=("""UPDATE pizzas SET nome=%s,tamanho=%s,preco=%s WHERE id = %s""")
        self.__cursor.execute(query,(nome,tamanho,preço,id))
        