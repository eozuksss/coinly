import pytest  # Importa o framework de testes pytest
import database  # Importa o módulo database com as funções a testar

# ======================== TESTES RECEITAS ========================
def test_inserir_receita():
    database.inserir_receita(1000.0, "Salário")  # Insere uma nova receita
    receitas = database.listar_receitas()  # Obtém todas as receitas
    assert (1000.0, "Salário") in receitas  # Verifica se a receita foi inserida

def test_editar_receita():
    database.editar_receita(1000.0, "Salário", 1200.0, "Investimento")  # Edita a receita existente
    receitas = database.listar_receitas()  # Obtém as receitas atualizadas
    assert (1200.0, "Investimento") in receitas  # Verifica se a receita foi alterada

def test_remover_receita():
    database.remover_receita(1200.0, "Investimento")  # Remove a receita específica
    receitas = database.listar_receitas()  # Obtém a lista após remoção
    assert (1200.0, "Investimento") not in receitas  # Verifica se foi removida

# ======================== TESTES DESPESAS ========================
def test_inserir_despesa():
    database.inserir_despesa(250.0, "Alimentação")  # Insere uma nova despesa
    despesas = database.listar_despesas()  # Obtém todas as despesas
    assert (250.0, "Alimentação") in despesas  # Verifica se a despesa foi inserida

def test_editar_despesa():
    database.editar_despesa(250.0, "Alimentação", 300.0, "Transporte")  # Edita a despesa existente
    despesas = database.listar_despesas()  # Obtém as despesas atualizadas
    assert (300.0, "Transporte") in despesas  # Verifica se a despesa foi alterada

def test_remover_despesa():
    database.remover_despesa(300.0, "Transporte")  # Remove a despesa específica
    despesas = database.listar_despesas()  # Obtém a lista após remoção
    assert (300.0, "Transporte") not in despesas  # Verifica se foi removida
