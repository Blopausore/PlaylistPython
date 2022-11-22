# projet musique-playlist :

## Description
A partir d'une bilbiothèque de musiques, ce programme permet de créer et jouer des sous-playlists d'une durée précise. Il est possible générer plusieurs sous-playlist séparé d'un temps de pause donné.

### Exemples
* Joue sous-playlist A 
* Pause de 5 minutes
* Joue sous-playlist B
* ...
## Commandes 

### Source
Les musiques sont employées en important une ou plusieurs sources de différent types.
Les différents type de sources qui sont ou seront mis en place :
* directory : Dossier contenant des musiques (et l'ensemble de ses sous-dossiers) (Opérationnel)
* spotify : Artiste, album et playlist spotify 
* deezer, youtube, ... : a envisager  
  
### Command

* playtime [type source] [source]  : Initialise le programme et ajoute éventuellement une source si elle a bien était mis en argument
* add [type source] [source] : Ajoute une source 
* play [temps] [temps_pause] : divise le set de musiques en sous playlist de durée [temps] (créer une compilation) avec une durée de pause de [temps_pause] puis joue la ou les playlists  


Les temps sont à donner en minutes et en valeur entière.

## Road Map


idée de mise à jour :
	Donné un nom et garder en mémoire un set de musiques.


