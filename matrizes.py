matriz = [
    [3, 8, 1],
    [4, 9, 6],
    [2, 7, 5]
]

print("EXIBIÇÃO DA MATRIZ EM FORMATO DE GRADE")
for l in range(3):
    for c in range(3):
        print(f"{matriz[1][c]}", end=" ")
    print()
    
    print("-"*45)
    print(f"Elemento da linha 0 coluna 1: {matriz[0][1]}")
    print(f"Elemento da linha 2 coluna 2: {matriz[2][2]}")
    print("-"*45)
    
    soma_diagonal = 0
    
    for l in range(3):
        for c in range (3):
            if l == c:
                soma_diagonal += matriz[1][c]
    print(f"Soma dos elementos da Diagonal Principal: {soma_diagonal}")
    
