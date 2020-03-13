import random

class BlackJack:

    def __init__(self):
        self.baralho = [{'1':1},{'2':2},{'3':3},{'4':4},{'5':5},{'6':6},{'7':7},{'8':8},{'9':9},{'10':10},{'J':10},{'Q':10},{'K':10},{'A':1}]
        random.shuffle(self.baralho)

    def jogada(self):
        self.carta_baralho = []
        carta = self.baralho.pop()
        self.carta_baralho.append(carta)
        return self.carta_baralho

    def cartas_jogador(self):
        self.mao_jogador = []
        self.mao_jogador.append(self.carta_baralho)
        return self.mao_jogador

    def regras(self):
        self.mao_jogador





a = BlackJack()
a.jogada()
print(a.cartas_jogador())