def fibonacci(numero):
    if numero == 1:  
        return 1
    elif numero == 2:
        return 1
    else:
        return fibonacci(numero-2) + fibonacci(numero-1)

numero_da_sequencia = 25
lista = []
for iterador in range(1, numero_da_sequencia+1, 1):
    resultado = fibonacci(iterador)
    lista.append(resultado)


print(lista)