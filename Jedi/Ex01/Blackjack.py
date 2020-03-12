import random

class BlackJack:

    def __init__(self):
        self.baralho = ['1','2','3','4','5','6','7','8','9','10','J','Q','K','A']

    def embaralhar(self):
        carta = random.randint(0, len(self.baralho) -1)
        return carta

    def jogador(self):
        pass

    def dealer(self):
        pass





a = BlackJack()
print(a.embaralhar())