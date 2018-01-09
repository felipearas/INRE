# Simple enough, just import everything from tkinter.
from tkinter import *

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import PhotoImage
from tkinter import StringVar

import sys
import os

import json

# Here, we are creating our class, Window, and inheriting from the Frame
# class. Frame is a class from the tkinter module. (see Lib/tkinter/__init__)
class Window(Frame):

    # Define settings upon initialization. Here you can specify
    def __init__(self, master=None):

        #reference to the master widget, which is the tk window                 
        self.master = master
        
        # parameters that you want to send through the Frame class. 
        Frame.__init__(self, self.master)
        
        #with that, we want to then run init_window, which doesn't yet exist
        self.init_window()

    #Creation of init_window
    def init_window(self):

        # changing the title of our master widget    
        self.master.title("INRE")

        # allowing the widget to take the full space of the root window
        self.grid()

        # creating a menu instance
        menu = Menu(self.master)
        self.master.config(menu=menu)

        # create the file object)
        file = Menu(menu)

        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit
        file.add_command(label="Exit", command=self.client_exit)

        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit

        #added "file" to our menu
        menu.add_cascade(label="File", menu=file)


        # create the file object)
        edit = Menu(menu)

        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit
        # edit.add_command(label="Show Img", command=self.showImg)
        edit.add_command(label="Serviços", command=self.showServicos)

        #added "file" to our menu
        menu.add_cascade(label="INRE", menu=edit)

        # create the file object)
        recic = Menu(menu)

        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit
        # edit.add_command(label="Show Img", command=self.showImg)
        recic.add_command(label="Cliente", command=self.showPreCliente)

        #added "file" to our menu
        menu.add_cascade(label="Pesquisa Interna", menu=recic)


    def client_exit(self):
        exit()

    def showServicos(self):

        self.master.destroy()

        self.__init__(master=None)

        label_1 = Label(self.master, text="INRE SERVIÇOS",font=fonteC)
        label_2 = Label(self.master, text=("Bem vindo, deseja executar qual dos serviços"),font=fonteC)
        button_2 = Button(self.master, width=35,pady = 10,text="Cadastrar cliente",command=lambda:self.showCadastro())
        button_3 = Button(self.master, width=35,pady = 10,text="Orçamento Recic-Lar",command=lambda:self.showReciclar())
        button_4 = Button(self.master, width=35,pady = 10,text="Orçamento Retirada PF",command=lambda:fef())
        button_5 = Button(self.master, width=35,pady = 10,text="Orçamento Retirada PJ",command=lambda:fe())
        label_1.grid(row=0,column=0,pady=10,padx=25)
        label_2.grid(row=1,column=0,pady=10,padx=25)
        button_2.grid()
        button_3.grid()
        button_4.grid()
        button_5.grid()

    def showCadastro(self):

        self.master.destroy()

        self.__init__(master=None)

        self.showCode()

        Label(self.master,text="Cadastro de cliente para o banco de dados",font=fonteC).grid(row=0,column=0)

        Label(self.master,text=code).grid(row=3,column=2)

        self.code = code

        self.nome=Entry(self.master)
        self.nome.grid(row=4, column=2)

        self.cpf=Entry(self.master)
        self.cpf.grid(row=5, column=2)

        self.rg=Entry(self.master)
        self.rg.grid(row=6, column=2)

        self.mail=Entry(self.master)
        self.mail.grid(row=7, column=2)

        self.tel=Entry(self.master)
        self.tel.grid(row=8, column=2)

        self.end=Entry(self.master)
        self.end.grid(row=9, column=2)

        self.cep=Entry(self.master)
        self.cep.grid(row=10, column=2)

        self.bairro = Entry(self.master)
        self.bairro.grid(row=11,column=2)

        self.cid=Entry(self.master)
        self.cid.grid(row=12, column=2)

        self.uf = Entry(self.master)
        self.uf.grid(row=13,column=2)

        self.usuario =Entry(self.master)
        self.usuario.grid(row=14,column=2)

        self.contact =Entry(self.master)
        self.contact.grid(row=15,column=2)

        frase1 = Label(self.master, text="Dados do cliente")
        frase1.grid(row=2 , column=2)

        frase0 = Label(self.master,text="Identificação - Código Cliente")
        frase0.grid(row=3,column=0)

        frase2 = Label(self.master, text="Nome do cliente")
        frase2.grid(row=4, column=0)

        frase4 = Label(self.master, text="CPF")
        frase4.grid(row=5 , column=0)

        frase3 = Label(self.master, text="RG")
        frase3.grid(row=6 , column=0)

        frase5 = Label(self.master, text="E-mail")
        frase5.grid(row=7 , column=0)

        frase10 = Label(self.master, text="Contato Telefone/Celular")
        frase10.grid(row=8 , column=0)

        frase20 = Label(self.master, text="Endereço")
        frase20.grid(row=9, column=0)

        frase30 = Label(self.master, text="CEP")
        frase30.grid(row=10 , column=0)

        frase40 = Label(self.master, text="Bairro")
        frase40.grid(row=11 , column=0)

        frase60 = Label(self.master,text="Cidade")
        frase60.grid(row=12,column=0)

        frase50 = Label(self.master, text="UF")
        frase50.grid(row=13 , column=0)

        fraseU = Label(self.master, text="Usuário INRE")
        fraseU.grid(row=14,column=0)

        frasec = Label(self.master, text="Forma de contato")
        frasec.grid(row=15,column=0)

        butt = Button(self.master,text="Salvar dados",command=self.showGet)
        butt.grid(row=16, column=2)

        butt_2 = Button(self.master,text="Concluir e voltar a tela dos serviços",command=self.showServicos)
        butt_2.grid(row=17,column=0)

    def showGet(self):

        salvos = Label(self.master,text="Os dados do cliente foram salvos com sucesso!",font=fonteA).grid(row=17,column=2)

        self.nome.real = self.nome.get()
        self.rg.real = self.rg.get()
        self.cpf.real = self.cpf.get()
        self.mail.real = self.mail.get()
        self.tel.real = self.tel.get()
        self.end.real = self.end.get()
        self.cep.real = self.cep.get()
        self.bairro.real = self.bairro.get()
        self.cid.real = self.cid.get()
        self.uf.real = self.uf.get()
        self.usuario.real = self.usuario.get()
        self.contact.real = self.contact.get()

        self.saveCliente()

    def saveCliente(self):

        with open('arquivo.json') as C:
            data = json.load(C)

        data["Clientes"].append({"Code":str(self.code),"Nome": str(self.nome.real),"RG": str(self.rg.real),"CPF": str(self.cpf.real),"E-mail": str(self.mail.real),\
            "Telefone de contato": str(self.tel.real),"Endereco": str(self.end.real),"CEP": str(self.cep.real),"Bairro": str(self.bairro.real),"Cidade": str(self.cid.real),\
            "UF": str(self.uf.real),"Usuario INRE": str(self.usuario.real),"Forma de contato":str(self.contact.real), "Pedidos":[]
            })

        with open('arquivo.json', 'w') as C:
            json.dump(data, C)

    def showReciclar(self):

        self.master.destroy()

        self.__init__(master=None)

        Label(self.master,text="Recic-Lar",font=fonteD).grid()

        self.scroll = ttk.Notebook(self.master)

        self.scroll_1 = ttk.Frame(self.scroll)
        self.scroll_2 = ttk.Frame(self.scroll)
        self.scroll_3 = ttk.Frame(self.scroll)
        self.scroll_4 = ttk.Frame(self.scroll)
        self.scroll_5 = ttk.Frame(self.scroll)
        self.scroll_6 = ttk.Frame(self.scroll)

        self.scroll.add(self.scroll_1, text='Charge')

        self.defineCliente()

        self.scroll.add(self.scroll_2, text='Orçamento')

        self.createOrcamento()

        self.scroll.add(self.scroll_3, text='Mudança')

        self.showMudanca()

        self.scroll.add(self.scroll_4, text='Endereço serviço')

        self.showEndereco()

        self.scroll.add(self.scroll_5, text='Dados cliente')

        Button(self.scroll_5, text="Mostrar cliente",command=lambda:self.showClienteRecic()).grid(row=0,column=2)

        self.scroll.add(self.scroll_6, text="Finalização")
        
        self.scroll.grid()

    def defineCliente(self):

        Label(self.scroll_1,text="Digite o código do cliente para iniciar o orçamento",font=fonteC).grid(row=0,column=0)

        self.pre = Entry(self.scroll_1)
        self.pre.grid(row=1,column=0)

        Button(self.scroll_1,text="Verificar se existe no registro de clientes",command=self.verifyClienteRecic).grid()

    def verifyClienteRecic(self):

        with open('arquivo.json') as C:
            data = json.load(C)

        self.pre.real = self.pre.get()

        self.searchClienteRecic()

    def searchClienteRecic(self):

        with open('arquivo.json') as C:
            data = json.load(C)

        for cliente in data["Clientes"]:
            if cliente['Code'] == self.pre.real:

                self.chargeCliente(self.pre.real)

                Label(self.scroll_1,text="Cliente carregado prossiga com o orçamento!",font=fonteC).grid(row=5,column=0)

            else:

                Label(self.scroll_1,text="Cliente não registrado",font=fonteC)

    def createOrcamento(self):

        v = tk.IntVar()

        Label(self.scroll_2, text="Esvaziamento", padx = 20,pady=20).grid(row=0,column=0)
        Radiobutton(self.scroll_2,text="Com movéis grandes",padx = 20,pady=20,variable=v,value=1).grid(row=0,column=1)
        Radiobutton(self.scroll_2,text="Sem movéis grandes",padx = 20,pady=20,variable=v,value=2).grid(row=0,column=2)

        scrollbar = Scrollbar(self.scroll_2)
        scrollbar.grid(row=3,column=1)

        Label(self.scroll_2,text="Lista de equipamentos").grid(row=2,column=0)

        self.mylist = Listbox(self.scroll_2,yscrollcommand=scrollbar.set,width=40)
        self.mylist.insert(1, "Equipamentos                         M3")

        Button(self.scroll_2,text="ADD",command=self.CurSelet).grid(row=5,column=1)

        self.mylist.grid(row=3,column=0)
        scrollbar.config(command=self.mylist.yview)

        self.mylist1 = Listbox(self.scroll_2,yscrollcommand=scrollbar.set,width=40)
        self.mylist1.grid(row=3,column=2)
        Label(self.scroll_2,text="Lista de equipamentos adicionados").grid(row=2,column=2)

        self.qnt = Entry(self.scroll_2)
        self.qnt.grid(row=4,column=1)

    #def addEquipamento(self):


    def CurSelet(self):

        self.getQnt()

        value = str(self.mylist.get(self.mylist.curselection()))
        for i in range(0,int(self.qnt.new)):
            self.mylist1.insert(END,value)

    def getQnt(self):

        self.qnt.new = self.qnt.get()
        
    def showMudanca(self):

        Label(self.scroll_3,text="Data da mudança").grid()

        self.data = Entry(self.scroll_3)
        self.data.grid()

        Label(self.scroll_3,text="Motivo da mudança").grid()

        self.motivo = Entry(self.scroll_3)
        self.motivo.grid()

    def showEndereco(self):
        
        Label(self.scroll_4,text="Endereço do serviço").grid()

        Button(self.scroll_4,text="Mesmo do cadastro",command=lambda:self.showEnderecoRecic()).grid()

        Button(self.scroll_4,text="Outro endereço",command=lambda:self.createEndereco()).grid()

    def showEnderecoRecic(self):

        Label(self.scroll_4,text=self.end,font=fonteB).grid(row=3,column=1)

        Label(self.scroll_4,text=self.cep,font=fonteB).grid(row=4,column=1)

        Label(self.scroll_4,text=self.bairro,font=fonteB).grid(row=5,column=1)

        Label(self.scroll_4,text=self.cid,font=fonteB).grid(row=6,column=1)

        Label(self.scroll_4,text=self.uf,font=fonteB).grid(row=7,column=1)

        frase20 = Label(self.scroll_4, text="Endereço")
        frase20.grid(row=3,column=0)

        frase30 = Label(self.scroll_4, text="CEP")
        frase30.grid(row=4,column=0)

        frase40 = Label(self.scroll_4, text="Bairro")
        frase40.grid(row=5,column=0)

        frase60 = Label(self.scroll_4,text="Cidade")
        frase60.grid(row=6,column=0)

        frase50 = Label(self.scroll_4, text="UF")
        frase50.grid(row=7,column=0)

    def createEndereco(self):

        self.end_recic=Entry(self.scroll_4)
        self.end_recic.grid(row=3, column=1)

        self.cep_recic=Entry(self.scroll_4)
        self.cep_recic.grid(row=4, column=1)

        self.bairro_recic = Entry(self.scroll_4)
        self.bairro_recic.grid(row=5,column=1)

        self.cid_recic=Entry(self.scroll_4)
        self.cid_recic.grid(row=6, column=1)

        self.uf_recic = Entry(self.scroll_4)
        self.uf_recic.grid(row=7,column=1)

        frase20 = Label(self.scroll_4, text="Endereço")
        frase20.grid(row=3, column=0)

        frase30 = Label(self.scroll_4, text="CEP")
        frase30.grid(row=4 , column=0)

        frase40 = Label(self.scroll_4, text="Bairro")
        frase40.grid(row=5 , column=0)

        frase60 = Label(self.scroll_4,text="Cidade")
        frase60.grid(row=6,column=0)

        frase50 = Label(self.scroll_4, text="UF")
        frase50.grid(row=7 , column=0)

    def showClienteRecic(self):

        Label(self.scroll_5,text="Dados do cliente para orçamento",font=fonteC).grid(row=0,column=0)

        Label(self.scroll_5,text=self.code,font=fonteB).grid(row=3, column=2)

        Label(self.scroll_5,text=self.nome,font=fonteB).grid(row=4, column=2)

        Label(self.scroll_5,text=self.cpf,font=fonteB).grid(row=5, column=2)

        Label(self.scroll_5,text=self.rg,font=fonteB).grid(row=6, column=2)

        Label(self.scroll_5,text=self.mail,font=fonteB).grid(row=7, column=2)

        Label(self.scroll_5,text=self.tel,font=fonteB).grid(row=8, column=2)

        Label(self.scroll_5,text=self.end,font=fonteB).grid(row=9, column=2)

        Label(self.scroll_5,text=self.cep,font=fonteB).grid(row=10, column=2)

        Label(self.scroll_5,text=self.bairro,font=fonteB).grid(row=11, column=2)

        Label(self.scroll_5,text=self.cid,font=fonteB).grid(row=12, column=2)

        Label(self.scroll_5,text=self.uf,font=fonteB).grid(row=13, column=2)

        Label(self.scroll_5,text=self.usuario,font=fonteB).grid(row=14, column=2)

        Label(self.scroll_5,text=self.contact,font=fonteB).grid(row=15, column=2)

        frase1 = Label(self.scroll_5, text="Dados do cliente")
        frase1.grid(row=2 , column=2)

        frase0 = Label(self.scroll_5,text="Identificação - Código Cliente")
        frase0.grid(row=3,column=0)

        frase2 = Label(self.scroll_5, text="Nome de usuário")
        frase2.grid(row=4, column=0)

        frase4 = Label(self.scroll_5, text="CPF")
        frase4.grid(row=5 , column=0)

        frase4 = Label(self.scroll_5, text="RG")
        frase4.grid(row=6 , column=0)

        frase5 = Label(self.scroll_5, text="E-mail")
        frase5.grid(row=7 , column=0)

        frase10 = Label(self.scroll_5, text="Contato Telefone/Celular")
        frase10.grid(row=8 , column=0)

        frase20 = Label(self.scroll_5, text="Endereço")
        frase20.grid(row=9, column=0)

        frase30 = Label(self.scroll_5, text="CEP")
        frase30.grid(row=10 , column=0)

        frase40 = Label(self.scroll_5, text="Bairro")
        frase40.grid(row=11 , column=0)

        frase60 = Label(self.scroll_5,text="Cidade")
        frase60.grid(row=12,column=0)

        frase50 = Label(self.scroll_5, text="UF")
        frase50.grid(row=13,column=0)

        fraseU = Label(self.scroll_5, text="Usuário INRE")
        fraseU.grid(row=14,column=0)

        fraseU = Label(self.scroll_5, text="Forma de contato")
        fraseU.grid(row=15,column=0)

    def showPreCliente(self):

        self.master.destroy()

        self.__init__(master=None)

        self.showCode()

        Label(self.master,text="Digite o código do cliente para ver seus dados",font=fonteC).grid(row=0,column=0)

        self.pre = Entry(self.master)
        self.pre.grid(row=1,column=0)

        Button(self.master,text="Verificar se existe no registro de clientes",command=self.verifyCliente).grid()

    def showImg(self):
        load = Image.open("a.png")
        render = ImageTk.PhotoImage(load)

        # labels can be text or images
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)

    def verifyCliente(self):

        with open('arquivo.json') as C:
            data = json.load(C)

        self.pre.real = self.pre.get()

        self.searchCliente()

    def searchCliente(self):

        with open('arquivo.json') as C:
            data = json.load(C)

        for cliente in data["Clientes"]:
            if cliente['Code'] == self.pre.real:

                self.chargeCliente(self.pre.real)

                Label(self.master,text="Cliente registrado!",font=fonteC).grid(row=5,column=0)

                Button(self.master,text="Ver dados",command=self.showCliente,font=fonteC).grid(row=6,column=0)

            else:

                Label(self.master,text="Cliente não registrado",font=fonteC)

    def showBut(self):
        button_1 = Button(self, text="Cadastro Cliente")  
        button_1.grid()

    def showCliente(self):

        self.master.destroy()

        self.__init__(master=None)

        Label(self.master,text="Dados de cliente",font=fonteC).grid(row=0,column=0)

        Label(self.master,text=self.code,font=fonteB).grid(row=3, column=2)

        Label(self.master,text=self.nome,font=fonteB).grid(row=4, column=2)

        Label(self.master,text=self.cpf,font=fonteB).grid(row=5, column=2)

        Label(self.master,text=self.rg,font=fonteB).grid(row=6, column=2)

        Label(self.master,text=self.mail,font=fonteB).grid(row=7, column=2)

        Label(self.master,text=self.tel,font=fonteB).grid(row=8, column=2)

        Label(self.master,text=self.end,font=fonteB).grid(row=9, column=2)

        Label(self.master,text=self.cep,font=fonteB).grid(row=10, column=2)

        Label(self.master,text=self.bairro,font=fonteB).grid(row=11, column=2)

        Label(self.master,text=self.cid,font=fonteB).grid(row=12, column=2)

        Label(self.master,text=self.uf,font=fonteB).grid(row=13, column=2)

        Label(self.master,text=self.usuario,font=fonteB).grid(row=14, column=2)

        Label(self.master,text=self.contact,font=fonteB).grid(row=15, column=2)

        frase1 = Label(self.master, text="Dados do cliente")
        frase1.grid(row=2 , column=2)

        frase0 = Label(self.master,text="Identificação - Código Cliente")
        frase0.grid(row=3,column=0)

        frase2 = Label(self.master, text="Nome de usuário")
        frase2.grid(row=4, column=0)

        frase4 = Label(self.master, text="CPF")
        frase4.grid(row=5 , column=0)

        frase4 = Label(self.master, text="RG")
        frase4.grid(row=6 , column=0)

        frase5 = Label(self.master, text="E-mail")
        frase5.grid(row=7 , column=0)

        frase10 = Label(self.master, text="Contato Telefone/Celular")
        frase10.grid(row=8 , column=0)

        frase20 = Label(self.master, text="Endereço")
        frase20.grid(row=9, column=0)

        frase30 = Label(self.master, text="CEP")
        frase30.grid(row=10 , column=0)

        frase40 = Label(self.master, text="Bairro")
        frase40.grid(row=11 , column=0)

        frase60 = Label(self.master,text="Cidade")
        frase60.grid(row=12,column=0)

        frase50 = Label(self.master, text="UF")
        frase50.grid(row=13,column=0)

        fraseU = Label(self.master, text="Usuário INRE")
        fraseU.grid(row=14,column=0)

        fraseU = Label(self.master, text="Forma de contato")
        fraseU.grid(row=15,column=0)

    def showClienteScroll(self):

        Label(self.scroll_5,text=self.code,font=fonteB).grid(row=3, column=2)

        Label(self.scroll_5,text=self.nome,font=fonteB).grid(row=4, column=2)

        Label(self.scroll_5,text=self.cpf,font=fonteB).grid(row=5, column=2)

        Label(self.scroll_5,text=self.rg,font=fonteB).grid(row=6, column=2)

        Label(self.scroll_5,text=self.mail,font=fonteB).grid(row=7, column=2)

        Label(self.scroll_5,text=self.tel,font=fonteB).grid(row=8, column=2)

        Label(self.scroll_5,text=self.end,font=fonteB).grid(row=9, column=2)

        Label(self.scroll_5,text=self.cep,font=fonteB).grid(row=10, column=2)

        Label(self.scroll_5,text=self.bairro,font=fonteB).grid(row=11, column=2)

        Label(self.scroll_5,text=self.cid,font=fonteB).grid(row=12, column=2)

        Label(self.scroll_5,text=self.uf,font=fonteB).grid(row=13, column=2)

        Label(self.scroll_5,text=self.usuario,font=fonteB).grid(row=14, column=2)

        frase1 = Label(self.scroll_5, text="Dados do cliente")
        frase1.grid(row=2 , column=2)

        frase0 = Label(self.scroll_5,text="Identificação - Código Cliente")
        frase0.grid(row=3,column=0)

        frase2 = Label(self.scroll_5, text="Nome de usuário")
        frase2.grid(row=4, column=0)

        frase4 = Label(self.scroll_5, text="CPF")
        frase4.grid(row=5 , column=0)

        frase4 = Label(self.scroll_5, text="RG")
        frase4.grid(row=6 , column=0)

        frase5 = Label(self.scroll_5, text="E-mail")
        frase5.grid(row=7 , column=0)

        frase10 = Label(self.scroll_5, text="Contato Telefone/Celular")
        frase10.grid(row=8 , column=0)

        frase20 = Label(self.scroll_5, text="Endereço")
        frase20.grid(row=9, column=0)

        frase30 = Label(self.scroll_5, text="CEP")
        frase30.grid(row=10 , column=0)

        frase40 = Label(self.scroll_5, text="Bairro")
        frase40.grid(row=11 , column=0)

        frase60 = Label(self.scroll_5,text="Cidade")
        frase60.grid(row=12,column=0)

        frase50 = Label(self.scroll_5, text="UF")
        frase50.grid(row=13,column=0)

        fraseU = Label(self.scroll_5, text="Usuário INRE")
        fraseU.grid(row=14,column=0)

    def chargeCliente(self,cod):

        with open('arquivo.json') as C:
            data = json.load(C)

        for cliente in data["Clientes"]:
            if cliente["Code"] == cod:
                self.code = cod
                self.nome = cliente["Nome"]
                self.rg = cliente["RG"]
                self.cpf = cliente["CPF"]
                self.tel = cliente["Telefone de contato"]
                self.end = cliente["Endereco"]
                self.mail = cliente["E-mail"]
                self.cep = cliente["CEP"]
                self.bairro = cliente["Bairro"]
                self.cid = cliente["Cidade"]
                self.uf = cliente["UF"]
                self.usuario = cliente["Usuario INRE"]
                self.contact = cliente["Forma de contato"]

    def showCode(self):

        global code

        with open('arquivo.json') as C:
            data = json.load(C)

        co = len(data["Clientes"])+1

        code = "{0}/2018".format(co)

        
# Fontes

fonteA = ("Verdana", 8)
fonteB = ("Verdana", 10)
fonteC = ("Verdana", 12)
fonteD = ("Verdana", 16)
fonteE = ("Verdana", 20)

# root window created. Here, that would be the only window, but
# you can later have windows within windows.
root = Tk()

root.geometry("600x400")

#creation of an instance
app = Window(root)


#mainloop 
root.mainloop()