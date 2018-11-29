#autoria Marconi Maia
from tkinter import *
from tkinter import messagebox
import time
class Janela_Vendedor(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title('Janela do Vendedor')
        self.geometry('500x500+200+200')
        self.transient(parent)
        self.grab_set()
        Label(self, text='').grid(row=0, column=0, padx=20, pady=10)
        Label(self, text='').grid(row=0, column=0, padx=20, pady=10)
        Label(self, text='').grid(row=0, column=0, padx=20, pady=10)
        self.btn_close = Button(self, text='Sair Janela', command=self.destroy, width=10)
        self.btn_close.grid(row=8, column=1, columnspan=3, stick=S, pady=20)
        self.entry_nome_var = StringVar()
        self.entry_nome = Entry(self, textvariable=self.entry_nome_var).grid(row=1, column=3, padx=1, pady=1)
        self.lbl_nome = Label(self, text='Nome do Vendedor:').grid(row=1, column=1, padx=1, pady=1)
        self.entry_cpf_var = StringVar()
        self.entry_cpf = Entry(self, textvariable=self.entry_cpf_var).grid(row=2, column=3, padx=1, pady=1)
        self.lbl_cpf = Label(self, text='CPF:').grid(row=2, column=1, padx=1, pady=1)
        self.entry_cpf_var2 = StringVar()
        self.entry_cpf2 = Entry(self, textvariable=self.entry_cpf_var2).grid(row=6, column=3, padx=1, pady=1, stick=S)
        self.lbl_cpf2 = Label(self, text='Matricula do Vendedor:').grid(row=6, column=1, padx=1, pady=1, stick=S)
        self.btn_16 = Button(self,width=10,text='Comfirma',command=self.destroy())
        self.btn_16.place(x=230,y=130)
    def destroy(self):
        time.sleep(2)
        if messagebox.askokcancel('Sair', 'Deseja Sair?'):
            super().destroy()
            # autoria Marconi Maia