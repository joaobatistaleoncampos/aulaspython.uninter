preco = float(input('Digite o preço do produto'))
percentual = float(input('Digite o percentual de desconto( 0-100%):'))

desconto = preco * (percentual/100)
final = preco - desconto

print(f' preço do produto é { preco}. desconto de {percentual}%')
print(f'valor calculado de desconto:{desconto}.valor final do produto:{final}')

