#Exemplo de herança:


# Classe pai
class Veiculo:
    def __init__(self, modelo):
        self.modelo = modelo

    def dirigir(self):
        print(f"Dirigindo o {self.modelo}.")

# Classe filha que herda de Veiculo
class Carro(Veiculo):
    def __init__(self, modelo, cor):
        super().__init__(modelo)  # Chama o construtor da classe pai
        self.cor = cor

    def exibir_cor(self):
        print(f"A cor do carro é {self.cor}.")

# Usando as classes
carro = Carro("Fusca", "azul")
carro.dirigir()       # Herança do método "dirigir"
carro.exibir_cor()    # Método específico da classe Carro
