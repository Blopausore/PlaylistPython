#! /bin/bash

if [ "$#" -ne 0 ] && [ "$#" -ne 2 ];then
    echo "Erreur : nombre d'arguments incorrect" 2>/dev/null
    exit 1
fi

exec 4>sources.data
echo "Création du set de musique"

if [ "$#" -eq 2 ];then
    echo $1"::"$2 >&4
    echo -e "\t$1::$2 : ajouter au fichier source"
    
else
    echo -e "\tAttention : vous avez initialisé un set vide"
fi

echo "Création du set : Done"
exit 0