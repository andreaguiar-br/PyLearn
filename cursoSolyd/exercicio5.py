'''
solicitar numero de convidades
com estrutura de repetição, solicitar nome dos convidados
com estrutura de repetiçao, imprimr lista de convidados
'''

qtConvidados = input("Informe o numero de convidados: ")
listaConvidados = []

i = 1
while i <= int(qtConvidados):
    listaConvidados.append(input("Informe o nome do convidado nr." + str(i) + ': '))
    i += 1

i = 0
for nome in listaConvidados:
    print("Convidado ", i+1, ": ", nome)
    i += 1
print ("*** fim normal *** ")