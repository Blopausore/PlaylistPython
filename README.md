Clarification du projet musique-playlist :
	Créer et joue des sous-playlists créer de manière aléatoire d'un temps donnée et créer des
	pauses aux temps voulus.
	


sources : data file
	Ou sera initialisé les sources pour formé le set de musique sur lequel on travaille

playTime : 
	bash utilitaire, il regroupera les commandes possibles a effectuer.
		Usage : playtime [option]

	option : 
		create [type] [source] : créer le set de musique issu de la source [source]
			type : spotify | directory 
			source :
				spotify : liens vers une playlist (/alubm ?)
				directory : chemin absolu vers un dossier contenant les musiques

		add [type] [source] : ajoute une nouvelle source aux set de musiques actuel (type et source voir précédemment)

		play [temps] [temps_pause]: divise le set de musiques en sous playlist de durée [temps] (créer une compilation) avec une durée de pause de [temps_pause] puis joue la ou les playlists 

	Les temps sont à donner en minutes et en valeur entière.



idée de mise à jour :
	Donné un nom et garder en mémoire un set de musiques.


