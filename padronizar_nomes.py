
nomes = []

with open("nomes.txt", 'r', encoding= 'utf-8') as f:
    for linha in f:
        nomes.append(linha.strip().upper())

with open("nomes_upper.txt", 'w', encoding= 'utf-8') as f:
    for nome in nomes:
        f.write(nome + '\n')