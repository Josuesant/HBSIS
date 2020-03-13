from Ex01.Blackjack import BlackJack
class Jogador:
    def __init__(self,):
        self.jogadores = ''

    def __quantidade_jogadores(self):
        self.jogadores = int(input('Quantos jogadores nesta partida? '))
        if type(self.jogadores) == int and self.jogadores >= 1 and self.jogadores <= 7:
            return self.jogadores
        return 'Numero de jogadores não permitido! (nimíno 1, máximo 7)


#a = Jogador()