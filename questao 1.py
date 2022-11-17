def crialistavazia(tamanho):
    lista = []
    for i in range(tamanho):
        n = int(input('digite um valor: '))
        lista.append(n)

    return lista


# programa principal
lista1 = crialistavazia(int(input('digite o tamanho da lista:  ')))
print(f'a lista solicitada é {lista1}')
lista1.sort()
print(f'a lista ordenada é {lista1}')
print(f' a soma dos elementos da lista é  igual {sum(lista1)}')
print(f'o maior valor da lista é {max(lista1)}')
