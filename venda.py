#autoria Marconi Maia
from tkinter import *
from pagamento import Pagamento
from tkinter import messagebox
import time
class Venda(Toplevel):
    time.sleep(3)
    def __init__(self, parent):
        super().__init__(parent)
        self.title('Janela do Comprador')
        self.geometry('500x500+200+200')
        self.transient(parent)
        self.grab_set()
        self.config(background='green')
        ##
        Label(self, text='').grid(row=0, column=0, padx=20, pady=10)
        Label(self, text='').grid(row=0, column=0, padx=20, pady=10)
        Label(self, text='').grid(row=0, column=0, padx=20, pady=10)
        Label(self, text='').grid(row=0, column=0, padx=20, pady=10)
        Label(self, text='').grid(row=0, column=0, padx=20, pady=10)
        Label(self, text='').grid(row=0, column=0, padx=20, pady=10)
        ##
        self.entry_numero_var = StringVar()
        self.entry_numero = Entry(self, textvariable=self.entry_numero_var).grid(row=1, column=3, padx=1, pady=1)
        self.lbl_numero = Label(self, text='Numero do Cartão:').grid(row=1, column=1, padx=1, pady=1)
        ##
        self.entry_nome_var = StringVar()
        self.entry_nome = Entry(self, textvariable=self.entry_nome_var).grid(row=2, column=3, padx=1, pady=1)
        self.lbl_nome = Label(self, text='Nome do Portador do cartão:').grid(row=2, column=1, padx=1, pady=1)
        ##
        self.entry_paga_var = StringVar()
        self.entry_paga = Entry(self, textvariable=self.entry_paga_var).grid(row=3, column=3, padx=1, pady=1)
        self.lbl_paga = Label(self, text='Codigo de Segurança do Cartão:').grid(row=3, column=1, padx=1, pady=1)
        ##
        self.entry_paga1_var = StringVar()
        self.entry_paga1 = Entry(self, textvariable=self.entry_paga1_var).grid(row=4, column=3, padx=1, pady=1)
        self.lbl_paga1 = Label(self, text='CPF Cadastrado:').grid(row=4, column=1, padx=1, pady=1)
        ##
        self.entry_paga2_var = StringVar()
        self.entry_paga2 = Entry(self, textvariable=self.entry_paga2_var).grid(row=5, column=3, padx=1, pady=1)
        self.lbl_paga2 = Label(self, text='Validade do Cartão:').grid(row=5, column=1, padx=1, pady=1)
        ##
        self.entry_paga3_var = StringVar()
        self.entry_paga3 = Entry(self, textvariable=self.entry_paga3_var).grid(row=6, column=3, padx=1, pady=1)
        self.lbl_paga3 = Label(self, text='Operação:').grid(row=6, column=1, padx=1, pady=1)
        ##
        self.btn_12 = Button(self,width=10,text='Cancelar',command=self.destroy())
        self.btn_12.place(x=80,y=200)
        ##
        self.btn_13 = Button(self, width=25, text='Forma de Pagamento',command=self.teste12())
        self.btn_13.place(x=180, y=200)
        ##
    def destroy(self):
        if messagebox.askokcancel('Sair', 'Deseja Sair?'):
            super().destroy()
    def teste12(self):
        Pagamento(self)

