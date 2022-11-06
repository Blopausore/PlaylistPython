##
#%%
import time
import Playlist
import Musique

class Compilation(Playlist.Playlist):
#Compilation : set of playlist
    def __init__(self,playlist : Playlist.Playlist, temps : float, temps_pause : float, methode = 1):
        self.temps_pause = temps_pause
        if methode == 1:
                
            print("Création de la compile : une musique par playlists")
            compile =[]
            for musique in playlist.musiques:
                playlist_ = Playlist.Playlist()
                playlist_.doAddMusique(musique)
                compile.append(playlist_)
            self.playlists = compile

        elif methode == 2:
            self.playlists = playlist.doSplitPlaylist2(temps)
        print("Compilation créer :")
        print("\t",len(self.playlists))
        print(type(self.playlists[0]))

    def __iter__(self):
        self.iter=iter(self.playlists)
        return self
    
    def __next__(self):
        playlist = next(self.iter)
        return playlist

    def doPlay(self):
        for playlist in self.playlists:
            playlist.doPlay()
            time.sleep(self.temps_pause)
            
    def toString(self):
        "\n".join([playlist.toString() for playlist in self.playlists])
    

# %%


if __name__ == "__main__":
    playlist = Playlist.Playlist()
    playlist.doImportFile("/home/smaug/Music/test_playtime/")
    compilation = Compilation(playlist,3,3,1)
    print("OUI : ",len(compilation.playlists))
    
    for playlist_ in compilation.playlists:
        print(type(playlist_))
        print(playlist_.toString())  
    compilation.doPlay()

# %%

if __name__ == "__main__":
    playlist = Playlist.Playlist()
    playlist.doImportFile("/home/smaug/Music/test_playtime/")
    compilation = Compilation(playlist,1,1,1)
    print(len(compilation.playlists))
    for playlist in compilation:
        print("oui")
#        print(playlist.toString())  


# %%
