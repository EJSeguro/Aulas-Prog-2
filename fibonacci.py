def fibonacci(numero):
   if numero == 1:
       return 1
   elif numero <= 2: 
       return 1
   else:
       return fibonacci(numero-2) + fibonacci(numero-1)

numero = 25

print(fibonacci(numero))