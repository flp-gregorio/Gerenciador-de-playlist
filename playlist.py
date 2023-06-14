import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class Playlist:
    def __init__(self, titulo, musicas):
        self.__titulo = titulo
        self.__musicas = []
    
    @property
    def titulo(self):
        return self.__titulo
    
    @property
    def musicas(self):
        return self.__musicas

class LimitePlaylist(tk.Toplevel):
    def __init__(self, controle, listaArtista, listaAlbum):
        tk.Toplevel.__init__(self)
        self.geometry('500x250')
        self.title("Album")
        self.controle = controle
        self.listaAlbum = listaAlbum

        # album
        self.frameNome = tk.Frame(self)
        self.frameDiscip = tk.Frame(self)
        self.frameEstudante = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameButton2 = tk.Frame(self)
        # album
        self.frameNome.pack()
        self.frameDiscip.pack()
        self.frameEstudante.pack()
        self.frameButton.pack()  
        self.frameButton2.pack()  

        self.labelNome = tk.Label(self.frameNome,text="Nome da playlist: ")
        self.labelNome.pack(side="left")  
        self.inputNome = tk.Entry(self.frameNome, width=20)
        self.inputNome.pack(side="left") 

        self.labelDiscip = tk.Label(self.frameDiscip, text="Escolha o artista: ")
        self.labelDiscip.pack(side="left")

        self.escolhaCombo = tk.StringVar()
        self.combobox = ttk.Combobox(self.frameDiscip, width=15, textvariable=self.escolhaCombo)
        self.combobox.pack(side="left")
        self.combobox['values'] = listaArtista
        self.combobox.bind("<<ComboboxSelected>>", self.filter_listbox)  # Bind the function to the event

        self.labelEst = tk.Label(self.frameEstudante, text="Escolha as musicas: ")
        self.labelEst.pack(side="left")
        self.listbox = tk.Listbox(self.frameEstudante)
        self.listbox.pack(side="left")   

        self.buttonConcluir = tk.Button(self.frameButton, text="Inserir Música", command=self.controle.insereMusica)           
        self.buttonConcluir.pack(side="bottom")

        self.buttonCriar = tk.Button(self.frameButton, text="Criar Playlist", command=self.controle.criaPlaylist)           
        self.buttonCriar.pack(side="bottom")

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)    

    def filter_listbox(self, event):
        selected_artist = self.escolhaCombo.get()
        self.listbox.delete(0, tk.END)  # Clear the listbox

        for album in self.listaAlbum:
            if selected_artist == album.artista.nome:
                for msc in album.musica:
                    self.listbox.insert(tk.END, msc.titulo)
       

class LimiteMostraAlbums():
    def __init__(self, str):
        messagebox.showinfo('Lista de Álbuns', str)

class ctrlPlaylist():
    def __init__(self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal
        self.playlists = []
        self.listaMusicas = []


    def inserePlaylist(self):
        listaArtista = self.ctrlPrincipal.ctrlArtista.getListaArtistas()
        listaMusica = self.ctrlPrincipal.ctrlAlbum.getAlbums()
        self.limitePlaylist = LimitePlaylist(self, listaArtista, listaMusica)

    def criaPlaylist(self):
        nome = self.limitePlaylist.inputNome.get()

        if not nome:
            self.limitePlaylist.mostraJanela('Erro', 'Digite um nome para a playlist')
            return

        for playlist in self.playlists:
            if playlist.titulo == nome:
                self.limitePlaylist.mostraJanela('Erro', 'Já existe uma playlist com esse nome')
                return

        novaPlaylist = Playlist(nome, None)
        self.playlists.append(novaPlaylist)
        self.limitePlaylist.mostraJanela('Sucesso', 'Playlist criada com sucesso')

    def insereMusica(self):

        if not self.playlists:
            self.LimitePlaylist.mostraJanela('Erro', 'Nenhuma playlist foi criada')
            return
        
        msc = self.limitePlaylist.listbox.get(tk.ACTIVE)

        if not msc:
            self.limitePlaylist.mostraJanela('Erro', 'Selecione uma música para inserir na playlist')
            return

        pl = self.playlists[-1]
        pl.musicas.append(msc)
        self.limitePlaylist.mostraJanela('Sucesso', 'Música inserida')
        self.limitePlaylist.listbox.delete(tk.ACTIVE)
    
    def mostraPlaylist(self):
        output = ''
        for playlist in self.playlists:
            output += 'Titulo: ' + playlist.titulo + '\n'
            output += 'Musicas:\n'
            for msc in playlist.musicas:  # Iterate over the song titles
                output += msc + '\n'  # Access the song title directly
            output += '------\n'

        self.limiteLista = LimiteMostraAlbums(output)


    def concluir(self, event):
        self.LimitePlaylist.destroy()
    