class Personagem:
    def __init__(self, nome):
        self.nome = nome
        self.local = "floresta"

    def mudar_local(self, novo_local):
        self.local = novo_local

class Jogo:
    def __init__(self):
        self.personagem = Personagem("Aventureiro")

    def iniciar_jogo(self):
        print(f"Bem-vindo, {self.personagem.nome}! Você acorda em uma floresta escura.")
        self.floresta()

    def floresta(self):
        print("Você está perdido na floresta e vê duas trilhas.")
        print("1. Seguir pela trilha à esquerda.")
        print("2. Seguir pela trilha à direita.")
        
        escolha = input("O que você faz? (1 ou 2): ")
        
        if escolha == "1":
            self.trilha_esquerda()
        elif escolha == "2":
            self.trilha_direita()
        else:
            print("Opção inválida. Tente novamente.")
            self.floresta()

    def trilha_esquerda(self):
        print("\nVocê escolheu a trilha à esquerda e encontra um rio brilhante.")
        print("1. Tentar atravessar o rio.")
        print("2. Seguir ao longo do rio.")
        
        escolha = input("O que você faz? (1 ou 2): ")
        
        if escolha == "1":
            self.atravessar_rio()
        elif escolha == "2":
            self.seguir_rio()
        else:
            print("Opção inválida. Tente novamente.")
            self.trilha_esquerda()

    def trilha_direita(self):
        print("\nVocê escolheu a trilha à direita e encontra uma caverna.")
        print("1. Entrar na caverna.")
        print("2. Voltar para a floresta.")
        
        escolha = input("O que você faz? (1 ou 2): ")
        
        if escolha == "1":
            self.explorar_caverna()
        elif escolha == "2":
            self.floresta()
        else:
            print("Opção inválida. Tente novamente.")
            self.trilha_direita()

    def atravessar_rio(self):
        print("\nVocê tenta atravessar o rio, mas a correnteza é forte demais!")
        print("Infelizmente, você é arrastado e acaba sendo levado por ela.")
        print("Fim do jogo.")
    
    def seguir_rio(self):
        print("\nVocê segue o rio e encontra uma aldeia.")
        print("Você é bem-vindo na aldeia e vive em paz por muitos anos.")
        print("Fim do jogo.")
    
    def explorar_caverna(self):
        print("\nVocê entra na caverna e encontra um baú dourado!")
        print("1. Levar a espada e continuar explorando.")
        print("2. Deixar a espada e sair da caverna.")
        
        escolha = input("O que você faz? (1 ou 2): ")
        
        if escolha == "1":
            self.continuar_explorando()
        elif escolha == "2":
            self.sair_caverna()
        else:
            print("Opção inválida. Tente novamente.")
            self.explorar_caverna()

    def continuar_explorando(self):
        print("\nCom a espada mágica, você segue sua jornada e se torna um herói lendário!")
        print("Fim do jogo.")
    
    def sair_caverna(self):
        print("\nVocê sai da caverna e segue seu caminho, mas a aventura fica incompleta.")
        print("Fim do jogo.")

jogo = Jogo()
jogo.iniciar_jogo()
