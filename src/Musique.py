##
#%%

import mutagen.mp3
from abc import ABC,abstractmethod
#import spotipy
#from spotipy.oauth2 import SpotifyClientCredentials
import vlc
import time
import playsound

class Musique(ABC):
    
    @abstractmethod
    def __init__(self,path:str) -> None:
        self.temps = 0
        self.path = path
        self.info = "" 

    #return a string describtive of the musique
    @abstractmethod
    def toString(self) -> str:
        pass
    #play the music
    @abstractmethod
    def doPlay(self) -> None:
        pass


class MusiqueDownload(Musique):
    
    def __init__(self,path:str):
        super().__init__(path)
        self.info = mutagen.mp3.Open(path)
        self.temps = float( self.info.info.pprint().split()[-2] )
        
    def toString(self):
        return self.info.pprint()[:42]

    def doPlay(self):
        playsound.playsound(self.path)


 
# %%
if __name__ == "__main__":
    musique = MusiqueDownload("/home/smaug/Music/test_playtime/Maxence - Comme tu le regardes (Eels cover).mp3")
    print(musique.toString())
    
# %%
