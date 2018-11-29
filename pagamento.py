#autoria Marconi Maia
from tkinter import *
from randompy import *
from tkinter import messagebox
import time
class Pagamento(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title('Nota fiscal')
        self.geometry('500x500+200+200')
        self.transient(parent)
        self.grab_set()
        self.config(background='blue')
        self.lbl_numero = Label(self, text='Numero do Boleto:').grid(row=1, column=1, padx=1, pady=1)
        Label(self, text=random.randrange(2000000000,90000000000)).grid(row=1, column=2, padx=10, pady=15)
        self.lbl_numero2 = Label(self,text='Nome do Comprador:').grid(row=2,column=1,padx=1,pady=1)
        self.lbl_numero3 = Label(self, text='Joe Silva').grid(row=2, column=2, padx=5, pady=10)
        self.lbl_numero4 = Label(self,text='CPF do Comprador:').grid(row=3,column=1,padx=1,pady=1)
        self.lbl_numero5 = Label(self, text='123456789').grid(row=3, column=2, padx=5, pady=10)
        self.lbl_numero6 = Label(self, text='Nome do Vendedor:').grid(row=4, column=1, padx=1, pady=1)
        self.lbl_numero7 = Label(self, text='Ronaldo').grid(row=4, column=2, padx=5, pady=10)
        self.lbl_numero8 = Label(self, text='Registro do Vendedor:').grid(row=5, column=1, padx=1, pady=1)
        self.lbl_numero9 = Label(self, text='123456789').grid(row=5, column=2, padx=5, pady=10)
        self.lbl_numero10 = Label(self, text='Compra efetuada dia:').grid(row=6, column=1, padx=1, pady=1)
        self.lbl_numero11 = Label(self, text='01/01/2000').grid(row=6, column=2, padx=5, pady=10)
        self.lbl_numero12 = Label(self, text='Veiculo Comprado:').grid(row=7, column=1, padx=1, pady=1)
        self.lbl_numero13 = Label(self, text='Chevrolet Chevette 79 cor laranja').grid(row=7, column=2, padx=5, pady=10)
        self.lbl_numero14 = Label(self, text='Obrigado(a) pela preferência,volte sempre!!').grid(row=9, column=1, padx=1, pady=1)
        self.btn_1 = Button(self, width=25, text='Voltar a Pagina Inicial',command=self.destroy())
        self.btn_1.place(x=10,y=350)
    def destroy(self):
        time.sleep(1)
        if messagebox.askokcancel('Sair', 'Deseja Sair?'):
            super().destroy()



