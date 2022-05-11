import random
maquina = random.randint(1, 100)
print("Adivinhe qual número entre 1 e 100 eu estou pensando!")
adivinhar = False

# p igual a palpate
p = 0
while not adivinhar:
    usuario = int(input("Digite um número: "))
    p = p + 1
    if usuario == maquina:
        adivinhar = True
    else:
        if usuario < maquina:
            print("Seu palpite está abaixo do meu número! Tente a sorte mais uma vez.")
        elif usuario > maquina:
            print("Seu palpite está acima do meu número! Tente a sorte mais uma vez.")
print("Essa foi boa! Você acertou com {} tentativas!". format(p))