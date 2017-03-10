import random, time
startTime= time.time()
l = []

for k in range(10000):
    l.append(random.randint(1, 10000-1))

print('lista desordenada')
print(l)

#bubble sort

print('ordenando...')
tam_lista = len(l)

for i in range(tam_lista):
    for j in range(1, tam_lista - i):

        if l[j] < l[j-1]:
            l[j], l[j - 1] = l[j-1], l[j]



print()
print('vetor ordenado')
print(l)
endTime = time.time()

print('Took %s seconds to calculate.' %((endTime - startTime )))

