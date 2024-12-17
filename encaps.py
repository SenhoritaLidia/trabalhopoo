#Exemplo de Encapsulamento:


class Perfume:
    def __init__(self, nome, volume):
        self.__nome = nome  # Atributo privado
        self.__volume = volume  # Atributo privado

    def get_nome(self):
        return self.__nome

    def get_volume(self):
        return self.__volume

    def set_nome(self, nome):
        self.__nome = nome
    def set_volume(self, volume):
        if volume > 0:
            self.__volume = volume
        else:
            print("Volume inválido!")

perfume = Perfume("Chanel No. 5", 100)

print(perfume.get_nome())    # "Chanel No. 5"
print(perfume.get_volume())  # 100

perfume.set_nome("Dior Sauvage")
perfume.set_volume(150)

print(perfume.get_nome())    # "Dior Sauvage"
print(perfume.get_volume())  # 150

