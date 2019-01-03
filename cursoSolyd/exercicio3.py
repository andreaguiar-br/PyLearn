'''
exercício 3: solicitar idade, peso e altura e decidir de o individio entrará no exercito
para entrar no exercito, deve-se ter ao menos 60kg, 18anos e 1,7m
'''
print("Avaliação para aptidão ao Exército")
print("==================================\n")
idade = int(input("Informe a sua idade: "))
peso = float(input("Informe o seu peso: "))
altura = float(input("Informe sua altura em metros: "))

print("Seu IMC é", peso/(altura**2))

if idade >= 18 and peso >= 60 and altura >= 1.7 :
    print("voce está apto a entrar no Exército")
else:
    print("Você está fora dos padrões para o Exército")
