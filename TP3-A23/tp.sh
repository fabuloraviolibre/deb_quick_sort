#!/bin/bash

: <<'COMMENT'
Utilisation
	tp.sh -e [chemin_vers_exemplaire] [-p]


	Lorsque le script est exécuté sans le paramètre -p, le programme affiche uniquement 
    le nombre d’élèves dont la vue est obstruée plus le nombre de paires incompatibles 
    (multiplié par 10) sur une nouvelle ligne, à chaque fois qu’une meilleure solution est trouvée.

    Argument optionnel
        -p : Chaque fois qu’une meilleure solution est trouvée, 
        le programme affiche cette nouvelle solution.

COMMENT

is_e=1
is_p=1

#Get arguments given with options
while getopts "e:p" opt; do
    case $opt in
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
        \?)
            echo "Invalid option: -$OPTARG" >&2
            exit 1
            ;;
    esac
done

#Check the presence of mandatory options
if [ $is_e -eq 1 ]; then
    echo "-e is missing"
    exit 1
fi

#Execute the algorithm
if [ $is_p -eq 0 ]; then
    python3 main.py -e "$path" -p
else  
    python3 main.py -e "$path" 
fi