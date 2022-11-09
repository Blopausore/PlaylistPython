##
#%%

import mutagen.mp3
from abc import ABC,abstractmethod
import spotipy
#from spotipy.oauth2 import SpotifyClientCredentials
import playsound

class Musique(ABC):
    """Objet Musique
    CHAMPS
    ------
    temps : int | float
        Durée de la musique
    path : str
        Moyen d'accès à la musique
    info : str
        Information supplémentaire sur la musique
    """ 
    @abstractmethod

    def __init__(self,path:str) -> None:
        self.temps = 0 
        self.path = path
        self.info = "" 

    
    @abstractmethod
    def toString(self) -> str: 
        """Retourne le string reprénsatif de la musique
        Returns
        -------
             : str
             Information sur la musique
        """
        pass
    #Joue la musique

    @abstractmethod
    def doPlay(self) -> None:
        """Joue la Musique"""
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

class MusiqueSpotify(Musique):

    def __init__(self,link:str):
        super().__init__(link)

         
 
# %%
if __name__ == "__main__":
    musique = MusiqueDownload("/home/smaug/Music/test_playtime/Maxence - Comme tu le regardes (Eels cover).mp3")
    print(musique.toString())
    
# %%
