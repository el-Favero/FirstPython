n1 = float(input('Digite um número'))
n2 = float(input('Diga outro numero'))
a =  n1 -1
b = 1 + n1
area = n1 * n2
litro = area/2
dobro = n1 * 2
triplo = n1 * 3
raiz = n1 **(1/2)
m = (n1 + n2) / 2
centimetros = n1 *100
mili = n1*1000
dolar1 = n1 / 3.27
dolar2 = n1 / 5.63
desconto = n1 * 0.95
salario = n1 * 1.15
t0 = n1*1
t1 = n1*1
t2 = n1*2
t3 = n1*3
t4 = n1*4
t5 = n1*5
t6 = n1*6
t7 = n1*7
t8 = n1*8
t9 = n1*9
t10 = n1*10
print('o numero escolhido foi o {}\nseu antecessor é o {}\ne o seu sucessor é {}'.format(n1,a,b))
print('seu dobro é igual a {}\nseu triplo é igual a {}\ne a sua Raiz quadrada é igual a {:.3f}' .format(dobro,triplo, raiz))
print('a média dele é igual a {}'.format(m))
print( 'ele tem {}m, que equivale a {}cm, que equivale a {}mil' .format(n1, centimetros, mili))
print('Na cotação do video, com esse valor {}$, eu conseguiria comprar {:.3f} Dolar, mas na cotação atual, eu conseguiria compar {:.3f}Dolar'.format(n1,dolar1,dolar2))
print('o Preço do produto é {}$ e com o desconto, ele fica {}$'.format(n1, desconto))
print('Jorge tem um sálario de {}$, mas nesse mês ele teve uma bonificação de 15%,que resulta em {:.3f }$'.format(n1,salario))
print('esse quarto tem {}m2 de altra e {}m2 de largura, sua área é de {}m2 e a quantidade de tinta necessária é de {}L'.format(n1, n2, area, litro ))
print('seu numero escolhido foi o {} e a sua tabuada é x0={}, x1={}, x2={}, x3={}, x4={}, x5={}, x6={}, x7={}, x8={}, x9={} e x10={}'.format(n1,t0,t1, t2, t3, t4, t5, t6, t7, t8, t9, t10))