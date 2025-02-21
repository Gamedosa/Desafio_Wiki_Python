#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9).

Temp = float(input('Informe a temperatura EM F° :\n'))
C = 5 * ((Temp-32) / 9)

print(f"A temperatura informado foi convertira para {C} C° ")