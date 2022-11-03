##
#%%
import mutagen.mp3
from abc import ABC,abstractmethod
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import vlc
import time

class Musique(ABC):

    @abstractmethod
    def __init__(self,path:str):
        pass

    @abstractmethod
    def toString(self):
        pass

    @abstractmethod
    def doPlay(self):
        pass


class MusiqueDownload(Musique):
    
    def __init__(self,path:str):
        self.path = path
        self.info = mutagen.mp3.Open(path)
        self.temps = float( self.info.info.pprint().split()[-2] )
        
    def toString(self):
        return self.info.pprint()

    def doPlay(self):
        music = vlc.MediaPlayer(self.path)
        music.play()
        time.sleep(self.temps)
        




class MusiqueSpotify(Musique):
    spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
    def __init__(self,link:str):
        self.path = link
        self



if __name__ == "__main__":
    rick = Musique("/home/smaug/Documents/Projet-MusiquePlaylist/resources/RickRoll.mp3")
    print(rick.toString())
    print(rick.temps,type(rick.temps))
# %%
