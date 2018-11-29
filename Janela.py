#autoria Marconi Maia
from tkinter import *
from tkinter import Tk
from tkinter import messagebox
from Janela_do_Comprador import Janela_do_Comprador
from carrinho import Carrinho
from vendedor import Janela_Vendedor
class Janela(Tk):
    def __init__(self):
        super().__init__()
        self.geometry('500x500+200+200')
        self.config(background='blue')
        self.title('Janela Principal')
        self.btn_close = Button(self, width=10, text='Sair', command=self.destroy)
        self.btn_ok = Button(self, width=10, text='ok', command=self.btn_ok_click)
        self.txt_ok = Entry(self, width=45)
        self.btn1_car = Button(self,width=25,text='Chevrolet Chevette 79',command=self.car1)
        self.btn_car = Button(self,width=10,text='ABC-1234',command=self.car)
        self.btn_search = Button(self,width=10,text='Pesquisar')
        self.btn_comfirma = Button(self,width=25,text='Clique na placa para comprar')
        self.btn_vendedor = Button(self,width=10,text='Vendedor',command=self.venda123)
        self.btn_vendedor.place(x=10,y=40)
        self.btn_comfirma.place(x=135,y=150)
        self.btn_close.place(x=10, y=450)
        self.btn_car.place(x=50,y=150)
        self.btn1_car.place(x=50,y=115)
        self.btn_ok.place(x=100, y=450)
        self.btn_search.place(x=10, y=10)
        self.txt_ok.place(x=100, y=10)
    def destroy(self):
        if messagebox.askokcancel('Sair', 'Deseja Sair?'):
            super().destroy()
    def btn_ok_click(self):
        self.lbl_ok['text'] = self.txt_ok.get()
    def car1(self):
        Carrinho(self)
    def car(self):
        Janela_do_Comprador(self)
    def venda123(self):
        Janela_Vendedor(self)
