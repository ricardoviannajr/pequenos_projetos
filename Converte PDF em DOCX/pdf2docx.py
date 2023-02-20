import tkinter as tk
from tkinter import filedialog
import aspose.words as aw
import os

# Cria uma janela para escolher o arquivo de entrada
root = tk.Tk()
root.withdraw()
nome_entrada = filedialog.askopenfilename(
    title="Escolha o arquivo PDF de entrada")

# Solicita o nome do arquivo de saída
nome_saida = input("Digite o nome do arquivo DOCX de saída: ")

# Abre o arquivo de entrada e salva como DOCX
doc = aw.Document(nome_entrada)
nome_base = os.path.splitext(nome_entrada)[0]
doc.save(nome_base + ".docx")
