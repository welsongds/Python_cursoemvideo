prc = int(input('Qual o preço do produto? '))
prcn = prc - prc * 0.05
print('Com o desconto de 5%, o valor fica R${:.2f}.'.format(prcn))