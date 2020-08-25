def calc(nota0, nota1, nota2):
     media = (nota0 + nota1 + nota2) / 3
     print(f'Sua média é: {media}')




contador = 0
while contador < 1:
    result0 = float(input("Primeira nota: "))
    result1 = float(input("Segunda nota: "))
    result2 = float(input("Terceira nota: "))
    contador += 1

calc(result0, result1, result2)

