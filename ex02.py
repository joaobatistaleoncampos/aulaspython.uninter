km = int(input('quantos  KM foram percorridos?'))
dias = int(input('quantos dias foram percorridos?'))

preco = 60 * dias + 0.15*km
print(f'Km = {km}.Dias: {dias}.')
print(f'valor a ser pago: {preco}')