##
#%%
import src.Musique

rick = MusiqueDownload("/home/smaug/Documents/Projet-MusiquePlaylist/resources/RickRoll.mp3")
print(rick.toString())
print(rick.temps,type(rick.temps))
rick.doPlay()
