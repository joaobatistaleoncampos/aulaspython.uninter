print('CALCULADORA')
print('+ Adição')
print('- Subtração')
print('* multiplicação')
print('/ Divisão')
print('pressione qualquer outra tecla pra sair.')

op = input('qual operação deseja realizar?')
x = float(input('Digite o primeiro valor:'))
y = float(input('Digite o segundo valor:'))

if  (op =='+'):
    res = x + y 
    print(f' resultado: {x} + {y} = {res}')
elif (op == '-'):
    res = x - y 
    print(f'resultado: {x} - {y} = {res}')
elif (op == '*'):
    res = x * y 
    print(f'resultado: {x} x {y} = {res}')
elif (op == '/'):
    res = x / y 
    print(f'resultado: {x} / {y} = {res}')

else:  
    print(f'opção invalida tente novamente!!')  
    print('Encerramos o programa...')
