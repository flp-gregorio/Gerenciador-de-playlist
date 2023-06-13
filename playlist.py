import tkinter as tk
from tkinter import messagebox

class Musica:

    def __init__(self, titulo):
        self.__titulo = titulo
    
    @property
    def titulo(self):
        return self.__titulo
    
    @titulo.getter
    def getTitul(self):
        return self.__titulo


class LimiteInsereMusicas(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('250x100')
        self.title("Musica")
        self.controle = controle

        self.frameNro = tk.Frame(self)
        self.frameNome = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameNro.pack()
        self.frameNome.pack()
        self.frameButton.pack()
      
        self.labelNro = tk.Label(self.frameNro,text="Nro Matrícula: ")
        self.labelNome = tk.Label(self.frameNome,text="Nome: ")
        self.labelNro.pack(side="left")
        self.labelNome.pack(side="left")  

        self.inputNro = tk.Entry(self.frameNro, width=20)
        self.inputNro.pack(side="left")
        self.inputNome = tk.Entry(self.frameNome, width=20)
        self.inputNome.pack(side="left")             
      
        self.buttonSubmit = tk.Button(self.frameButton ,text="Enter")      
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.enterHandler)
      
        self.buttonClear = tk.Button(self.frameButton ,text="Clear")      
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controle.clearHandler)  

        self.buttonFecha = tk.Button(self.frameButton ,text="Concluído")      
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fechaHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteMostraMusicas():
    def __init__(self, str):
        messagebox.showinfo('Lista de Musicas', str)

      
class ctrlPlaylist():       
    def __init__(self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal
        self.listaMusicas = []

    def getMusica(self, titulo):
        mscRet = None
        for msc in self.listaMusicas:
            if msc.getMusica() == titulo:
                mscRet = msc
        return mscRet

    def getListaMusicas(self):
        listaMsc = []
        for msc in self.listaMusicas:
            listaMsc.append(msc.gettitulo())
        return listaMsc

    def insereMusicas(self):
        self.limiteIns = LimiteInsereMusicas(self) 

    def mostraMusicas(self):
        str = 'Nro Matric. -- Nome\n'
        for msc in self.listaMusicas:
            str += msc.getMusica() + ' -- ' + msc.getNome() + '\n'       
        self.limiteLista = LimiteMostraMusicas(str)

    def enterHandler(self, event):
        titulo = self.limiteIns.inputNro.get()
        nome = self.limiteIns.inputNome.get()
        Musica = Musica(titulo, nome)
        self.listaMusicas.append(Musica)
        self.limiteIns.mostraJanela('Sucesso', 'Musica cadastrado com sucesso')
        self.clearHandler(event)

    def clearHandler(self, event):
        self.limiteIns.inputNro.delete(0, len(self.limiteIns.inputNro.get()))
        self.limiteIns.inputNome.delete(0, len(self.limiteIns.inputNome.get()))

    def fechaHandler(self, event):
        self.limiteIns.dmscroy()
    
    def insereMusica(self, event):
        print(" ")

    def mostraPlaylist(self, event):
        print(" ")