import csv
import json
import database

# =============================================================
# ================== EXPORTAÇÃO PARA CSV ======================
# =============================================================

# Função para exportar dados (receitas ou despesas) para um ficheiro CSV
def exportar_para_csv(tipo, caminho):
    dados = []  # Lista que armazenará os dados a serem exportados

    # Decide quais dados buscar com base no tipo ('receitas' ou 'despesas')
    if tipo == "receitas":
        dados = database.listar_receitas()
    elif tipo == "despesas":
        dados = database.listar_despesas()

    # Abre o ficheiro no modo escrita, com codificação UTF-8 com BOM (compatível com Excel)
    with open(caminho, mode='w', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f)  # Cria um escritor CSV
        writer.writerow(["valor", "categoria"])  # Escreve o cabeçalho do ficheiro
        writer.writerows(dados)  # Escreve todas as linhas com os dados

# =============================================================
# ================== EXPORTAÇÃO PARA JSON =====================
# =============================================================

# Função para exportar dados (receitas ou despesas) para um ficheiro JSON
def exportar_para_json(tipo, caminho):
    dados = []  # Lista para armazenar os dados

    # Busca os dados conforme o tipo
    if tipo == "receitas":
        dados = database.listar_receitas()
    elif tipo == "despesas":
        dados = database.listar_despesas()

    # Abre o ficheiro no modo escrita com codificação UTF-8
    with open(caminho, mode='w', encoding='utf-8') as f:
        # Converte os dados em uma lista de dicionários e grava no ficheiro
        json.dump(
            [{"valor": v, "categoria": c} for v, c in dados],  # Converte cada tupla (v, c) em dict
            f,
            indent=4,               # Indenta o JSON para melhor legibilidade
            ensure_ascii=False      # Permite caracteres acentuados no ficheiro
        )

# =============================================================
# ==================== IMPORTAÇÃO DE CSV ======================
# =============================================================

# Função para importar dados de um ficheiro CSV para o banco de dados
def importar_de_csv(tipo, caminho):
    # Abre o ficheiro no modo leitura com codificação compatível com Excel
    with open(caminho, mode='r', newline='', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)  # Lê o CSV como dicionários (com base no cabeçalho)
        for linha in reader:
            valor = float(linha["valor"])  # Converte o valor de string para float
            categoria = linha["categoria"]  # Lê a categoria como string
            # Insere no banco de dados de acordo com o tipo
            if tipo == "receitas":
                database.inserir_receita(valor, categoria)
            elif tipo == "despesas":
                database.inserir_despesa(valor, categoria)

# =============================================================
# ==================== IMPORTAÇÃO DE JSON =====================
# =============================================================

# Função para importar dados de um ficheiro JSON para o banco de dados
def importar_de_json(tipo, caminho):
    # Abre o ficheiro no modo leitura com codificação UTF-8
    with open(caminho, mode='r', encoding='utf-8') as f:
        dados = json.load(f)  # Lê e converte o JSON para uma lista de dicionários
        for item in dados:
            valor = float(item["valor"])  # Converte o valor para float
            categoria = item["categoria"]  # Lê a categoria
            # Insere no banco de acordo com o tipo
            if tipo == "receitas":
                database.inserir_receita(valor, categoria)
            elif tipo == "despesas":
                database.inserir_despesa(valor, categoria)
