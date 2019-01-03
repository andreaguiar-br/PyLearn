val_verdadeiro = True
val_falso = False
valorInput = input("Entre um valor: ")

# print(type(val_verdadeiro), val_verdadeiro)
# if (val_verdadeiro):
#     print ("verdadeiro")
#     print ("Segundo valor")
# print ("Fora do if")

if int(valorInput) > 5 :
    print ("Valor maior que 5")
elif int(valorInput) == 5 :
    print("valor === igual === a 5")
else:
    print ("Valor MENOR ou igual a 5")