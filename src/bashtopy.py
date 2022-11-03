#BASH TO PY
import sys
import Compilation
import Playlist

def main():
    path = "../"
    temps = int(sys.argv[1])
    temps_pause = int(sys.argv[2])
    mother_playlist = Playlist()

    with open("../sources.data",'r') as sources:
        for type_source in sources:
            type_data,source = type_source.split("::")
            playlist = Playlist()
            if type_data == "directory":
                playlist.doImportFile(source)
            elif type_data == "spotify":
                pass
        mother_playlist.doMerge(playlist)
    
    Compilation(mother_playlist,temps,temps_pause).play()
main()




