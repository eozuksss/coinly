# Importa o módulo mysql.connector, necessário para conectar e interagir com um banco de dados MySQL
import mysql.connector

# Importa a classe Error para tratamento de exceções específicas do MySQL
from mysql.connector import Error

# Define a função 'conectar' que tenta estabelecer uma conexão com o banco de dados MySQL
def conectar():
    try:
        # Tenta criar uma conexão com o banco de dados usando as credenciais e nome da base
        conexao = mysql.connector.connect(
            host='localhost',          # Nome do servidor onde o MySQL está a correr (localhost = computador local)
            user='root',               # Nome do utilizador do MySQL
            password='Tiago123$',      # Senha do utilizador do MySQL
            database='gestao_financeira'  # Nome do banco de dados ao qual se deseja conectar
        )
        return conexao  # Se a conexão for bem-sucedida, retorna o objeto de conexão
    except Error as e:
        # Em caso de erro, exibe uma mensagem explicando o que ocorreu
        print(f"Erro ao conectar ao MySQL: {e}")
        return None  # Retorna None se não conseguir conectar

# -------------------------
# FUNÇÕES RELACIONADAS A RECEITAS
# -------------------------

# Função para inserir uma nova receita no banco de dados
def inserir_receita(valor, categoria):
    conexao = conectar()  # Tenta conectar ao banco
    if conexao:  # Se a conexão foi bem-sucedida
        cursor = conexao.cursor()  # Cria um cursor para executar comandos SQL
        # Prepara o comando SQL para inserir os valores na tabela 'receitas'
        query = "INSERT INTO receitas (valor, categoria) VALUES (%s, %s)"
        # Executa o comando com os valores fornecidos como argumentos
        cursor.execute(query, (valor, categoria))
        conexao.commit()  # Salva as alterações no banco
        cursor.close()  # Fecha o cursor
        conexao.close()  # Fecha a conexão com o banco

# Função para listar todas as receitas armazenadas
def listar_receitas():
    conexao = conectar()  # Conecta ao banco
    if conexao:
        cursor = conexao.cursor()  # Cria o cursor
        # Executa uma query que seleciona os dados da tabela 'receitas'
        cursor.execute("SELECT valor, categoria FROM receitas")
        resultados = cursor.fetchall()  # Obtém todos os resultados da query
        cursor.close()  # Fecha o cursor
        conexao.close()  # Fecha a conexão
        return resultados  # Retorna os resultados como uma lista de tuplas
    return []  # Se a conexão falhar, retorna uma lista vazia

# Função para editar (atualizar) uma receita existente
def editar_receita(valor_antigo, categoria_antiga, novo_valor, nova_categoria):
    conexao = conectar()  # Conecta ao banco
    if conexao:
        cursor = conexao.cursor()  # Cria o cursor
        # Atualiza uma linha na tabela 'receitas' onde o valor e categoria correspondem
        # ABS(valor - %s) < 0.01 é usado para evitar problemas com precisão de float
        query = "UPDATE receitas SET valor = %s, categoria = %s WHERE ABS(valor - %s) < 0.01 AND categoria = %s"
        cursor.execute(query, (novo_valor, nova_categoria, valor_antigo, categoria_antiga))
        conexao.commit()  # Salva a alteração no banco
        cursor.close()  # Fecha o cursor
        conexao.close()  # Fecha a conexão

# Função para remover uma receita específica
def remover_receita(valor, categoria):
    conexao = conectar()  # Conecta ao banco
    if conexao:
        cursor = conexao.cursor()  # Cria o cursor
        # Comando SQL para apagar uma linha da tabela 'receitas' com valor e categoria específicos
        query = "DELETE FROM receitas WHERE ABS(valor - %s) < 0.01 AND categoria = %s"
        cursor.execute(query, (valor, categoria))  # Executa o comando
        conexao.commit()  # Aplica a alteração no banco
        cursor.close()  # Fecha o cursor
        conexao.close()  # Fecha a conexão

# -------------------------
# FUNÇÕES RELACIONADAS A DESPESAS
# -------------------------

# Função para inserir uma nova despesa
def inserir_despesa(valor, categoria):
    conexao = conectar()  # Conecta ao banco
    if conexao:
        cursor = conexao.cursor()  # Cria o cursor
        # Comando SQL para inserir dados na tabela 'despesas'
        query = "INSERT INTO despesas (valor, categoria) VALUES (%s, %s)"
        cursor.execute(query, (valor, categoria))  # Executa a inserção
        conexao.commit()  # Salva no banco
        cursor.close()  # Fecha o cursor
        conexao.close()  # Fecha a conexão

# Função para listar todas as despesas
def listar_despesas():
    conexao = conectar()  # Conecta ao banco
    if conexao:
        cursor = conexao.cursor()  # Cria o cursor
        # Comando SQL para selecionar todas as despesas
        cursor.execute("SELECT valor, categoria FROM despesas")
        resultados = cursor.fetchall()  # Recupera todos os registros encontrados
        cursor.close()  # Fecha o cursor
        conexao.close()  # Fecha a conexão
        return resultados  # Retorna a lista de tuplas com os dados
    return []  # Se não conseguir conectar, retorna lista vazia

# Função para editar uma despesa existente
def editar_despesa(valor_antigo, categoria_antiga, novo_valor, nova_categoria):
    conexao = conectar()  # Conecta ao banco
    if conexao:
        cursor = conexao.cursor()  # Cria o cursor
        # Atualiza uma linha específica na tabela 'despesas'
        query = "UPDATE despesas SET valor = %s, categoria = %s WHERE ABS(valor - %s) < 0.01 AND categoria = %s"
        cursor.execute(query, (novo_valor, nova_categoria, valor_antigo, categoria_antiga))
        conexao.commit()  # Aplica a alteração
        cursor.close()  # Fecha o cursor
        conexao.close()  # Fecha a conexão

# Função para remover uma despesa
def remover_despesa(valor, categoria):
    conexao = conectar()  # Conecta ao banco
    if conexao:
        cursor = conexao.cursor()  # Cria o cursor
        # Comando para remover a despesa correspondente
        query = "DELETE FROM despesas WHERE ABS(valor - %s) < 0.01 AND categoria = %s"
        cursor.execute(query, (valor, categoria))  # Executa a exclusão
        conexao.commit()  # Salva as alterações
        cursor.close()  # Fecha o cursor
        conexao.close()  # Fecha a conexão
