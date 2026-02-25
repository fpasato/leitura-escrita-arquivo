
with open("nomes_ficticios.txt", "r", encoding="utf-8") as arquivo:
    nomes = arquivo.read().split("\n")
    
    nomes = [nome.lower() for nome in nomes]    
    nomes.sort()
    
    with open("nomes_tratados.txt", "w", encoding="utf-8") as arquivo:
        for nome in nomes:
            arquivo.write(f"{nome}\n")


