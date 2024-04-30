# OBI 2023 Modalidade Programação • Nível 1 • Fase 2 

'''N = int(input())
lista = []
for i in range(N):
    lista.append(int(i))
'''

'''N = 7
lista = [2, 2, 2, 3, 8, 5, 5]'''

N = 8
lista = [3, 2, 1, 2, 3, 1]

l = 0
r = 0
maior_intervalo = 0
contador = [0]*100

while r != N-1:
    if r - l > maior_intervalo:
        maior_intervalo = r - l

    n = lista[r]
    contador[n-1] += 1

    while contador[n-1] == 2:
        k = lista[l]
        contador[k-1] -= 1
        l += 1
    
    r += 1
    print(lista[l:r])
    
if r - l > maior_intervalo:
    maior_intervalo = r - l

print(maior_intervalo)