usuarios_data_science = [15,23,43,56]
usuarios_machine_learning = [13, 23, 56, 42]

assistiram = usuarios_data_science.copy()
assistiram.extend(usuarios_machine_learning)
#conjunto (set) conjuntos não tem elementos reptidos 
conjunto = set(assistiram)
print(conjunto)

#conjunto não tem index e nem ordem

usuarios_data_science = {15,23,43,56}
usuarios_machine_learning = {13, 23, 56, 42}
print(usuarios_data_science)
print(usuarios_machine_learning)

#união de conjuntos
assistiram = usuarios_data_science | usuarios_machine_learning
print(assistiram)

#retorna só os que estão nos dois grupos
esta_nos_dois_elementos = usuarios_data_science & usuarios_machine_learning
print(esta_nos_dois_elementos)

#retorna só os que estão somente no primeiro grupo
esta_somente_no_primeiro_grupo = usuarios_data_science - usuarios_machine_learning
print(esta_somente_no_primeiro_grupo)

#retorna só os que fizeram um dos dois mais não fez o outro
fez_um_dos_dois = usuarios_data_science ^ usuarios_machine_learning
print(fez_um_dos_dois)