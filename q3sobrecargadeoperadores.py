class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __add__(self, other):
        return f"{self.nome} e {other.nome} são amigos!"

     def __gt__(self, other):
        return self.idade > other.idade

      def __str__(self):
        return f"Pessoa(Nome: {self.nome}, Idade: {self.idade})"

pessoa1 = Pessoa("Alice", 30)
pessoa2 = Pessoa("Bruno", 25)

print(pessoa1 + pessoa2) # "Alice e Bruno são amigos!"

if pessoa1 > pessoa2:
    print(f"{pessoa1.nome} é mais velha que {pessoa2.nome}")

else:
    print(f"{pessoa2.nome} é mais velho(a) que {pessoa1.nome}")

print(pessoa1)
print(pessoa2)