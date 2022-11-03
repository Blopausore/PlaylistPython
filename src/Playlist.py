##
#%%
import os
import Musique
import random
import spotipy

class Playlist:

    def __init__(self):
        self.musiques = [Musique]
        self.temps = 0. #le temps de la playlist en seconde

    def doInit(self,musiques):
        self.musiques = musiques
        self.temps = sum([musiques.temps for musique in musiques])

    def doAddMusique(self,musique:Musique):
        self.temps += musique.temps
        self.musiques.append(musique)
    
    def doImportFile(self,file_path : str, recurrence=True):

        for musique in os.listdir(file_path):
            path=file_path + musique
            if os.path.isdir(path) and recurrence:
                self.doImportFile(self,file_path+musique+"/") #afin de parcouri meme les fichiers présent dans celui mère
            elif  path.split(".")[-1] == "mp3": 
                self.doAddMusique(Musique(file_path+musique)) 
 
    def doImportSpotify(self, playlist_link : str):
        sp = spotipy.Spotify()

    def temps_avg(self):
        return self.temps/len(self.musiques)

## TEST DE DEUX MANIERES DE SPLIT

    def doSplitPlaylist1(self,temps : float):#retourne une liste de playlist 
        compilation = [Playlist]
        random.shuffle(self.musiques)
        temps_avg = self.temps/len(self.musiques)
        pointer = 0
        epsi = 10.

        def core_recu(temps = temps):
            global pointer
            if pointer < len(self.musiques):
                if  abs(temps - self.temps_avg()) < epsi:
                    minimum = abs(temps-self.musiques[pointer].temps)
                    index_minimum = pointer
                    for index,musique in enumerate(self.musiques[pointer:]):
                        if abs(temps-musique.temps) <  minimum:
                            index_minimum = index + pointer + 1
                            minimum = abs(temps-musique.temps)
                    self.musiques[pointer],self.musiques[index_minimum] = self.musiques[index_minimum],self.musiques[pointer]
                    pointer +=1
                    return self.musiques[pointer-1]

                else :
                    pointer+=1
                    return self.musiques[pointer-1] + core_recu(temps)
            else:
                return []
        
        while pointer < len(self.musiques):
            playlist = Playlist().doInit(core_recu(temps))
            if abs(playlist.temps - temps) > epsi:
                break
            else:
                compilation.append(playlist)
        
        return compilation

  
    def doSplitPlaylist2(self,temps : int):
        compilation = [Playlist]
        random.shuffle(self.musiques)
        nbMusique = int( temps * len(self.musiques) / self.temps ) #Nombre de musiques par playlist
        for i in range(int( self.temps//temps )) :
            compilation.append(Playlist())
            compilation[-1].doInit(self.musiques[i*nbMusique : i*(nbMusique+1)])
        return compilation

    
    def doPlay(self):
        for musique in self.musiques:
            musique.doPlay()






# %%
