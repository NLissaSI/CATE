# Calculadora de Indice de Massa Corporea (IMC)

# Entrada de dados
nome = input("Digite seu nome: ")
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: ")) ## altura com ponto decimal

# Funcao para calcular o IMC
def calcula_imc(peso, altura):
    imc = peso / (altura ** 2) ## altura ao quadrado
    return imc

# Funcao para classificacao do IMC
def classifica_imc(imc):
    if imc < 18.5:
        print(f"{nome} seu imc é {imc:.2f} então está Abaixo do Peso")
    elif 18.5 <= imc < 24.9:
        print(f"{nome} seu imc é {imc:.2f} então está no Peso Ideal")
    elif 25 <= imc < 29.9:
        print(f"{nome} seu imc é {imc:.2f} então está com Sobrepeso")
    elif 30 <= imc < 34.9:
        print(f"{nome} seu imc é {imc:.2f} então está com Obesidade grau 1")
    elif 35 <= imc < 39.9:
        print(f"{nome} seu imc é {imc:.2f} então está com Obesidade grau 2")
    else:
        print(f"{nome} seu imc é {imc:.2f} então está com Obesidade grau 3")

# Print do resultado
imc = calcula_imc(peso, altura) ## Chama a funcao para calcular o IMC

classifica_imc(imc) ## Chama a funcao para classificar o IMC

# Pergunta se o usuário deseja fazer outro cálculo de IMC
decisao = input("Deseja fazer outro cálculo de IMC? (s/n): ")

# O loop continua até que o usuário digite `n`
while decisao.lower() == 's': ## Coloca o `input` da decisao em minusculo e verifica se é `s`, se for, fica no loop
    nome = input("Digite seu nome: ")
    peso = float(input("Digite seu peso em kg: "))
    altura = float(input("Digite sua altura em metros: "))

    imc = calcula_imc(peso, altura)
    
    classifica_imc(imc)
    
    decisao = input("Deseja calcular o IMC de outra pessoa? (s/n): ")
# Fim do loop

# Mensagem de despedida
print("Obrigado por usar a calculadora de IMC!")

# Fim do programa
