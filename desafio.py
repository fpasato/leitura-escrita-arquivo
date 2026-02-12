# 🧠 Atividade Prática – Tratamento e Organização de Dados (10 Milhão de Nomes) | Dia 11/02
 
# 🎯 Objetivo
 
# Trabalhar com leitura de arquivo, manipulação de string, escrita de arquivo e ordenação de dados.
 
# 📋 Cenário
# A empresa DataClean Solutions gerou um arquivo chamado:
# nomes_aleatorios.py
# Esse arquivo gera 10.000.000 de nomes gerados automaticamente.
# Porém, o sistema da empresa exige que:
# Todos os nomes estejam em letras minúsculas
# A lista esteja ordenada em ordem alfabética
# Você foi contratado para resolver esse problema.
 
# 📌 O que você deve fazer
# Ler o arquivo nomes_ficticios.txt
# Converter todos os nomes para minúsculo
# Criar uma nova lista com os nomes convertidos
# Salvar o resultado em um novo arquivo chamado:
# nomes_tratados.txt
 
# 💻 Exemplo
 
# Se o arquivo original tiver:
# Ana SilvaCARLOS Souza
# Mariana Oliveira
# O novo arquivo deve conter:
# ana silva
# carlos souza
# mariana oliveira
 
# ⭐ Desafio Bônus (Mais Difícil)
# Após converter todos os nomes para minúsculo:
# Ordene a lista em ordem alfabética
# Salve o resultado já ordenado no arquivo final
 
# 🧠 Conceitos que deverão ser utilizados
# open() para leitura
# open() para escrita
# .lower()
# for
# .strip()
 
# ✅ Critérios de Avaliação
# Ler corretamente o arquivo
# Converter todos os nomes para minúsculo
# Criar um novo arquivo
# (Bônus) Ordenou corretamente em ordem alfabética


with open("nomes_ficticios.txt", "r", encoding="utf-8") as arquivo:
    nomes = arquivo.read().split("\n")
    
    nomes = [nome.lower() for nome in nomes]
    
    nomes.sort()
    
    with open("nomes_tratados.txt", "w", encoding="utf-8") as arquivo:
        for nome in nomes:
            arquivo.write(f"{nome}\n")