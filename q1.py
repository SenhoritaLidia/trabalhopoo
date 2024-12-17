S# Em um dicionario no python foram colocados 2 tipos de bebidas e dentro de cada uma há um subtipo (nome da bebida) que foi implementada
# e dentro desse mesmo subtipo foram colocados os sabores e ingredientes . Exemplifique o codigo criando a variavel e use os conceitos ensinados em sala.


bebidas = {
    "refrigerante": {
        "Coca-Cola": {
            "sabores": ["Original", "Zero", "Cherry"],
            "ingredientes": ["Água", "Açúcar", "Cafeína"]
        },
        "Pepsi": {
            "sabores": ["Original", "Diet", "Max"],
            "ingredientes": ["Água", "Açúcar", "Aromatizantes"]
        }
    },
    "suco": {
        "Laranja": {
            "sabores": ["Laranja", "Laranja com Limão"],
            "ingredientes": ["Suco de laranja", "Água", "Açúcar"]
        },
        "Uva": {
            "sabores": ["Uva", "Uva Integral"],
            "ingredientes": ["Suco de uva", "Água", "Açúcar"]
        }
    }
}

# Acessando informações de bebidas
print(bebidas["refrigerante"]["Coca-Cola"]["sabores"])
print(bebidas["suco"]["Laranja"]["ingredientes"])

