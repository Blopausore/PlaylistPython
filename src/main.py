##BASH TO PY
#%%
import sys
import os

path = os.path.realpath(__file__)[:-8]
'''
print(path)
if path not in sys.path:
    sys.path.append(path)
'''

import Playlist
import Compilation

def main(args=sys.argv):

    temps = int(args[1])
    temps_pause = int(args[2])
    mother_playlist = Playlist.Playlist()

    with open(path+"/sources.data",'r') as sources:
        for type_source in sources:
            type_data,source = type_source.split("::")
            playlist = Playlist.Playlist()
            if type_data == "directory":
                playlist.doImportFile(source)
            elif type_data == "spotify":
                pass
        mother_playlist.doMerge(playlist)
    
    Compilation.Compilation(mother_playlist,temps,temps_pause).doPlay()


if __name__ == "__main__":
    sources = open(path+"/sources.data","w")
    sources.write("directory::/home/smaug/Music/test_playtime/")
    sources.close()
    main([0,5,5])
else:
    main()




# %%
