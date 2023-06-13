import tkinter as tk
from tkinter import messagebox

class Artista:

    def __init__(self, nome):
        self.__nome = nome
    
    @property
    def nome(self):
        return self.__nome
    
class LimiteInsereArtistas(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('250x100')
        self.title("Artista")
        self.controle = controle

        self.frameNome = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameNome.pack()
        self.frameButton.pack()
      
        self.labelNome = tk.Label(self.frameNome,text="Nome: ")
        self.labelNome.pack(side="left")  

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

class LimiteMostraArtistas():
    def __init__(self, str):
        messagebox.showinfo('Lista de Artistas', str)

      
class ctrlArtista():       
    def __init__(self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal
        self.listaArtistas = []

    def getArtista(self, nome):
        mscRet = None
        for msc in self.listaArtistas:
            if msc.nome == nome:
                mscRet = msc
        return mscRet

    def getListaArtistas(self):
        listaArt = []
        for art in self.listaArtistas:
            listaArt.append(art.nome)
        return listaArt

    def insereArtista(self):
        self.limiteIns = LimiteInsereArtistas(self) 

    def mostraArtistas(self):
        artists_str = 'Artistas: \n'
        for art in self.listaArtistas:
            artists_str += art.nome + '\n'
        self.limiteLista = LimiteMostraArtistas(artists_str)

    def enterHandler(self, event):
        nome = self.limiteIns.inputNome.get()
        artista = Artista(nome)
        self.listaArtistas.append(artista)
        self.limiteIns.mostraJanela('Sucesso', 'Artista cadastrado com sucesso')
        self.clearHandler(event)
    
    def consultaArtistaPorNome(self, nome):
        artistas_encontrados = []
        for artista in self.listaArtistas:
            if artista.nome == nome:
                artistas_encontrados.append(artista)
        return artistas_encontrados


    def clearHandler(self, event):
        self.limiteIns.inputNome.delete(0, len(self.limiteIns.inputNome.get()))

    def fechaHandler(self, event):
        self.limiteIns.destroy()