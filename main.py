
# Importação da biblioteca principal para construção da interface gráfica
import tkinter as tk  # 'tk' será usado como prefixo para todos os widgets

# Importação de widgets modernos (ttk) e da caixa de mensagens (messagebox)
from tkinter import ttk, messagebox

# Importação do módulo que contém funções de acesso ao banco de dados (inserir, listar, editar, remover)
import database

# Importação do módulo que gera os gráficos de receitas e despesas usando Matplotlib
import charts

# Importa a função que abre a janela de importação/exportação de ficheiros (csv/json)
from ficheiros_ui import abrir_ficheiros


# Estilo visual usado em todos os botões da aplicação
BTN_STYLE = {
    "font": ("Arial", 10, "bold"),        # Fonte em negrito para melhor destaque
    "bg": "#2e8b57",                      # Verde escuro (tom 'seagreen')
    "fg": "white",                        # Texto branco para melhor contraste
    "activebackground": "#3cb371",       # Verde claro ao pressionar (mais suave)
    "activeforeground": "white",         # Mantém texto branco ao pressionar
    "relief": "groove",                  # Borda mais suave que 'ridge'
    "bd": 2,                              # Borda mais fina e discreta
    "highlightthickness": 0,             # Remove a linha de foco
    "cursor": "hand2"                    # Muda o cursor para uma mãozinha ao passar o mouse
}

# Estilo dos rótulos usados em campos
LABEL_STYLE = {"font": ("Arial", 12)}  # Fonte usada em rótulos como "Valor", "Categoria"

# Estilo dos títulos principais das janelas
TITLE_STYLE = {"font": ("Arial", 14, "bold")}  # Fonte maior e em negrito para títulos


# ======================== JANELA DE GRÁFICOS ========================
def abrir_graficos():
    # Cria uma nova janela (filha da janela principal)
    janela = tk.Toplevel()
    # Define o título da janela
    janela.title("Gráficos Financeiros")
    # Define as dimensões da janela: largura x altura
    janela.geometry("300x150")
    # Define a cor de fundo da janela
    janela.config(bg="#f0f0f0")
    # Título da seção, exibido no topo da janela
    tk.Label(janela, text="Gráficos", **TITLE_STYLE, bg="#f0f0f0").pack(pady=10)

    # Botão que chama a função de gerar gráfico de receitas
    tk.Button(janela, text="📈 Receitas", command=charts.gerar_grafico_receitas, width=20, **BTN_STYLE).pack(pady=5)

    # Botão que chama a função de gerar gráfico de despesas
    tk.Button(janela, text="📉 Despesas", command=charts.gerar_grafico_despesas, width=20, **BTN_STYLE).pack(pady=5)

# ======================== JANELA DE RECEITAS ========================
def abrir_receitas():
    # Cria nova janela separada para gerenciar as receitas
    janela = tk.Toplevel()
    janela.title("Gerenciar Receitas")  # Título da janela
    janela.geometry("520x420")          # Define o tamanho da janela
    janela.config(bg="#fdfdfd")         # Cor de fundo clara

    # Adiciona o título da seção no topo da janela
    tk.Label(janela, text="Receitas", **TITLE_STYLE, bg="#fdfdfd").pack(pady=10)

    # Frame para agrupar os campos de entrada
    frame = tk.Frame(janela, bg="#fdfdfd")
    frame.pack(pady=5)

    # Campo de entrada para o valor da receita
    tk.Label(frame, text="Valor:", **LABEL_STYLE, bg="#fdfdfd").grid(row=0, column=0, padx=5)
    entry_valor = tk.Entry(frame)
    entry_valor.grid(row=0, column=1, padx=5)

    # Campo de entrada para a categoria da receita
    tk.Label(frame, text="Categoria:", **LABEL_STYLE, bg="#fdfdfd").grid(row=0, column=2, padx=5)
    categoria_var = tk.StringVar()  # Variável para armazenar a categoria selecionada
    combo = ttk.Combobox(frame, textvariable=categoria_var, state="readonly")  # Combobox com categorias fixas
    combo["values"] = ("Salário", "Investimento", "Outros")  # Valores disponíveis para seleção
    combo.grid(row=0, column=3, padx=5)

    # Função para atualizar os dados exibidos na tabela
    def atualizar_tabela():
        for i in tree.get_children():  # Remove dados antigos
            tree.delete(i)
        for item in database.listar_receitas():  # Lista as receitas do banco
            tree.insert("", "end", values=item)

    # Função para adicionar nova receita
    def adicionar():
        try:
            valor = float(entry_valor.get())  # Converte o valor para float
            categoria = categoria_var.get()
            if categoria:  # Verifica se foi escolhida uma categoria
                database.inserir_receita(valor, categoria)  # Insere no banco
                atualizar_tabela()  # Atualiza a tabela
                entry_valor.delete(0, tk.END)
                combo.set("")  # Limpa os campos
            else:
                messagebox.showwarning("Aviso", "Escolha uma categoria.")
        except ValueError:
            messagebox.showerror("Erro", "Insira um valor numérico.")

    # Função para editar a receita selecionada
    def editar():
        selecionado = tree.focus()  # Obtém a linha selecionada
        if selecionado:
            antigo_valor, antiga_categoria = tree.item(selecionado)["values"]
            try:
                novo_valor = float(entry_valor.get())
                nova_categoria = categoria_var.get()
                if nova_categoria:
                    database.editar_receita(antigo_valor, antiga_categoria, novo_valor, nova_categoria)
                    atualizar_tabela()
                    entry_valor.delete(0, tk.END)
                    combo.set("")
                else:
                    messagebox.showwarning("Aviso", "Escolha uma nova categoria.")
            except ValueError:
                messagebox.showerror("Erro", "Insira um valor válido.")
        else:
            messagebox.showinfo("Info", "Selecione uma receita para editar.")

    # Função para remover receita selecionada
    def remover():
        selecionado = tree.focus()
        if selecionado:
            valor, categoria = tree.item(selecionado)["values"]
            database.remover_receita(valor, categoria)
            atualizar_tabela()
        else:
            messagebox.showinfo("Info", "Selecione uma receita para remover.")

    # Frame que contém os botões de ação
    botoes = tk.Frame(janela, bg="#fdfdfd")
    botoes.pack(pady=10)

    # Botões para adicionar, editar e remover receitas
    tk.Button(botoes, text="Adicionar", command=adicionar, **BTN_STYLE).grid(row=0, column=0, padx=5)
    tk.Button(botoes, text="Editar", command=editar, **BTN_STYLE).grid(row=0, column=1, padx=5)
    tk.Button(botoes, text="Remover", command=remover, **BTN_STYLE).grid(row=0, column=2, padx=5)

    # Tabela para exibir as receitas registradas
    tree = ttk.Treeview(janela, columns=("Valor", "Categoria"), show="headings")
    for col in ("Valor", "Categoria"):
        tree.heading(col, text=col)
        tree.column(col, width=200)
    tree.pack(pady=10)

    atualizar_tabela()  # Inicializa com os dados atuais do banco

# ======================== JANELA DE DESPESAS ========================
def abrir_despesas():
    janela = tk.Toplevel()  # Cria nova janela para despesas
    janela.title("Gerenciar Despesas")
    janela.geometry("520x420")
    janela.config(bg="#fdfdfd")

    tk.Label(janela, text="Despesas", **TITLE_STYLE, bg="#fdfdfd").pack(pady=10)

    frame = tk.Frame(janela, bg="#fdfdfd")
    frame.pack(pady=5)

    tk.Label(frame, text="Valor:", **LABEL_STYLE, bg="#fdfdfd").grid(row=0, column=0, padx=5)
    entry_valor = tk.Entry(frame)
    entry_valor.grid(row=0, column=1, padx=5)

    tk.Label(frame, text="Categoria:", **LABEL_STYLE, bg="#fdfdfd").grid(row=0, column=2, padx=5)
    categoria_var = tk.StringVar()
    combo = ttk.Combobox(frame, textvariable=categoria_var, state="readonly")
    combo["values"] = ("Alimentação", "Transporte", "Moradia", "Lazer", "Outros")
    combo.grid(row=0, column=3, padx=5)

    def atualizar_tabela():
        for i in tree.get_children():
            tree.delete(i)
        for item in database.listar_despesas():
            tree.insert("", "end", values=item)

    def adicionar():
        try:
            valor = float(entry_valor.get())
            categoria = categoria_var.get()
            if categoria:
                database.inserir_despesa(valor, categoria)
                atualizar_tabela()
                entry_valor.delete(0, tk.END)
                combo.set("")
            else:
                messagebox.showwarning("Aviso", "Escolha uma categoria.")
        except ValueError:
            messagebox.showerror("Erro", "Insira um valor numérico.")

    def editar():
        selecionado = tree.focus()
        if selecionado:
            antigo_valor, antiga_categoria = tree.item(selecionado)["values"]
            try:
                novo_valor = float(entry_valor.get())
                nova_categoria = categoria_var.get()
                if nova_categoria:
                    database.editar_despesa(antigo_valor, antiga_categoria, novo_valor, nova_categoria)
                    atualizar_tabela()
                    entry_valor.delete(0, tk.END)
                    combo.set("")
                else:
                    messagebox.showwarning("Aviso", "Escolha uma nova categoria.")
            except ValueError:
                messagebox.showerror("Erro", "Insira um valor válido.")
        else:
            messagebox.showinfo("Info", "Selecione uma despesa para editar.")

    def remover():
        selecionado = tree.focus()
        if selecionado:
            valor, categoria = tree.item(selecionado)["values"]
            database.remover_despesa(valor, categoria)
            atualizar_tabela()
        else:
            messagebox.showinfo("Info", "Selecione uma despesa para remover.")

    botoes = tk.Frame(janela, bg="#fdfdfd")
    botoes.pack(pady=10)
    tk.Button(botoes, text="Adicionar", command=adicionar, **BTN_STYLE).grid(row=0, column=0, padx=5)
    tk.Button(botoes, text="Editar", command=editar, **BTN_STYLE).grid(row=0, column=1, padx=5)
    tk.Button(botoes, text="Remover", command=remover, **BTN_STYLE).grid(row=0, column=2, padx=5)

    tree = ttk.Treeview(janela, columns=("Valor", "Categoria"), show="headings")
    for col in ("Valor", "Categoria"):
        tree.heading(col, text=col)
        tree.column(col, width=200)
    tree.pack(pady=10)

    atualizar_tabela()


# ======================== JANELA PRINCIPAL ========================
def main():
    root = tk.Tk()  # Cria a janela principal do programa
    root.title("Gestão Financeira - Coinly")  # Título da aplicação
    root.geometry("320x330")  # Define tamanho da janela
    root.config(bg="#f0f8ff")  # Cor de fundo da janela principal

    # Título de boas-vindas
    tk.Label(root, text="Bem-vindo ao Coinly!", **TITLE_STYLE, bg="#f0f8ff").pack(pady=20)

    # Botões que abrem as diferentes janelas/funções
    tk.Button(root, text="Receitas", width=25, command=abrir_receitas, **BTN_STYLE).pack(pady=6)
    tk.Button(root, text="Despesas", width=25, command=abrir_despesas, **BTN_STYLE).pack(pady=6)
    tk.Button(root, text="Gráficos", width=25, command=abrir_graficos, **BTN_STYLE).pack(pady=6)
    tk.Button(root, text="Ficheiros", width=25, command=abrir_ficheiros, **BTN_STYLE).pack(pady=6)
    tk.Button(root, text="Sair", width=25, command=root.destroy, **BTN_STYLE).pack(pady=20)

    root.mainloop()  # Mantém a janela aberta e responde a eventos (loop principal)

# Se o script for executado diretamente, chama a função main()
if __name__ == "__main__":
    main()
