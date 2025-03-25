from database import Pizza
import menu

def main():
    pizza= Pizza()
    pizza.listar_pizzas()
    menu.menu()
    

if __name__=="__main__":
    main()
    