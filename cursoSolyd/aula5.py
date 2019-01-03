# estruturas de repetição

nomes = ['guilherme', 'marcelo', 'Joao', 'Julia']

print(nomes)

for nome in nomes:
    print(nome)

listaNUm = range(5, 10)
for item in  listaNUm:
    print ( item)
    
i=0 
while i < len(nomes):
    print ( i , nomes[i])
    i += 1 