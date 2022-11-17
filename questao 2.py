from random import randint

jogador1 = []
jogador2 = []
n = str(input('digite seu nome:  '))
f = str(input('digite seu nome:  '))
while True:

    jogada = randint(1, 6)
    jogador1.append(jogada)
    print(f'senhore {n} voce sorteou o numero {jogada}')
    jogadaf = randint(1, 6)
    jogador2.append(jogadaf)
    print(f'senhore {f} voce sorteou o numero {jogadaf}')
    resp = str(input(f'para continuar jogando digite 1, para sair digite 2:  '))
    if resp in '2':
        break

soma1 = sum(jogador1)
soma2 = sum(jogador2)
if soma2 > soma1:
    print(f'{f} venceu')
else:
    print(f'{n} venceu')


print(f'score do  jogador(a) {n} teve os seguintes numeros no dado {jogador1} totalizando {sum(jogador1)}')
print(f'score do jogador(a) {f} teve os seguintes numeros no dado {jogador2} totalizando {sum(jogador2)}')
