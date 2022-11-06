#! /bin/bash 

if [ "$#" -ne 2 ]; then
    echo "Erreur : nombres d'arguments incorrect"
    exit 1
else 
    isnum1="$(expr 0 + "$1" 2>/dev/null)"
    isnum2="$(expr 0 + "$2" 2>/dev/null)"
    if [ -z "$isnum1" ] && [ -z "$isnum2" ]; then
        echo "Erreur : les arguments ne sont pas des entiers"
        exit 1
    fi
fi

python3 src/main.py $@ 

exit 0


