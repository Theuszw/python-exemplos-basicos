from classes.cachorro import Cachorro
from classes.gato import Gato

# função para demonstrar polimorfismo
def emitir_som (animal):
    print(f"{animal.get_home()} faz: {animal.fazer_som()}")
    print(" ")

def main():
    # Criando Instâncias (Objetos) das Classes
    rex = Cachorro("Rex", "Labrador")
    mimi = Gato ("Mimi", "Branco")

    # Demonstrando o funcionamento
    print (" ")
    print(f"Nome do cachorro{rex.get_nome()}")
    print(f"Raça do cachorro{rex.raca()}")
    print(" == 2DE == DEVs Python :)")
    print(f"Nome do gato{mimi.get_nome()}")
    print(f"Raça do gato{mimi.cor()}")
    print(" ")

    # Demonstrando polimorfismo
    emitir_som(rex)
    emitir_som(mimi)

if __name__ == "__main__":
    main()