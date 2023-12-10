# Importando tk ---
# Importando scrolledtext para posicionar o bloco de notas ---
# Importanfo colorchooser para diversificar as cores ---

from tkinter import *
import tkinter as tk
from tkinter import colorchooser
from tkinter import scrolledtext


# Criando e configurando janela tk ---
janela = Tk()
janela.title('Bloco de notas .py')
janela.geometry('600x400')
janela.config(bg='#bce3cc')
janela.resizable(width=True, height=True)
janela.iconphoto(False, PhotoImage(file='3907595-200.png'))


# Criando funções ---
def iniciar_bloco_de_notas():
    iniciar_bloco = scrolledtext.ScrolledText(janela, wrap=tk.WORD)
    iniciar_bloco.grid()

def sair_da_aplicacao():
    quit()

def mudar_cores():
    cor_escolhida = colorchooser.askcolor()[1]
    janela.config(bg=cor_escolhida)
    
