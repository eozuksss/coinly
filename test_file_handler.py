import os  # Importa o módulo os para manipulação de ficheiros (verificar e apagar)
import file_handler  # Importa o módulo responsável por exportar/importar dados
import database  # Importa o módulo que interage com o banco de dados

def test_exportar_csv():
    caminho = "test_export_receitas.csv"  # Define o nome do ficheiro de teste
    database.inserir_receita(99.99, "Salário")  # Insere uma receita fictícia
    file_handler.exportar_para_csv("receitas", caminho)  # Exporta para CSV
    assert os.path.exists(caminho)  # Verifica se o ficheiro foi criado com sucesso
    os.remove(caminho)  # Remove o ficheiro após o teste para manter o ambiente limpo

def test_exportar_json():
    caminho = "test_export_receitas.json"  # Define o nome do ficheiro de teste
    file_handler.exportar_para_json("receitas", caminho)  # Exporta as receitas para JSON
    assert os.path.exists(caminho)  # Verifica se o ficheiro foi criado corretamente
    os.remove(caminho)  # Apaga o ficheiro para não deixar lixo no sistema

def test_importar_csv():
    caminho = "test_import_receitas.csv"  # Define o nome do ficheiro temporário para importação
    with open(caminho, "w", encoding="utf-8") as f:  # Cria e abre o ficheiro para escrita
        f.write("valor,categoria\n")  # Escreve o cabeçalho do CSV
        f.write("55.55,Outros\n")  # Adiciona uma linha de dados fictícios
    file_handler.importar_de_csv("receitas", caminho)  # Importa os dados do CSV para o banco
    receitas = database.listar_receitas()  # Lê todas as receitas atuais do banco
    assert any(v == 55.55 and c == "Outros" for v, c in receitas)  # Verifica se a receita foi realmente importada
    os.remove(caminho)  # Remove o ficheiro CSV após o teste
