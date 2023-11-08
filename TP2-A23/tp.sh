#!/bin/bash

: <<'COMMENT'
Utilisation
	tp.sh -a [glouton | progdyn | proba] -e [path_vers_exemplaire]

Arguments optionnels
	-p affiche les blocs utilisés dans la construction de la tour chacun sur une ligne (hauteur, largeur, profondeur) en commençant par le bas.
	-H affiche la hauteur totale atteinte par la tour.
	-t affiche le temps d’exécution en ms, sans unité ni texte superflu 
Important: l’option -e doit accepter des fichiers avec des paths absolus.

COMMENT

is_a=1
is_e=1
is_p=1
is_H=1
is_t=1

#Get arguments given with options
while getopts "a:e:pht" opt; do
    case $opt in
        a)
            sort=$OPTARG
            if [ "$sort" != "glouton" ] && [ "$sort" != "progdyn" ] && [ "$sort" != "proba" ]; then
                echo "Invalid value for -a. It should be one of: [glouton | progdyn | proba]"
                exit 1
            fi
            is_a=0
            ;;
        e)
            path=$OPTARG
            if [[ ! -f "$path" ]]; then
                echo "Invalid path"
                exit 1
            fi
            is_e=0
            ;;
        p)
            is_p=0
            ;;
        h)
            is_H=0
            ;;
        t)
            is_t=0
            ;;
        \?)
            echo "Invalid option: -$OPTARG" >&2
            exit 1
            ;;
    esac
done

#Check the presence of mandatory options
if [ $is_a -eq 1 ]; then
    echo "-a is missing"
    exit 1
fi
if [ $is_e -eq 1 ]; then
    echo "-e is missing"
    exit 1
fi

#Execute the algorithm
if [ $is_p -eq 0 ]  && [ $is_H -eq 0 ] && [ $is_t -eq 0 ]; then
    python3 main.py -a $sort -e "$path" -p -H -t
elif [ $is_p -eq 0 ]  && [ $is_H -eq 0 ] && [ $is_t -eq 1 ]; then
    python3 main.py -a $sort -e "$path" -p -H 
elif [ $is_p -eq 0 ]  && [ $is_H -eq 1 ] && [ $is_t -eq 0 ]; then
    python3 main.py -a $sort -e "$path" -p -t 
elif [ $is_p -eq 0 ]  && [ $is_H -eq 1 ] && [ $is_t -eq 1 ]; then
    python3 main.py -a $sort -e "$path" -p 
elif [ $is_p -eq 1 ]  && [ $is_H -eq 0 ] && [ $is_t -eq 0 ]; then
    python3 main.py -a $sort -e "$path" -H -t
elif [ $is_p -eq 1 ]  && [ $is_H -eq 0 ] && [ $is_t -eq 1 ]; then
    python3 main.py -a $sort -e "$path" -H
elif [ $is_p -eq 1 ]  && [ $is_H -eq 1 ] && [ $is_t -eq 0 ]; then
    python3 main.py -a $sort -e "$path" -t
else  
    python3 main.py -a $sort -e "$path" 
fi