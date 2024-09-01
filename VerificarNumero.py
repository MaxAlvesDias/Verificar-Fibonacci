def verificarFibonacci(n):
    a, b = 0, 1
    count = 1
    while a < n:
        a, b = b, a + b
        count += 1
    return a == n, count if a == n else -1

numero = int(input("Digite um numero para verificação se ele pertence a sequencia fibonacci: "))
pertence, posicao = verificarFibonacci(numero)

if pertence:
    print(f"O número {numero} pertence à sequência de Fibonacci e está na posição: {posicao}.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")
