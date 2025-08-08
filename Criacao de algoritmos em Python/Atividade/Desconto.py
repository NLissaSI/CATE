# Desconto de 10% no valor do produto

# Nome e o preço do produto
nome = input("Digite o produto: ")
prec = float(input("Digite o preço do produto: "))

# Cálculo o preco com desconto
prec_final = prec * (1 - 0.10) ## Valor com desconto = preço original * (1 - taxa de desconto)

# Classificacao do produto
if prec_final > 1000:
    print("Muito caro")
elif 800 < prec_final <= 1000:
    print("Caro")
elif 500 <= prec_final <= 800:
    print("Justo")
else:
    print("Barato")

# Print para comparar o preço original e o preço com desconto
print(f"Produto: {nome}")
print(f"Preço original: R$ {prec:.2f}")
print(f"Preço com desconto: R$ {prec_final:.2f}")

# Fim do programa
