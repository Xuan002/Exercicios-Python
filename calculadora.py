
print("---opções---")
print("[0] soma\n[1] subtração\n[2] divisão\n[3] multiplicação\n")
user = int(input("Digite sua escolha: "))
valor1 = float(input("Digite o valor: "))
valor2 = float(input("Digite o valor: "))


if user == 0:
     print("Resultado:",valor1 + valor2) 
elif user == 1:
    print("Resultado:",valor1 - valor2) 
elif user == 2:
    print("Resultado:",valor1 / valor2) 
elif user == 3:
    print("Resultado:",valor1 * valor2) 







