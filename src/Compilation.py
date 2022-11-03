import Playlist
import time

class Compilation:
#Compilation : set of playlist
    def __init__(self,playlist : Playlist, temps : float, temps_pause : float, methode = 1):
        self.playlists = [Playlist]
        self.temps_pause = temps_pause
        if methode == 1:
            self.playlists = playlist.doSplitPlaylist1(temps)

        elif methode == 2:
            self.playlists = playlist.doSplitPlaylist2(temps)


    def doPlay(self):
        for playlist in self.playlists:
            playlist.doPlay()
            time.sleep(self.temps_pause)
            

    


    