aparicoes = {
    "Guilherme": 1,
    "cachorro": 2,
    "nome": 2,
    "vindo": 1
}

#busca o valor 
print(aparicoes["Guilherme"])

#busca o valor, mas retorna um valor padrão caso não encontre
print(aparicoes.get("Guilherme", 0))
print(aparicoes.get("xpto", 0))

#adicionando elemento
aparicoes["carlos"] = 2
print(aparicoes)

#remover um elemento
del aparicoes["carlos"]
print(aparicoes)

#interar pelos chaves
for elemento in aparicoes: # ou for elemento in aparicoes.keys()
    print(elemento)

#interar pelos valores
for elemento in aparicoes.values():
    print(elemento)


#interar pelas chaves e valores 
for chave, valor in aparicoes.items():
    print(chave, '=', valor)


meu_texto = 'O Capitalismo falhou falha e falhara em cada um dos lugares que ele colcoar os seus tentaculos que se baseiam na exploração do homem pelo homem'
meu_texto = meu_texto.lower()

aparicoes = {}

for palavra in meu_texto.split():
    ate_agora = aparicoes.get(palavra, 0)
    aparicoes[palavra] = ate_agora + 1

print(aparicoes)


from collections import defaultdict

meu_texto = 'O Capitalismo falhou falha e falhara em cada um dos lugares que ele colcoar os seus tentaculos que se baseiam na exploração do homem pelo homem'
meu_texto = meu_texto.lower()

aparicoes = defaultdict(int)

for palavra in meu_texto.split():
    aparicoes[palavra] += 1

print(aparicoes)

#contando palavras con contador
from collections import Counter
aparicoes = Counter(meu_texto.split())
print(aparicoes)