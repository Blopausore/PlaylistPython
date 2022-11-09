#! /bin/bash

if [ "$#" -ne 2 ];then
    echo "Erreur : nombre d'arguments incorrect" 2>/dev/null
    exit 1
fi

if [ "$1" == "directory" ] && [ -f "$2" ]; then
    echo "Erreur : le dossier n'existe pas"
    exit 1
fi

exec 4>>sources.data

echo $1"::"$2 >&4
echo -e "\t$1::$2 : ajouter au fichier source"

exit 0
