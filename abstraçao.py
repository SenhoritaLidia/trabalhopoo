from abc import ABC, abstractmethod

class Pessoa(ABC):
    @abstractmethod
    def trabalhar(self):
        pass

class Medico(Pessoa):
    def trabalhar(self):
        return "Estou cuidando de pacientes."

class Engenheiro(Pessoa):
    def trabalhar(self):
        return "Estou projetando edifícios."

medico = Medico()
engenheiro = Engenheiro()

print(medico.trabalhar()) 
print(engenheiro.trabalhar()) 