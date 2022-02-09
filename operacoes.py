usuarios = {1,5,76,34,52,13,17}

#tamanho do conjunto
print(f'o conjunto tem {len(usuarios)} elementos.')

#adiciona um elemento
usuarios.add(765)
print(f'o conjunto tem {len(usuarios)} elementos.')

usuarios.add(765) #se já existe o elemento ele não adiciona
print(f'o conjunto tem {len(usuarios)} elementos.')

#congela um conjunto para impedir que tenha mudanças
usuarios_congelados = frozenset(usuarios)
print(f'o conjunto tem {len(usuarios)} elementos.')

#usuarios_congelados.add(134)

#tabalhando com texto
meu_texto = 'O Capitalismo falhou falha e falhara em cada um dos lugares que ele colcoar os seus tentaculos que se baseiam na exploração do homem pelo homem'
print(set(meu_texto.split()))

