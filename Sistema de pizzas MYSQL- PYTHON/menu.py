from database import Pizza

pizza=Pizza()

def menu():
    while True:
        opcao = int(input("Digite 1- Adicionar\n2-Excluir\n3-Listar\n4-Editar\n5-Sair do Programa"))

        if opcao==1:
            sabor = input("Digite o sabor da pizza")
            tamanho = input("Digite o tamanho da pizza")
            preço = int(input("Digite o preço"))
            pizza.inserir_pizza(sabor,tamanho,preço)
            print("Pizza adicionada com sucesso!")
        
        if opcao==2:
            pizza.listar_pizzas()
            id = int(input("Digite o ID da pizza que você deseja excluir"))
            pizza.excluir_pizza(id)
            
        if opcao==3:
            print("Lista de pizzas")
            pizza.listar_pizzas()
            
        if opcao==4:
            pizza.listar_pizzas()
            id = int(input("Digite o ID da pizza que você deseja alterar"))
            nome = input("Digite o nome da pizza")
            tamanho = input("Digite o tamanho")
            preço = int(input("Digite o preço "))
            pizza.alterar_pizza(id,nome,tamanho,preço)
        
        if opcao==5:
            print("Adeus!")
            break
            
    
