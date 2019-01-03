frase = "Oi tudo bem?"
lista = ["Joao", "Maria", frase, "final", "ponto"]

print(lista)
print(lista[-1:-3:-1])

lista.append('lorena')
print(lista)
print(lista[-1:-3:-1])

lista.remove("Maria")
print(lista)

lista.insert(2,"Joao")
contador_joao = lista.count("Joao")
print(lista)
print(contador_joao)
print(len(frase))
print(len(lista))

print(lista.pop())
print(lista)
print(lista.pop())
print(lista)
print(lista.pop())
print(lista)

print(frase.split(' '))

