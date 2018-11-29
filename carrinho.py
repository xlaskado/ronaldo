#autoria Marconi Maia
from tkinter import *
from tkinter import Tk
class Carrinho(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title('Tela')
        self.geometry('350x350+175+175')
        self.transient(parent)
        self.grab_set()
        self.title('Especificações Carro')
        self.config(background='yellow')
        Label(self, text='Chevrolet Chevette 79\nFicha Técnica:\n Ano=1979\nPlaca=ABC-1234\nModelo=Chevette\nCor=Laranja').grid(row=0, column=2, padx=20, pady=10)