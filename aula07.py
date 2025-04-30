n1 = int(input('Diga um valor?'))
n2 = int(input('Diga outro valor'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
ex = n1 ** n2
print ('A soma é igual a {},\nMultiplicação é igual a{},\ndivisão é igual a {:.3f},'.format(s, m, d,),end=' ')
print ('\nDivisão inteira é igual a {},\ne a potencia é igual a {}' .format(di, ex))
