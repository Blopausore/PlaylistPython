#SubPlaylist-Generator
from abc import ABC,abstractmethod
import Playlist
import random
class SubPlaylistGenerator_(ABC):
    def __init__(self):
        pass

    def __iter__(self):
        pass

    def __next__(self):
        pass



class SubPlaylistGenerator(ABC):
    def __init__(self,playlist : Playlist.Playlist,temps : float | int):
        self.playlist = playlist
        random.shuffle(playlist)
        self.temps = temps
        
        
        
    def subPossible(self,debut : int) -> float:
        """Give the time of the best sub-playlist possible that begin at debut
        PARAMETER
        ---------
            debut : int
                Index of the start of the sub
        RETURN
        ------
            time : float
                The time of this playlist
        """
        fin = (debut + 1) % len(self.playlist)
        s = self.playlist.musiques[debut].temps
        e = self.playlist.musiques[fin].temps
        while abs(self.temps - s) > abs(self.temps - (e+s)):
            if fin == debut :
                break
            s+=e
            fin+=1
            e=self.playlist.musiques[fin].temps
        return s





    def __iter__(self):
        self.i = 0
        self.s = 0
        return self

    def __next__(self):
        if self.playlist
