##
#%%
import mutagen.mp3
from abc import ABC,abstractmethod
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import vlc
import time
import playsound

class Musique(ABC):
    
    @abstractmethod
    def __init__(self,path:str):
        pass
    #return a string describtive of the musique
    @abstractmethod
    def toString(self):
        pass
    #play the music
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
        playsound.playsound(self.path)
    
        

class MusiqueSpotify(Musique):
    spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

    def __init__(self,link:str):
        self.path = link



