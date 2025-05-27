
# =============================================================
# Módulo responsável por gerar os gráficos do sistema Coinly
# Utiliza a biblioteca matplotlib para visualização de dados
# Gráficos: receitas e despesas agrupadas por categoria
# =============================================================

import matplotlib.pyplot as plt  # Biblioteca principal para gráficos
import database  # Importa funções que acessam o banco de dados

# =================== GRÁFICO DE RECEITAS ===================
def gerar_grafico_receitas():
    dados = database.listar_receitas()  # Lista todas as receitas
    categorias = {}  # Dicionário para somar os valores por categoria

    for valor, categoria in dados:
        categorias[categoria] = categorias.get(categoria, 0) + valor  # Agrupa valores por categoria

    # Cria o gráfico de barras
    plt.bar(
        categorias.keys(),       # Categorias no eixo X
        categorias.values(),     # Valores no eixo Y
        color="#4caf50",         # Cor das barras (verde)
        width=0.2                # Largura das barras (mais fino)
    )
    plt.title("Receitas por Categoria")  # Título do gráfico
    plt.xlabel("Categoria")              # Rótulo do eixo X
    plt.ylabel("Total (€)")              # Rótulo do eixo Y
    plt.grid(axis='y', linestyle='--', alpha=0.3)  # Grade leve no eixo Y
    plt.tight_layout()                   # Ajusta layout para não cortar texto
    plt.show()                           # Exibe o gráfico

# =================== GRÁFICO DE DESPESAS ===================
def gerar_grafico_despesas():
    dados = database.listar_despesas()  # Lista todas as despesas
    categorias = {}  # Dicionário para somar os valores por categoria

    for valor, categoria in dados:
        categorias[categoria] = categorias.get(categoria, 0) + valor  # Agrupa valores por categoria

    # Cria o gráfico de barras
    plt.bar(
        categorias.keys(),       # Categorias no eixo X
        categorias.values(),     # Valores no eixo Y
        color="#f44336",         # Cor das barras (vermelha)
        width=0.2                # Largura das barras (mais fino)
    )
    plt.title("Despesas por Categoria")
    plt.xlabel("Categoria")
    plt.ylabel("Total (€)")
    plt.grid(axis='y', linestyle='--', alpha=0.3)
    plt.tight_layout()
    plt.show()
