#Crie um jogo de froca, com nomes de frutas.
import random
class Forca:
    def __init__(self):
        self.lista_frutas = ['banana', 'jabuticaba', 'pitanga', 'mirtilo', 'morango', 'abacaxi', 'cereja']

    def palavra(self):
        return random.choice(self.lista_frutas)

    def palpite(self):
        while True:
            palpite = []
            letra = input('Digite uma letra: ')
            if type(letra) != str and len(letra) != 1:
                print('Digite uma única letra!')
            elif letra == palpite:
                print('Você já digitou essa letra, tente outra! ')
            else:
                return True
        return palpite.append(letra)

a = Forca()
print(a.palpite())