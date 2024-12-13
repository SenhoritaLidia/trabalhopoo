class Animal:
    def emitir_som(self):
        pass

class Cachorro(Animal):
    def emitir_som(self):
        return "Latido"

class Gato(Animal):
    def emitir_som(self):
        return "Miau"

def fazer_som(animal):
    print(animal.emitir_som())

cachorro = Cachorro()
gato = Gato()

fazer_som(cachorro) 
fazer_som(gato) 