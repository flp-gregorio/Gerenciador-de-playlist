import tkinter as tk
from tkinter import messagebox
import playlist as plt
import artista as art
import album as alb

class LimitePrincipal():
    def __init__(self, root, controle):
        self.controle = controle
        self.root = root
        self.root.geometry('300x250')
        self.menubar = tk.Menu(self.root)        
        self.AlbumMenu = tk.Menu(self.menubar)
        self.ArtistaMenu = tk.Menu(self.menubar)
        self.PlaylistMenu = tk.Menu(self.menubar)     

        self.AlbumMenu.add_command(label="Insere", \
                    command=self.controle.insereAlbum)
        self.AlbumMenu.add_command(label="Mostra", \
                    command=self.controle.mostraAlbum)
        self.menubar.add_cascade(label="Álbum", \
                    menu=self.AlbumMenu)

        self.ArtistaMenu.add_command(label="Insere", \
                    command=self.controle.insereArtista)
        self.ArtistaMenu.add_command(label="Mostra", \
                    command=self.controle.mostraArtista)        
        self.menubar.add_cascade(label="Artista", \
                    menu=self.ArtistaMenu)

        self.PlaylistMenu.add_command(label="Insere", \
                    command=self.controle.inserePlaylist)
        self.PlaylistMenu.add_command(label="Mostra", \
                    command=self.controle.mostraPlaylist)                     
        self.menubar.add_cascade(label="Playlist", \
                    menu=self.PlaylistMenu)        

        self.root.config(menu=self.menubar)

      
class ControlePrincipal():       
    def __init__(self):
        self.root = tk.Tk()

        self.ctrlAlbum = alb.ctrlAlbum(self)
        self.ctrlArtista = art.ctrlArtista(self)
        self.ctrlPlaylist = plt.ctrlPlaylist(self)

        self.limite = LimitePrincipal(self.root, self) 

        self.root.title("Exemplo MVC")
        # Inicia o mainloop
        self.root.mainloop()
       
    def insereArtista(self):
        self.ctrlArtista.insereArtista()

    def mostraArtista(self):
        self.ctrlArtista.mostraArtistas()
 
    def insereAlbum(self):
        self.ctrlAlbum.insereAlbum()

    def mostraAlbum(self):
        self.ctrlAlbum.mostraAlbum()

    def inserePlaylist(self):
        self.ctrlPlaylist.insereMusica()

    def mostraPlaylist(self):
        self.ctrlPlaylist.mostraPlaylist()

if __name__ == '__main__':
    c = ControlePrincipal()