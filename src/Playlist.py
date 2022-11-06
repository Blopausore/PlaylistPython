##
#%%

import os
import random
import spotipy
import Musique

class Playlist(Musique.Musique):
#Playlist : a set of music
    def __init__(self):
        self.musiques = []
        self.temps = 0. #le temps de la playlist en seconde
    
    @staticmethod
    def len(self):
        return len(playlist.musiques)

    def doInit(self, musiques : list[Musique.Musique]):
        self.musiques = musiques
        self.temps = sum([musique.temps for musique in musiques])
        

    def doAddMusique(self,musique):
        self.temps += musique.temps
        self.musiques.append(musique)


    def doImportFile(self,file_path : str, recurrence=True):
        for musique in os.listdir(file_path):
            path=file_path + musique
            if os.path.isdir(path) and recurrence:
                self.doImportFile(file_path+musique+"/") #afin de parcouri meme les fichiers présent dans celui mère
            elif  path.split(".")[-1] == "mp3": 
                self.doAddMusique(Musique.MusiqueDownload(file_path+musique)) 
 
    def __iter__(self):
        self.i = 0
        return self
    
    def __next__(self):
        i = self.i 
        if i == len(self.musiques):
            raise StopIteration
        self.i +=1
        return self.musiques[i]



    def doMerge(self, other):
        self.musiques.extend(other.musiques)
        self.temps+=other.temps

    def toString(self) -> str:
        return "\n".join([musique.toString() for musique in self.musiques])

    def temps_avg(self):
        return self.temps/len(self.musiques)

## TEST DE DEUX MANIERES DE SPLIT
    """doSplitPlaylist
    Subdivise une playlist en sous-playlist aléatoire de durée donnée 
    Parametre 
        temps : float
            Durée des sous playlists créer 
    Retour
        compilation : [Playlist]
            Une liste de sous playlist issu de la playlist mère. Cette liste sert seulement à la création 
            du type compilation. (cf class compilation)
    """
    def doSplitPlaylist2(self):
        print("Création de la compile : une musique par playlists")
        compile =[]
        for musique in self.musiques:
            playlist = Playlist()
            playlist.doAddMusique(musique)
            compile.append(playlist)
        return compile


    def doSplitPlaylist1(self,temps : float):#retourne une liste de playlist 

        compilation = []
        random.shuffle(self.musiques)
        temps_avg = self.temps/len(self.musiques)
        global pointer
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
                    return [self.musiques[pointer-1]] + core_recu(temps)
            else:
                return []
        
        while pointer < len(self.musiques):
            playlist = Playlist()
            playlist.doInit(core_recu(temps))

            if playlist.temps == 0 or abs(playlist.temps - temps) > epsi:
                break
            else:
                temps-=playlist.temps
                compilation.append(playlist)
        
        return compilation

    """
    def doSplitPlaylist2(self,temps : int):
        compilation = []
        random.shuffle(self.musiques)
        nbMusique = int( temps * len(self.musiques) / self.temps ) #Nombre de musiques par playlist
        for i in range(int( self.temps//temps )) :
            compilation.append(Playlist())
            compilation[-1].doInit(self.musiques[i*nbMusique : i*(nbMusique+1)])
        return compilation

    """ 

#Play the musics in playlist 
    def doPlay(self):
        for musique in self.musiques:
            musique.doPlay()


 # %%

if __name__ == "__main__":
    playlist = Playlist()
    playlist.doImportFile("/home/smaug/Music/test_playtime/")
    playlists = playlist.doSplitPlaylist2()
    print(len(playlists))
    for playlist_ in playlists:
        print("Blop :", Playlist.len(playlist_))
        print(playlist_.toString())


# %%

if __name__ == "__main__":
    playlist = Playlist()
    playlist.doImportFile("/home/smaug/Music/test_playtime/")

    for musique in playlist:
        print(musique.toString())

# %%
