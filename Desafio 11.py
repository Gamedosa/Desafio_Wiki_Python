'''Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
A) o produto do dobro do primeiro com metade do segundo .
B) a soma do triplo do primeiro com o terceiro.
C )o terceiro elevado ao cubo.'''

Number1 = int(input('Informe um numero inteiro : \n'))
Number2 = int(input('Informe um numero inteiro : \n'))
number3 = float(input('Informe um numero real : \n'))

print ('Soma:', ((2*Number1) * (Number2/2)))
print ('Produto:', (3 * Number1) + number3)
print ('Cubo:', number3 ** 3)