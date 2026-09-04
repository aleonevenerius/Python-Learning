num = int(input("Number: "))
var1 = 1
var2 = var1 + 1
soma = var1 + var2

while var1 <= num:
    print(f"{var1}+{var2}={soma}")
    var1+=1 
    var2 = var1 + 1
    soma = var1 + var2