num = 1
pointPar=0
pointImpar=0

while num <= 100:
    if num%2 == 0:
        print(f"{num} é um número par")
        pointPar+=1
    else:
        print(f"{num} é um número impar")
        pointImpar+=1
    num+=1
    
print(f"Entre 1 e 100 há {pointPar} números pares e {pointImpar} ímpares")