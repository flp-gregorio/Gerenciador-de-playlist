import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os.path
import pickle

class Musica:
    def __init__(self, nroMusica, titulo):
        self.__nroMusica = nroMusica
        self.__titulo = titulo

    @property
    def nroMusica(self):
        return self.__nroMusica
    
    @property
    def titulo(self):
        return self.__titulo
    
class Album:

    def __init__(self, ano, titulo, artista, musica):
        self.__ano = ano
        self.__titulo = titulo
        self.__artista = artista
        self.__musica = musica
        
    @property
    def ano(self):
        return self.__ano

    @property
    def titulo(self):
        return self.__titulo

    @property
    def artista(self):
        return self.__artista
    
    @property
    def musica(self):
        return self.__musica

class LimiteInsereAlbum(tk.Toplevel):
    def __init__(self, controle, listaCodDiscip):

        tk.Toplevel.__init__(self)
        self.geometry('500x250')
        self.title("Album")
        self.controle = controle

        #album
        self.frameAnoAlbum = tk.Frame(self)
        self.frameCodAlbum = tk.Frame(self)
        self.frameDiscip = tk.Frame(self)
        self.frameEstudante = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        #musica
        self.frameNome = tk.Frame(self)
        self.frameButton2 = tk.Frame(self)
        #concluir 
        self.frameButton3 = tk.Frame(self)

        #album
        self.frameAnoAlbum.pack()
        self.frameCodAlbum.pack()
        self.frameDiscip.pack()
        self.frameEstudante.pack()
        self.frameButton.pack()  
        #musica
        self.frameNome.pack()
        self.frameButton2.pack()
        #concluir 
        self.frameButton3.pack()

        self.labelAnoAlbum = tk.Label(self.frameAnoAlbum,text="Informe o ano do álbum: ")
        self.labelAnoAlbum.pack(side="left")
        self.inputAnoAlbum = tk.Entry(self.frameAnoAlbum, width=20)
        self.inputAnoAlbum.pack(side="left")

        self.labelCodAlbum = tk.Label(self.frameCodAlbum,text="Informe o nome do álbum: ")
        self.labelCodAlbum.pack(side="left")
        self.inputCodAlbum = tk.Entry(self.frameCodAlbum, width=20)
        self.inputCodAlbum.pack(side="left")

        self.labelDiscip = tk.Label(self.frameDiscip,text="Escolha o artista: ")
        self.labelDiscip.pack(side="left")
        self.escolhaCombo = tk.StringVar()
        self.combobox = ttk.Combobox(self.frameDiscip, width = 15 , textvariable = self.escolhaCombo)
        self.combobox.pack(side="left")
        self.combobox['values'] = listaCodDiscip
          
        self.labelNome = tk.Label(self.frameNome,text="Nome da música: ")
        self.labelNome.pack(side="left")  

        self.inputNome = tk.Entry(self.frameNome, width=20)
        self.inputNome.pack(side="left")            

        self.buttonCria = tk.Button(self.frameButton ,text="Cria Album")           
        self.buttonCria.pack(side="bottom")
        self.buttonCria.bind("<Button>", controle.criaAlbum)  

        self.buttonInsere = tk.Button(self.frameButton2 ,text="Insere Música")           
        self.buttonInsere.pack(side="bottom")
        self.buttonInsere.bind("<Button>", controle.insereMusica)

        self.buttonConcluir = tk.Button(self.frameButton3 ,text="Concluir")           
        self.buttonConcluir.pack(side="bottom")
        self.buttonConcluir.bind("<Button>", controle.salvaAlbums)
        self.buttonConcluir.bind("<Button>", controle.concluir)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)            

class LimiteMostraAlbums():
    def __init__(self, str):
        messagebox.showinfo('Lista de Álbuns', str)

class ctrlAlbum():
    def __init__(self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal
        self.listaMusicas = []
        if not os.path.isfile("album.pickle"):
            self.listaAlbum =  []
        else:
            with open("album.pickle", "rb") as f:
                self.listaAlbum = pickle.load(f)

    def salvaAlbums(self):
        if len(self.listaAlbum) != 0:
            with open("album.pickle","wb") as f:
                pickle.dump(self.listaAlbum, f)


    def insereAlbum(self):        
        self.listaAlunosAlbum = []
        listaCodDisc = self.ctrlPrincipal.ctrlArtista.getListaArtistas()
        if len(listaCodDisc) == 0:
            messagebox.showinfo('Erro','Nenhum artista encontrado')
            self.limiteIns.destroy()
        self.limiteIns = LimiteInsereAlbum(self, listaCodDisc)

    def criaAlbum(self, event):
        anoAlbum = self.limiteIns.inputAnoAlbum.get()
        codAlbum = self.limiteIns.inputCodAlbum.get()
        discSel = self.limiteIns.escolhaCombo.get()
        disc = self.ctrlPrincipal.ctrlArtista.getArtista(discSel)
        
        # Verifica se o álbum já existe na lista de álbuns
        for album in self.listaAlbum:
            if album.titulo == codAlbum:
                self.limiteIns.mostraJanela('Erro', 'Já existe um álbum com esse nome')
                return
        
        album = Album(anoAlbum, codAlbum, disc, list(self.listaMusicas))
        self.listaAlbum.append(album)
        self.limiteIns.mostraJanela('Sucesso', 'Álbum criado com sucesso')
        self.limiteIns.buttonInsere.config(state='normal')
        self.limiteIns.buttonCria.config(state='disabled')

    def insereMusica(self, event):
        nome = self.limiteIns.inputNome.get()

        # Verifica se o álbum está sendo criado
        if len(self.listaAlbum) == 0:
            self.limiteIns.mostraJanela('Erro', 'Crie um álbum primeiro')
            return
        
        album = self.listaAlbum[-1]  # Pega o último álbum da lista


        musica = Musica(len(album.musica) + 1, nome)
        album.musica.append(musica)
        self.limiteIns.mostraJanela('Sucesso', 'Música número ' + str(len(album.musica)) + ' cadastrado com sucesso')
        self.clearHandlerMusica(event)
        self.mostraAlbum

    def clearHandlerMusica(self, event):
        self.limiteIns.inputNome.delete(0, len(self.limiteIns.inputNome.get()))
    
    def getAlbums(self):
        listaAlbums = []
        for album in self.listaAlbum:
            print(album.artista.nome)
            listaAlbums.append(album)
        return listaAlbums

    def mostraAlbum(self):
        output = ''
        for alb in self.listaAlbum:
            output += 'Autor: ' + alb.artista.nome + '\n'
            output += 'Ano: ' + alb.ano + '\n'
            output += 'Titulo: ' + alb.titulo + '\n'
            output += 'Musicas:\n'
            for msc in alb.musica:
                nome = str(msc.titulo)
                num = str(msc.nroMusica)
                output += num + ' - ' + nome + '\n'
            output += '------\n'

        self.limiteLista = LimiteMostraAlbums(output)
    
    def concluir(self, event):
        self.limiteIns.destroy()
    