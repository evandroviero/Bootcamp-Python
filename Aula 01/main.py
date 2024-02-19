print('Hello World!')

def calcular_bonus(nome, salario, bonus):
    valor = 1000 + salario * bonus
    return f'Olá {nome}, o seu valor final será {valor:.2f}'

nome = input('Defina um nome: ')
salario = float(input('Defina o valor: '))
bonus = float(input('Digite um bonus: '))
print(calcular_bonus(nome=nome, salario=salario, bonus=bonus))

print('Final de execução')