#autoria Marconi Maia
from tkinter import *
from venda import Venda
from tkinter import messagebox
class Janela_do_Comprador(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title('Janela do Comprador')
        self.geometry('500x500+200+200')
        self.transient(parent)
        self.grab_set()
        Label(self, text='').grid(row=0, column=0, padx=20, pady=10)
        Label(self, text='').grid(row=0, column=0, padx=20, pady=10)
        Label(self, text='').grid(row=0, column=0, padx=20, pady=10)
        self.btn_close = Button(self, text='Sair Janela', command=self.destroy, width=10)
        self.btn_close.grid(row=8, column=1, columnspan=3, stick=S, pady=20)
        self.btn_venda = Button(self,width=25,text='Forma de Pagamento',command=self.venda)
        self.btn_venda.place(x=220,y=130)
        self.entry_nome_var = StringVar()
        self.entry_nome = Entry(self, textvariable=self.entry_nome_var).grid(row=1, column=3, padx=1, pady=1)
        self.lbl_nome = Label(self, text='Nome:').grid(row=1, column=1, padx=1, pady=1)
        self.entry_cpf_var = StringVar()
        self.entry_cpf = Entry(self, textvariable=self.entry_cpf_var).grid(row=2, column=3, padx=1, pady=1)
        self.lbl_cpf = Label(self, text='CPF:').grid(row=2, column=1, padx=1, pady=1)
        self.entry_cpf_var2 = StringVar()
        self.entry_cpf2 = Entry(self, textvariable=self.entry_cpf_var2).grid(row=6, column=3, padx=1, pady=1, stick=S)
        self.lbl_cpf2 = Label(self, text='Nome do Vendedor:').grid(row=6, column=1, padx=1, pady=1, stick=S)
    def destroy(self):
        if messagebox.askokcancel('Sair', 'Deseja Sair?'):
            super().destroy()
    def venda(self):
        Venda(self)