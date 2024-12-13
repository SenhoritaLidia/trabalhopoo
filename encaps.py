#Exemplo de Encapsulamento:


class Perfume:
    def __init__(self, nome, volume):
        self.__nome = nome  # Atributo privado
        self.__volume = volume  # Atributo privado

    # Método público para acessar o nome
    def get_nome(self):
        return self.__nome

    # Método público para acessar o volume
    def get_volume(self):
        return self.__volume

    # Método público para alterar o nome
    def set_nome(self, nome):
        self.__nome = nome

    # Método público para alterar o volume
    def set_volume(self, volume):
        if volume > 0:
            self.__volume = volume
        else:
            print("Volume inválido!")

# Usando a classe
perfume = Perfume("Chanel No. 5", 100)

# Acessando os atributos através dos métodos
print(perfume.get_nome())    # "Chanel No. 5"
print(perfume.get_volume())  # 100

# Alterando o nome e o volume usando os setters
perfume.set_nome("Dior Sauvage")
perfume.set_volume(150)

print(perfume.get_nome())    # "Dior Sauvage"
print(perfume.get_volume())  # 150

# Tentando acessar diretamente os atributos privados
# print(perfume.__nome)  # Erro: AttributeError
