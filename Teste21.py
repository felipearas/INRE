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

    def __init__(self, master=None):

        #reference to the master widget, which is the tk window                 
        self.master = master
        
        # parameters that you want to send through the Frame class. 
        Frame.__init__(self,self.master)

        # setting the window dimensions.
        self.master.geometry("1000x720")
        
        #with that, we want to then run init_window, which doesn't yet exist
        self.init_window()

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

        recic.add_command(label="Prestador",command=self.showPrePrestador)

        #added "file" to our menu
        menu.add_cascade(label="Pesquisa Interna", menu=recic)

    def showImagemInicial(self):

        foto =PhotoImage(file="a.PNG")
        titulo=Label(self.master, image=foto,width=800, height=370)
        titulo.image=foto
        titulo.grid()

    def showTeam(self):

        Label(self.master,text="INRE Team",font=fonteG).grid(row=8,column=0)

        Label(self.master,text="Carol",font=fonteH).grid(row=9,column=0)

        Label(self.master,text="Felipe",font=fonteH).grid(row=10,column=0)

        Label(self.master,text="George",font=fonteH).grid(row=11,column=0)

        Label(self.master,text="Tati",font=fonteH).grid(row=12,column=0)

    def showServicos(self):

        self.master.destroy()

        self.__init__(master=None)

        Label(self.master, text="INRE SERVIÇOS",font=fonteC,padx=325,pady=30).grid(row=0,column=0)

        Label(self.master, text="Bem vindo, serviços disponíveis:",font=fonteC,pady=10).grid(row=1,column=0)

        Button(self.master, width=35,pady = 10,text="Cadastrar cliente",command=lambda:self.showCadastro()).grid()
        Button(self.master, width=35,pady = 10,text="Cadastrar prestador", command=lambda:self.showCadastroPrestador()).grid()
        Button(self.master, width=35,pady = 10,text="Orçamento Recic-Lar",command=lambda:self.showReciclar()).grid()
        Button(self.master, width=35,pady = 10,text="Orçamento Retirada PF",command=lambda:self.showRetiradaPF()).grid()
        Button(self.master, width=35,pady = 10,text="Orçamento Retirada PJ",command=lambda:self.showRetiradaPJ()).grid()

    def showCadastro(self):

        self.master.destroy()

        self.__init__(master=None)

        self.showCode()

        self.data_inicial = Entry(self.master)
        self.data_inicial.grid(row=4,column=2)

        self.nome = Entry(self.master)
        self.nome.grid(row=5,column=2)

        self.cpf = Entry(self.master)
        self.cpf.grid(row=6,column=2)

        self.rg = Entry(self.master)
        self.rg.grid(row=7,column=2)

        self.mail = Entry(self.master)
        self.mail.grid(row=8,column=2)

        self.tel = Entry(self.master)
        self.tel.grid(row=9,column=2)

        self.end = Entry(self.master)
        self.end.grid(row=10,column=2)

        self.cep = Entry(self.master)
        self.cep.grid(row=11,column=2)

        self.bairro = Entry(self.master)
        self.bairro.grid(row=12,column=2)

        self.cid = Entry(self.master)
        self.cid.grid(row=13,column=2)

        self.uf = Entry(self.master)
        self.uf.grid(row=14,column=2)

        self.usuario = Entry(self.master)
        self.usuario.grid(row=15,column=2)

        self.forma_contato = Entry(self.master)
        self.forma_contato.grid(row=16,column=2)

        Label(self.master,text="Cadastro de cliente para o banco de dados",font=fonteC,padx=100,pady=30).grid(row=0,column=0)

        Label(self.master,text=self.code).grid(row=3,column=2)

        Label(self.master,text="Dados do cliente").grid(row=2 , column=2)

        Label(self.master,text="Identificação - Código Cliente").grid(row=3,column=0)

        Label(self.master,text="Data do contato inicial").grid(row=4,column=0)

        Label(self.master,text="Nome do cliente").grid(row=5, column=0)

        Label(self.master,text="CPF").grid(row=6 , column=0)

        Label(self.master,text="RG").grid(row=7 , column=0)

        Label(self.master,text="E-mail").grid(row=8 , column=0)

        Label(self.master,text="Contato Telefone/Celular").grid(row=9 , column=0)

        Label(self.master,text="Endereço").grid(row=10, column=0)

        Label(self.master,text="CEP").grid(row=11 , column=0)

        Label(self.master,text="Bairro").grid(row=12 , column=0)

        Label(self.master,text="Cidade").grid(row=13,column=0)

        Label(self.master,text="UF").grid(row=14 , column=0)

        Label(self.master,text="Responsável pelo chamado").grid(row=15,column=0)

        Label(self.master,text="Forma de contato inicial").grid(row=16,column=0)

        Button(self.master,text="Salvar dados",command=self.showGet).grid(row=17, column=2)
        
        Button(self.master,text="Concluir e voltar a tela dos serviços",command=self.showServicos).grid(row=18,column=0)

    def showCode(self):

        with open('arquivo.json') as C:
            data = json.load(C)

        co = len(data["Clientes"])+1

        self.code = "{0}/2018".format(co)

    def showGet(self):

        Label(self.master,text="Os dados do cliente foram salvos com sucesso!",font=fonteA).grid(row=18,column=2)

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
        self.forma_contato.real = self.forma_contato.get()
        self.data_inicial.real = self.data_inicial.get()

        self.saveCliente()

    def saveCliente(self):

        with open('arquivo.json') as C:
            data = json.load(C)

        data["Clientes"].append({"Code":str(self.code),"Data do contato inicial":str(self.data_inicial.real),"Nome": str(self.nome.real),"RG": str(self.rg.real),"CPF": str(self.cpf.real),"E-mail": str(self.mail.real),\
            "Telefone de contato": str(self.tel.real),"Endereco": str(self.end.real),"CEP": str(self.cep.real),"Bairro": str(self.bairro.real),"Cidade": str(self.cid.real),\
            "UF": str(self.uf.real),"Usuario INRE": str(self.usuario.real),"Forma de contato":str(self.forma_contato.real), "Pedidos":[]
            })

        with open('arquivo.json', 'w') as C:
            json.dump(data, C)

    def showCadastroPrestador(self):

        self.master.destroy()

        self.__init__(master=None)

        self.showCodePrestador()

        self.data_inicial_prestador = Entry(self.master)
        self.data_inicial_prestador.grid(row=4,column=2)

        self.empresa = Entry(self.master)
        self.empresa.grid(row=5,column=2)

        self.cnpj = Entry(self.master)
        self.cnpj.grid(row=6,column=2)

        self.servico_prestado = Entry(self.master)
        self.servico_prestado.grid(row=7,column=2)

        self.email = Entry(self.master)
        self.email.grid(row=8,column=2)

        self.telefone = Entry(self.master)
        self.telefone.grid(row=9,column=2)

        self.endereco_prestador = Entry(self.master)
        self.endereco_prestador.grid(row=10,column=2)

        self.cep_prestador = Entry(self.master)
        self.cep_prestador.grid(row=11,column=2)

        self.bairro_prestador = Entry(self.master)
        self.bairro_prestador.grid(row=12,column=2)

        self.cidade_prestador = Entry(self.master)
        self.cidade_prestador.grid(row=13,column=2)

        self.uf_prestador = Entry(self.master)
        self.uf_prestador.grid(row=14,column=2)

        self.usuario_empresa = Entry(self.master)
        self.usuario_empresa.grid(row=15,column=2)

        self.forma_contato_prestador = Entry(self.master)
        self.forma_contato_prestador.grid(row=16,column=2)

        Label(self.master,text="Cadastro de prestador de serviços para o banco de dados",font=fonteC,padx=100,pady=30).grid(row=0,column=0)

        Label(self.master,text=self.codePrestador).grid(row=3,column=2)

        Label(self.master,text="Dados do prestador de serviços").grid(row=2 , column=2)

        Label(self.master,text="Identificação - Código prestador").grid(row=3,column=0)

        Label(self.master,text="Data do contato inicial").grid(row=4,column=0)

        Label(self.master,text="Nome da/do Empresa/Prestador").grid(row=5, column=0)

        Label(self.master,text="CNPJ").grid(row=6 , column=0)

        Label(self.master,text="Serviço prestado").grid(row=7 , column=0)

        Label(self.master,text="E-mail").grid(row=8 , column=0)

        Label(self.master,text="Contato Telefone/Celular").grid(row=9 , column=0)

        Label(self.master,text="Endereço").grid(row=10, column=0)

        Label(self.master,text="CEP").grid(row=11 , column=0)

        Label(self.master,text="Bairro").grid(row=12 , column=0)

        Label(self.master,text="Cidade").grid(row=13,column=0)

        Label(self.master,text="UF").grid(row=14 , column=0)

        Label(self.master,text="Falar diretamente com").grid(row=15,column=0)

        Label(self.master,text="Forma de contato inicial").grid(row=16,column=0)

        Button(self.master,text="Salvar dados",command=self.showGetPrestador).grid(row=17, column=2)
        
        Button(self.master,text="Concluir e voltar a tela dos serviços",command=self.showServicos).grid(row=18,column=0)

    def showCodePrestador(self):

        with open('arquivo.json') as C:
            data = json.load(C)

        codePrestador = len(data["Prestadores"])+1

        self.codePrestador = "2018/{0}".format(codePrestador)

    def showGetPrestador(self):

        Label(self.master,text="Os dados do prestador foram salvos com sucesso!",font=fonteA).grid(row=18,column=2)

        self.empresa.real = self.empresa.get()
        self.servico_prestado.real = self.servico_prestado.get()
        self.cnpj.real = self.cnpj.get()
        self.email.real = self.email.get()
        self.telefone.real = self.telefone.get()
        self.endereco_prestador.real = self.endereco_prestador.get()
        self.cep_prestador.real = self.cep_prestador.get()
        self.bairro_prestador.real = self.bairro_prestador.get()
        self.cidade_prestador.real = self.cidade_prestador.get()
        self.uf_prestador.real = self.uf_prestador.get()
        self.usuario_empresa.real = self.usuario_empresa.get()
        self.forma_contato_prestador.real = self.forma_contato_prestador.get()
        self.data_inicial_prestador.real = self.data_inicial_prestador.get()

        self.savePrestador()

    def savePrestador(self):

        with open('arquivo.json') as C:
            data = json.load(C)

        data["Prestadores"].append({"Code":str(self.codePrestador),"Data do contato inicial":str(self.data_inicial_prestador.real),"Nome": str(self.empresa.real),"Servico prestado": str(self.servico_prestado.real),"CNPJ": str(self.cnpj.real),"E-mail": str(self.email.real),\
            "Telefone de contato": str(self.telefone.real),"Endereco": str(self.endereco_prestador.real),"CEP": str(self.cep_prestador.real),"Bairro": str(self.bairro_prestador.real),"Cidade": str(self.cidade_prestador.real),\
            "UF": str(self.uf_prestador.real),"Falar diretamente com": str(self.usuario_empresa.real),"Forma de contato":str(self.forma_contato_prestador.real), "Pedidos":[]
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
        self.defineClienteRecic()

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

    def defineClienteRecic(self):

        Label(self.scroll_1,text="Digite o código do cliente para iniciar o orçamento",font=fonteC,padx=100,pady=30).grid(row=0,column=0)

        self.pre = Entry(self.scroll_1)
        self.pre.grid(row=1,column=0)

        Button(self.scroll_1,text="Verificar se existe no registro de clientes",command=self.verifyClienteRecic,pady=30,font=fonteB).grid(row=2,column=0)

    def verifyClienteRecic(self):

        with open('arquivo.json') as C:
            data = json.load(C)

        self.pre.real = self.pre.get()

        self.searchClienteRecic()

    def searchClienteRecic(self):

        with open('arquivo.json') as C:
            data = json.load(C)

        self.true_false = ["0"]

        for cliente in data["Clientes"]:
            if cliente['Code'] == self.pre.real:

                self.chargeCliente(self.pre.real)

                Label(self.scroll_1,text="Cliente carregado prossiga com o orçamento!",font=fonteC,pady=20).grid(row=5,column=0)

                self.true_false[0] = "TRUE"

        if self.true_false[0] == "0":

            Label(self.scroll_1,text="Cliente não encontrado",font=fonteC).grid(row=5,column=0)

    def createOrcamento(self):

        self.v = StringVar()

        Label(self.scroll_2, text="Esvaziamento", padx = 20,pady=20).grid(row=0,column=0)
        Radiobutton(self.scroll_2,text="Com movéis grandes",padx = 20,pady=20,variable=self.v,value="Com moveis grandes").grid(row=0,column=2)
        Radiobutton(self.scroll_2,text="Sem movéis grandes",padx = 20,pady=20,variable=self.v,value="Sem moveis grandes").grid(row=0,column=3)

        scrollbar = Scrollbar(self.scroll_2)
        scrollbar.grid(row=3,column=1)

        scrollbar_2 = Scrollbar(self.scroll_2)
        scrollbar_2.grid(row=3,column=4)

        Label(self.scroll_2,text="Lista de equipamentos").grid(row=2,column=0)

        self.mylist = Listbox(self.scroll_2,yscrollcommand=scrollbar.set,width=40)
        self.mylist.insert(1, "Equipamentos")
        self.mylist.insert(2,  "Armario de cozinha")
        self.mylist.insert(3, "Buffet")
        self.mylist.insert(4, "Cadeira")
        self.mylist.insert(5, "Cama Box Casal")
        self.mylist.insert(6, "Cama Box Solteiro")
        self.mylist.insert(7, "Colchão cama de casal")
        self.mylist.insert(8, "Colchão cama de solteiro")
        self.mylist.insert(9, "Comoda")
        self.mylist.insert(10, "Escrivaninha")
        self.mylist.insert(11, "Fogão 4 bocas")
        self.mylist.insert(12, "Fogão 6 bocas")
        self.mylist.insert(13, "Freezer Vertical")
        self.mylist.insert(14, "Geladeira  2 portas")
        self.mylist.insert(15, "Lavadoura de louça")
        self.mylist.insert(16, "Maquina de lavar roupa")
        self.mylist.insert(17, "Mesa de Jantar 6 lugares")
        self.mylist.insert(18, "Mesa de Jantar 8 lugares")
        self.mylist.insert(19, "Poltrona")
        self.mylist.insert(20, "Rack")
        self.mylist.insert(21, "Sofá 2 lugares")
        self.mylist.insert(22, "Sofá 3 lugares")


        Button(self.scroll_2,text="Adicionar",command=self.CurSelet).grid(row=4,column=2)

        Button(self.scroll_2,text="Remover",command=self.deleteList).grid(row=4,column=3)

        self.mylist.grid(row=3,column=0)
        scrollbar.config(command=self.mylist.yview)

        self.mylist1 = Listbox(self.scroll_2,yscrollcommand=scrollbar.set,width=40)
        self.mylist1.grid(row=3,column=3)
        Label(self.scroll_2,text="Lista de equipamentos adicionados").grid(row=2,column=3)

        scrollbar_2.config(command=self.mylist1.yview)
        
        self.qnt = Entry(self.scroll_2)
        self.qnt.grid(row=3,column=2)

        Label(self.scroll_2,text="").grid(row=5,column=2)

        Label(self.scroll_2,text="Instituição").grid(row=6,column=2)

        self.inst = StringVar()

        Radiobutton(self.scroll_2,text="Unibes",padx = 20,pady=20,variable=self.inst,value="Unibes").grid(row=7,column=0)
        Radiobutton(self.scroll_2,text="Casa André Luis",padx = 20,pady=20,variable=self.inst,value="Casa Andre Luis").grid(row=7,column=2)
        Radiobutton(self.scroll_2,text="Exército de salvação",padx = 20,pady=20,variable=self.inst,value="Exercito de salvacao").grid(row=7,column=3)

        Label(self.scroll_2,text="Tipo do imóvel").grid(row=8,column=2)

        self.k = StringVar()

        Radiobutton(self.scroll_2,text="Casa",padx = 20,pady=20,variable=self.k,value="Casa").grid(row=9,column=0)
        Radiobutton(self.scroll_2,text="Apartamento",padx = 20,pady=20,variable=self.k,value="Apartamento").grid(row=9,column=2)
        Radiobutton(self.scroll_2,text="Escritório",padx = 20,pady=20,variable=self.k,value="Escritorio").grid(row=9,column=3)

        Label(self.scroll_2,text="N° Dorms").grid(row=11,column=0)

        self.ndorm = Entry(self.scroll_2)
        self.ndorm.grid(row=11,column=2)

        Label(self.scroll_2,text="N° Pavimentos").grid(row=12,column=0)

        self.npav = Entry(self.scroll_2)
        self.npav.grid(row=12,column=2)

        Label(self.scroll_2,text="Metragem (m²)").grid(row=13,column=0)

        self.met = Entry(self.scroll_2)
        self.met.grid(row=13,column=2)

        Label(self.scroll_2,text="Cor da tinta").grid(row=14,column=0)

        inst = ("Branco Gelo","Off White","Bege")

        Spinbox(self.scroll_2,values=sorted(inst),width=len(max(inst))+9).grid(row=14,column=2)

        Label(self.scroll_2,text="Pintura").grid(row=15,column=0)

        self.vav = StringVar()

        Radiobutton(self.scroll_2,text="Com teto",padx = 20,pady=20,variable=self.vav,value="Com teto").grid(row=15,column=2)
        Radiobutton(self.scroll_2,text="Sem teto",padx = 20,pady=20,variable=self.vav,value="Sem teto").grid(row=15,column=3)

        Button(self.scroll_2,text="Calcular",command=self.saveRecic,width=30).grid(row=16,column=3)

    def CurSelet(self):

        self.getQnt()

        value = str(self.mylist.get(self.mylist.curselection()))

        for i in range(0,int(self.qnt.new)):
            self.mylist1.insert(END,value)

    def getQnt(self):

        self.qnt.new = self.qnt.get()

    def deleteList(self):

        sel = self.mylist1.curselection()
        for index in sel[::-1]:
            self.mylist1.delete(index)

    def executeAplicar(self):

        self.equip = {"Cama Box Casal":2.16,"Colchão cama de casal":0.93,"Cama Box Solteiro":1.11,"Colchão cama de solteiro":0.6,"Geladeira  2 portas":0.97,"Fogão 4 bocas":0.3,"Fogão 6 bocas":0.49,\
                        "Maquina de lavar roupa":0.59,"Sofá 3 lugares":2,"Sofá 2 lugareS":1.85,"Mesa de Jantar 6 lugares":1.01,"Mesa de Jantar 8 lugares":1.89,"Cadeira":0.3,"Buffet":0.57,"Rack":0.49, \
                        "Lavadoura de louça":0.33,"Freezer Vertical":0.62,"Poltrona":0.93,"Armario de cozinha":1.68,"Comoda":1.11,"Escrivaninha":0.41}

        self.getRecic()

        self.string = self.mylist1.get(0,END)

        self.conta_cliente = []

        for i in range(0,len(self.string)):
            self.equipamentos = self.equip.get(self.string[i])
            self.conta_cliente.append(self.equipamentos)

        self.total = sum(self.conta_cliente)

        self.orcamento = 0

        self.caminhao_pequeno = 670

        self.caminhao_medio = 770

        self.caminhao_grande = 920

        self.pintm2 = 25

        self.limpm2 = 4

        self.pintetom2 = 8

        self.taxaInre = 30/100

        self.impostos = 0.83

        if self.total <= 6:
            self.orcamento = self.orcamento + self.caminhao_pequeno
            Label(self.scroll_2,text="CP:1  CM:0    CG:0").grid(row=17,column=0)

        if self.total > 6 and self.total <= 13:
            self.orcamento = self.orcamento + self.caminhao_medio
            Label(self.scroll_2,text="CP:0  CM:1    CG:0").grid(row=17,column=0)

        if self.total >13 and self.total <= 21:
            self.orcamento = self.orcamento + self.caminhao_grande
            Label(self.scroll_2,text="CP:0  CM:0    CG:1").grid(row=17,column=0)

        self.orcamento = self.orcamento + (int(self.met.real)*self.pintm2)

        self.orcamento = self.orcamento + (int(self.met.real)*self.limpm2)

        if self.vav.real == "Com teto":
            self.orcamento = self.orcamento + (int(self.met.real)*self.pintetom2)

        self.orcamento = self.orcamento + (self.orcamento*self.taxaInre)

        self.orcamento = self.orcamento/self.impostos

        with open('arquivo.json') as C:
            data = json.load(C)

    def getRecic(self):

        self.ndorm.real = self.ndorm.get()

        self.npav.real = self.npav.get()

        self.met.real = self.met.get()

        self.v.real = self.v.get()

        self.inst.real = self.inst.get()

        self.k.real = self.k.get()

        self.vav.real = self.vav.get()

    def saveRecic(self):

        self.executeAplicar()

        Label(self.scroll_2,text="O valor do orçamento é R${0}".format(round(self.orcamento,2))).grid(row=16,column=0)

        with open('arquivo.json') as C:
            data = json.load(C)

        for cliente in data["Clientes"]:
            if cliente['Code'] == self.pre.real:
                cliente["Pedidos"].append({"Pedido":len(cliente["Pedidos"])+1,"Servico":"Recic-Lar","Moveis":self.v.real,"Instituicao de doacao":self.inst.real,\
                                            "Tipo do imovel":self.k.real,"N de Dormitorios":self.ndorm.real,"N de Pavimentos":self.npav.real,"Metragem":self.met.real,\
                                            "Pintura com ou sem teto":self.vav.real,"Valor do Orcamento":self.orcamento})

        with open('arquivo.json', 'w') as C:
            json.dump(data, C)

    def showMudanca(self):

        Label(self.scroll_3,text="Data da mudança",padx=100,pady=30).grid(row=0,column=0)

        self.data = Entry(self.scroll_3)
        self.data.grid(row=0,column=1)

        Label(self.scroll_3,text="Motivo da mudança").grid(row=1,column=0)

        self.motivo = Entry(self.scroll_3)
        self.motivo.grid(row=1,column=1)

    def showEndereco(self):
        
        Label(self.scroll_4,text="Endereço do serviço",padx=100,pady=30).grid(row=0,column=0)

        Button(self.scroll_4,text="Mesmo do cadastro",command=lambda:self.showEnderecoRecic()).grid(row=0,column=1)

        Button(self.scroll_4,text="Outro endereço",command=lambda:self.createEndereco(),padx=20).grid(row=0,column=2)

    def showEnderecoRecic(self):

        Label(self.scroll_4,text=self.end,font=fonteB).grid(row=3,column=1)

        Label(self.scroll_4,text=self.cep,font=fonteB).grid(row=4,column=1)

        Label(self.scroll_4,text=self.bairro,font=fonteB).grid(row=5,column=1)

        Label(self.scroll_4,text=self.cid,font=fonteB).grid(row=6,column=1)

        Label(self.scroll_4,text=self.uf,font=fonteB).grid(row=7,column=1)

        Label(self.scroll_4, text="Endereço").grid(row=3,column=0)

        Label(self.scroll_4, text="CEP").grid(row=4,column=0)

        Label(self.scroll_4, text="Bairro").grid(row=5,column=0)

        Label(self.scroll_4,text="Cidade").grid(row=6,column=0)

        Label(self.scroll_4, text="UF").grid(row=7,column=0)

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

        Label(self.scroll_5,text="Dados do cliente para orçamento",font=fonteC,padx=100,pady=30).grid(row=0,column=0)

        Label(self.scroll_5,text=self.code,font=fonteB).grid(row=3, column=2)

        Label(self.scroll_5,text=self.data_inicial,font=fonteB).grid(row=4, column=2)

        Label(self.scroll_5,text=self.nome,font=fonteB).grid(row=5, column=2)

        Label(self.scroll_5,text=self.cpf,font=fonteB).grid(row=6, column=2)

        Label(self.scroll_5,text=self.rg,font=fonteB).grid(row=7, column=2)

        Label(self.scroll_5,text=self.mail,font=fonteB).grid(row=8, column=2)

        Label(self.scroll_5,text=self.tel,font=fonteB).grid(row=9, column=2)

        Label(self.scroll_5,text=self.end,font=fonteB).grid(row=10, column=2)

        Label(self.scroll_5,text=self.cep,font=fonteB).grid(row=11, column=2)

        Label(self.scroll_5,text=self.bairro,font=fonteB).grid(row=12, column=2)

        Label(self.scroll_5,text=self.cid,font=fonteB).grid(row=13, column=2)

        Label(self.scroll_5,text=self.uf,font=fonteB).grid(row=14, column=2)

        Label(self.scroll_5,text=self.usuario,font=fonteB).grid(row=15, column=2)

        Label(self.scroll_5,text=self.forma_contato,font=fonteB).grid(row=16, column=2)

        Label(self.scroll_5,text="Dados do cliente").grid(row=2,column=2)

        Label(self.scroll_5,text="Identificação - Código Cliente").grid(row=3,column=0)

        Label(self.scroll_5,text="Data do contato inicial").grid(row=4,column=0)

        Label(self.scroll_5,text="Nome do cliente").grid(row=5, column=0)

        Label(self.scroll_5,text="CPF").grid(row=6,column=0)

        Label(self.scroll_5,text="RG").grid(row=7,column=0)

        Label(self.scroll_5,text="E-mail").grid(row=8,column=0)

        Label(self.scroll_5,text="Contato Telefone/Celular").grid(row=9 , column=0)

        Label(self.scroll_5,text="Endereço").grid(row=10, column=0)

        Label(self.scroll_5,text="CEP").grid(row=11 , column=0)

        Label(self.scroll_5,text="Bairro").grid(row=12 , column=0)

        Label(self.scroll_5,text="Cidade").grid(row=13,column=0)

        Label(self.scroll_5,text="UF").grid(row=14 , column=0)

        Label(self.scroll_5,text="Responsável pelo chamado").grid(row=15,column=0)

        Label(self.scroll_5,text="Forma de contato inicial").grid(row=16,column=0)

    def showPreCliente(self):

        self.master.destroy()

        self.__init__(master=None)

        self.showCode()

        Label(self.master,text="Digite o código do cliente para ver seus dados",font=fonteC,padx=200,pady=30).grid(row=0,column=0)

        self.pre = Entry(self.master)
        self.pre.grid(row=1,column=0)

        Button(self.master,text="Verificar se existe no registro de clientes",command=self.verifyCliente,pady=30).grid()

    def verifyCliente(self):

        with open('arquivo.json') as C:
            data = json.load(C)

        self.pre.real = self.pre.get()

        self.searchCliente()

    def searchCliente(self):

        with open('arquivo.json') as C:
            data = json.load(C)

        self.true_false = ["0"]

        for cliente in data["Clientes"]:
            if cliente['Code'] == self.pre.real:

                self.chargeCliente(self.pre.real)

                Label(self.master,text="Cliente registrado!",font=fonteC,pady=20).grid(row=5,column=0)

                Button(self.master,text="Ver dados",command=self.showCliente,font=fonteC).grid(row=6,column=0)

                self.true_false[0] = "TRUE"

        if self.true_false[0] == "0":

            Label(self.master,text="Cliente não encontrado",font=fonteC).grid(row=5,column=0)

    def showCliente(self):

        self.master.destroy()

        self.__init__(master=None)

        Label(self.master,text=self.code,font=fonteB).grid(row=3, column=2)

        Label(self.master,text=self.data_inicial,font=fonteB).grid(row=4, column=2)

        Label(self.master,text=self.nome,font=fonteB).grid(row=5, column=2)

        Label(self.master,text=self.cpf,font=fonteB).grid(row=6, column=2)

        Label(self.master,text=self.rg,font=fonteB).grid(row=7, column=2)

        Label(self.master,text=self.mail,font=fonteB).grid(row=8, column=2)

        Label(self.master,text=self.tel,font=fonteB).grid(row=9, column=2)

        Label(self.master,text=self.end,font=fonteB).grid(row=10, column=2)

        Label(self.master,text=self.cep,font=fonteB).grid(row=11, column=2)

        Label(self.master,text=self.bairro,font=fonteB).grid(row=12, column=2)

        Label(self.master,text=self.cid,font=fonteB).grid(row=13, column=2)

        Label(self.master,text=self.uf,font=fonteB).grid(row=14, column=2)

        Label(self.master,text=self.usuario,font=fonteB).grid(row=15, column=2)

        Label(self.master,text=self.forma_contato,font=fonteB).grid(row=16, column=2)

        Label(self.master,text="Cliente {0}".format(self.code),font=fonteC,padx=200,pady=30).grid(row=0,column=0)

        Label(self.master,text="Dados do cliente").grid(row=2,column=2)

        Label(self.master,text="Identificação - Código Cliente").grid(row=3,column=0)

        Label(self.master,text="Data do contato inicial").grid(row=4,column=0)

        Label(self.master,text="Nome do cliente").grid(row=5, column=0)

        Label(self.master,text="CPF").grid(row=6,column=0)

        Label(self.master,text="RG").grid(row=7,column=0)

        Label(self.master,text="E-mail").grid(row=8,column=0)

        Label(self.master,text="Contato Telefone/Celular").grid(row=9 , column=0)

        Label(self.master,text="Endereço").grid(row=10, column=0)

        Label(self.master,text="CEP").grid(row=11 , column=0)

        Label(self.master,text="Bairro").grid(row=12 , column=0)

        Label(self.master,text="Cidade").grid(row=13,column=0)

        Label(self.master,text="UF").grid(row=14 , column=0)

        Label(self.master,text="Responsável pelo chamado").grid(row=15,column=0)

        Label(self.master,text="Forma de contato inicial").grid(row=16,column=0)

        Label(self.master,text=" ").grid(row=17,column=0)

        Button(self.master,text="O que já rolou",command=self.showRolou).grid(row=18,column=0)

        Button(self.master,text="Ir para os pedidos",command=self.showClientePedido).grid(row=19,column=0)

    def showRolou(self):

        Label(self.master,text="hahahaha")

    def showClientePedido(self):

        with open('arquivo.json') as C:
            data = json.load(C)

        self.master.destroy()

        self.__init__(master=None)

        self.searchPedidos()

        Label(self.master,text="Pedidos do cliente",font=fonteC,padx=300,pady=30).grid(row=0,column=0)

    def chargeCliente(self,cod):

        with open('arquivo.json') as C:
            data = json.load(C)

        for cliente in data["Clientes"]:
            if cliente["Code"] == cod:
                self.code = cod
                self.data_inicial = cliente["Data do contato inicial"]
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
                self.forma_contato = cliente["Forma de contato"]

    def searchPedidos(self):

        with open('arquivo.json') as C:
            data = json.load(C)

        for cliente in data["Clientes"]:
            if cliente["Code"] == self.code:
                self.pedidos = cliente["Pedidos"]

        self.npedidos = len(self.pedidos)

        for i in range(0,self.npedidos):
            self.pedidoscr = Button(self.master,text="{0}º Pedido".format(self.pedidos[i]["Pedido"]),command=lambda i=i: self.chargePedidos(i),width=50).grid(row=i+1,column=0)

    def chargePedidos(self,mynum):

        self.mynum = mynum+1

        with open('arquivo.json') as C:
            data = json.load(C)

        for i in range(0,self.npedidos):
            if self.mynum == self.pedidos[i]["Pedido"]:
                self.service = self.pedidos[i]["Servico"]
                self.mov = self.pedidos[i]["Moveis"]
                self.insts = self.pedidos[i]["Instituicao de doacao"]
                self.type = self.pedidos[i]["Tipo do imovel"]
                self.dormss = self.pedidos[i]["N de Dormitorios"]
                self.pavs = self.pedidos[i]["N de Pavimentos"]
                self.metrs = self.pedidos[i]["Metragem"]
                self.pints = self.pedidos[i]["Pintura com ou sem teto"]
                self.price = self.pedidos[i]["Valor do Orcamento"]

        self.showPedido()

    def showPedido(self):

        self.master.destroy()

        self.__init__(master=None)

        Label(self.master,text="Dados do pedido",font=fonteC,padx=100,pady=30).grid(row=0,column=0)

        Label(self.master,text=self.code,font=fonteB).grid(row=3, column=2)

        Label(self.master,text=self.mynum,font=fonteB).grid(row=4, column=2)

        Label(self.master,text=self.service,font=fonteB).grid(row=5, column=2)

        Label(self.master,text=self.mov,font=fonteB).grid(row=6, column=2)

        Label(self.master,text=self.insts,font=fonteB).grid(row=7, column=2)

        Label(self.master,text=self.type,font=fonteB).grid(row=8, column=2)

        Label(self.master,text=self.dormss,font=fonteB).grid(row=9, column=2)

        Label(self.master,text=self.pavs,font=fonteB).grid(row=10, column=2)

        Label(self.master,text=self.metrs,font=fonteB).grid(row=11, column=2)

        Label(self.master,text=self.pints,font=fonteB).grid(row=12, column=2)

        Label(self.master,text=self.price,font=fonteB).grid(row=13, column=2)

        Label(self.master, text="Dados do pedido").grid(row=2 , column=2)

        Label(self.master,text="Identificação - Código Cliente").grid(row=3,column=0)

        Label(self.master, text="Pedido de número").grid(row=4, column=0)

        Label(self.master, text="Serviço").grid(row=5 , column=0)

        Label(self.master, text="Com ou sem móveis grandes").grid(row=6 , column=0)

        Label(self.master, text="Instituição de doação").grid(row=7 , column=0)

        Label(self.master, text="Tipo de imóvel").grid(row=8 , column=0)

        Label(self.master, text="Nº de dormitórios").grid(row=9, column=0)

        Label(self.master, text="Nº de pavimentos").grid(row=10 , column=0)

        Label(self.master, text="Metragem (m2)").grid(row=11 , column=0)

        Label(self.master,text="Pintura com ou sem teto").grid(row=12,column=0)

        Label(self.master, text="Valor do orçamento").grid(row=13,column=0)

        Label(self.master,text=" ").grid(row=14,column=0)

        Button(self.master,text="Voltar para o cliente",command=self.showCliente).grid(row=15,column=0)

    def showPrePrestador(self):

        self.master.destroy()

        self.__init__(master=None)

        self.showCodePrestador()

        Label(self.master,text="Digite o código do prestador para ver seus dados",font=fonteC,padx=200,pady=30).grid(row=0,column=0)

        self.prestador = Entry(self.master)
        self.prestador.grid(row=1,column=0)

        Button(self.master,text="Verificar se existe no registro de clientes",command=self.verifyPrestador,pady=30).grid()

    def verifyPrestador(self):

        with open('arquivo.json') as C:
            data = json.load(C)

        self.prestador.real = self.prestador.get()

        self.searchPrestador()

    def searchPrestador(self):

        with open('arquivo.json') as C:
            data = json.load(C)

        self.true_false = ["0"]

        for prestador in data["Prestadores"]:
            if prestador['Code'] == self.prestador.real:

                self.chargePrestador(self.prestador.real)

                Label(self.master,text="Cliente registrado!",font=fonteC,pady=20).grid(row=5,column=0)

                Button(self.master,text="Ver dados",command=self.showPrestador,font=fonteC).grid(row=6,column=0)

                self.true_false[0] = "TRUE"

        if self.true_false[0] == "0":

            Label(self.master,text="Cliente não encontrado",font=fonteC).grid(row=5,column=0)

    def chargePrestador(self,code_prestador):

        with open('arquivo.json') as C:
            data = json.load(C)

        for prestador in data["Prestadores"]:
            if prestador["Code"] == code_prestador:
                self.code_prestador = code_prestador
                self.data_inicial_prestador = prestador["Data do contato inicial"]
                self.empresa = prestador["Nome"]
                self.servico_prestado = prestador["Servico prestado"]
                self.cnpj = prestador["CNPJ"]
                self.telefone = prestador["Telefone de contato"]
                self.endereco_prestador = prestador["Endereco"]
                self.email = prestador["E-mail"]
                self.cep_prestador = prestador["CEP"]
                self.bairro_prestador = prestador["Bairro"]
                self.cidade_prestador = prestador["Cidade"]
                self.uf_prestador = prestador["UF"]
                self.usuario_empresa = prestador["Falar diretamente com"]
                self.forma_contato_prestador = prestador["Forma de contato"]

    def showPrestador(self):

        self.master.destroy()

        self.__init__(master=None)

        Label(self.master,text=self.code_prestador,font=fonteB).grid(row=3, column=2)

        Label(self.master,text=self.data_inicial_prestador,font=fonteB).grid(row=4, column=2)

        Label(self.master,text=self.empresa,font=fonteB).grid(row=5, column=2)

        Label(self.master,text=self.cnpj,font=fonteB).grid(row=6, column=2)

        Label(self.master,text=self.servico_prestado,font=fonteB).grid(row=7, column=2)

        Label(self.master,text=self.email,font=fonteB).grid(row=8, column=2)

        Label(self.master,text=self.telefone,font=fonteB).grid(row=9, column=2)

        Label(self.master,text=self.endereco_prestador,font=fonteB).grid(row=10, column=2)

        Label(self.master,text=self.cep_prestador,font=fonteB).grid(row=11, column=2)

        Label(self.master,text=self.bairro_prestador,font=fonteB).grid(row=12, column=2)

        Label(self.master,text=self.cidade_prestador,font=fonteB).grid(row=13, column=2)

        Label(self.master,text=self.uf_prestador,font=fonteB).grid(row=14, column=2)

        Label(self.master,text=self.usuario_empresa,font=fonteB).grid(row=15, column=2)

        Label(self.master,text=self.forma_contato_prestador,font=fonteB).grid(row=16, column=2)

        Label(self.master,text="Prestador {0}".format(self.code_prestador),font=fonteC,padx=200,pady=30).grid(row=0,column=0)

        Label(self.master,text="Dados do prestador").grid(row=2,column=2)

        Label(self.master,text="Identificação - Código prestador").grid(row=3,column=0)

        Label(self.master,text="Data do contato inicial").grid(row=4,column=0)

        Label(self.master,text="Nome da/do Empresa/Prestador").grid(row=5, column=0)

        Label(self.master,text="CNPJ").grid(row=6,column=0)

        Label(self.master,text="Seriço prestado").grid(row=7,column=0)

        Label(self.master,text="E-mail").grid(row=8,column=0)

        Label(self.master,text="Contato Telefone/Celular").grid(row=9 , column=0)

        Label(self.master,text="Endereço").grid(row=10, column=0)

        Label(self.master,text="CEP").grid(row=11 , column=0)

        Label(self.master,text="Bairro").grid(row=12 , column=0)

        Label(self.master,text="Cidade").grid(row=13,column=0)

        Label(self.master,text="UF").grid(row=14 , column=0)

        Label(self.master,text="Falar diretamente com").grid(row=15,column=0)

        Label(self.master,text="Forma de contato inicial").grid(row=16,column=0)

        Label(self.master,text=" ").grid(row=17,column=0)

    def client_exit(self):
        exit()

        
# Fontes

fonteA = ("Verdana", 8)
fonteB = ("Verdana", 10)
fonteC = ("Verdana", 12)
fonteD = ("Verdana", 16)
fonteE = ("Verdana", 20)
fonteG = ("Times New Roman",20)
fonteH = ("Times New Roman",14)

# root window created. Here, that would be the only window, but
# you can later have windows within windows.
root = Tk()

root.geometry("1200x1024")

aha = ""

#creation of an instance
app = Window(root)

app.showImagemInicial()

app.showTeam()


#mainloop 
root.mainloop()