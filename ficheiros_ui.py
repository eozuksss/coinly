# Importa o módulo tkinter para criar interfaces gráficas
import tkinter as tk

# Importa funcionalidades adicionais do tkinter para diálogos de arquivos e mensagens
from tkinter import filedialog, messagebox

# Importa o módulo personalizado responsável por lidar com leitura/escrita de ficheiros
import file_handler

# Define a função que cria uma nova janela para importar e exportar ficheiros
def abrir_ficheiros():
    # Cria uma nova janela (janela filha) sobre a principal
    janela = tk.Toplevel()
    janela.title("Importar / Exportar Dados")  # Define o título da janela
    janela.geometry("380x360")  # Define o tamanho da janela
    janela.config(bg="#f8f8f8")  # Define a cor de fundo da janela

    # Função interna para exportar dados (receitas ou despesas) em formato CSV ou JSON
    def exportar(tipo, formato):
        # Define a extensão com base no formato selecionado
        ext = "csv" if formato == "csv" else "json"

        # Abre uma caixa de diálogo para o utilizador escolher onde salvar o arquivo
        caminho = filedialog.asksaveasfilename(
            defaultextension=f".{ext}",  # Extensão padrão
            filetypes=[(f"{ext.upper()} files", f"*.{ext}")]  # Tipo de ficheiro a mostrar
        )

        # Se o utilizador escolheu um caminho válido
        if caminho:
            try:
                # Chama a função apropriada para exportar os dados, dependendo do formato
                if formato == "csv":
                    file_handler.exportar_para_csv(tipo, caminho)
                else:
                    file_handler.exportar_para_json(tipo, caminho)
                # Mostra uma mensagem de sucesso
                messagebox.showinfo("Sucesso", f"{tipo.capitalize()} exportadas para {caminho}")
            except Exception as e:
                # Em caso de erro, mostra uma mensagem com o erro ocorrido
                messagebox.showerror("Erro", str(e))

    # Função interna para importar dados (receitas ou despesas) de ficheiros CSV ou JSON
    def importar(tipo, formato):
        # Define os tipos de ficheiro aceitos com base no formato escolhido
        if formato == "csv":
            tipos_arquivo = [("CSV files", "*.csv")]
        else:
            tipos_arquivo = [("JSON files", "*.json")]

        # Abre uma caixa de diálogo para o utilizador escolher o ficheiro a importar
        caminho = filedialog.askopenfilename(filetypes=tipos_arquivo)

        # Se o utilizador escolheu um ficheiro
        if caminho:
            try:
                # Chama a função apropriada para importar os dados
                if formato == "csv":
                    file_handler.importar_de_csv(tipo, caminho)
                else:
                    file_handler.importar_de_json(tipo, caminho)
                # Mostra uma mensagem de sucesso
                messagebox.showinfo("Sucesso", f"{tipo.capitalize()} importadas de {caminho}")
            except Exception as e:
                # Em caso de erro, exibe uma mensagem com a descrição do erro
                messagebox.showerror("Erro", str(e))

    # --- INTERFACE VISUAL ---

    # Título da secção de exportação
    tk.Label(janela, text="Exportar dados", font=("Arial", 12, "bold"), bg="#f8f8f8").pack(pady=10)

    # Botões para exportar receitas e despesas em CSV ou JSON
    tk.Button(janela, text="Exportar Receitas (.csv)", width=30,
              command=lambda: exportar("receitas", "csv")).pack(pady=2)

    tk.Button(janela, text="Exportar Receitas (.json)", width=30,
              command=lambda: exportar("receitas", "json")).pack(pady=2)

    tk.Button(janela, text="Exportar Despesas (.csv)", width=30,
              command=lambda: exportar("despesas", "csv")).pack(pady=2)

    tk.Button(janela, text="Exportar Despesas (.json)", width=30,
              command=lambda: exportar("despesas", "json")).pack(pady=2)

    # Título da secção de importação
    tk.Label(janela, text="Importar dados", font=("Arial", 12, "bold"), bg="#f8f8f8").pack(pady=10)

    # Botões para importar receitas e despesas em CSV ou JSON
    tk.Button(janela, text="Importar Receitas (.csv)", width=30,
              command=lambda: importar("receitas", "csv")).pack(pady=2)

    tk.Button(janela, text="Importar Receitas (.json)", width=30,
              command=lambda: importar("receitas", "json")).pack(pady=2)

    tk.Button(janela, text="Importar Despesas (.csv)", width=30,
              command=lambda: importar("despesas", "csv")).pack(pady=2)

    tk.Button(janela, text="Importar Despesas (.json)", width=30,
              command=lambda: importar("despesas", "json")).pack(pady=2)
