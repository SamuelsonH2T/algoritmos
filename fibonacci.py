'''

Código introdutório para programação dinâmica

Calcular o tempo de execução do algoritmo de fibonacci
de forma recursiva e de forma iterativa.

'''

'''

def fib(n):
    if n == 1 or n == 2:
        return 1

    return fib(n-1) + fib(n-2)


print(fib(10))

'''



import time
startTime= time.time()
MAX_N = 100
valores = [0] * MAX_N
valores[0] = valores[1]=1
def fib_otimo(n):
    if n > MAX_N:
        print('O valor maximo é 100')

    else:
        #print(valores[n-1])
        if valores[n-1] != 0:
            print('Fib de %d ja calculado'%n)
            return valores[n-1]

        else:
            print('Calculando fib de %d' %n)
            for i in range(2,n):
                valores[i] = valores[i-1] + valores[i-2]
            return valores[n-1]


#print(fib_otimo(70))
#print(fib_otimo(5))
#print(valores)


print(fib_otimo(70))
endTime = time.time()

print('Took %s seconds to calculate.' %(endTime - startTime))





'''
print('*******************************************************************************')


def calcProd():
    product = 1
    for i in range(1,100000):
        product = product *i

    return product

startTime = time.time()

prod = calcProd()

endTime = time.time()

print('This result is %s digits long.' %(len(str(prod))))

print('Took %s seconds to calculate.' %(endTime - startTime))
'''




