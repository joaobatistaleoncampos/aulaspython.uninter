
print('escolha o que deseja comprar:')
print('1-maçã')
print('2-laranja')
print('3-banana')
produto =int(input('qual a sua escolha'))
qtd =int(input('quantas unidades?'))

if (produto == 1):
   pagar = qtd * 2.3
   print(f'voçê comprou {qtd}maçãs.total à pagar:{pagar}')
elif (produto == 2):
   pagar = qtd * 3.6
   print(f'voçê comprou{qtd} laranjas. total à pagar: {pagar}')
elif( produto == 3):
   pagar = qtd * 1.85
   print(f'voçê comprou {qtd} bananas.total à pagar: {pagar}')
else:
   print('produto inexistente')
   