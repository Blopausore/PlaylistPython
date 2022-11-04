#! /bin/bash

if [ "$#" -eq 0 ]; then
    ./readme.sh
    exit 1
fi
path=$0
command=$1
shift 1
case $command in
    "create")
        ./command/create.sh $@;;
    "add")
        ./command/add.sh $@;;
    "split")
        ./command/split.sh $@;;
    "play")
        ./command/play.sh $@;;
    "help")
        ./readme.sh;;
    *)
        echo "Erreur : Argument inexistant" 2>/dev/null;
esac



exit 1