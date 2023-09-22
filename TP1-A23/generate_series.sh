#!/bin/bash


#Reset the samples fold
if [ -d "samples" ]; then
    rm -r samples
fi
mkdir samples

#Create all folds needed
for i in {1..4}; do
    for j in {1..4}; do
        mkdir -p "samples/serie$i/gen$j"
    done
done


#Remark: for every serie, every generation has 10 samples
#Important to have magnitude higher than size

#Generate series n°1 - size: 50000-100000-200000-400000, magnitude: 1000000
python3 gen.py -s 50000  -n 10 -m 1000000 -r 1001
mv -v ./samples/sample* ./samples/serie1/gen1/
python3 gen.py -s 100000  -n 10 -m 1000000 -r 1002
mv -v ./samples/sample* ./samples/serie1/gen2/
python3 gen.py -s 200000  -n 10 -m 1000000 -r 1003
mv -v ./samples/sample* ./samples/serie1/gen3/
python3 gen.py -s 400000  -n 10 -m 1000000 -r 1004
mv -v ./samples/sample* ./samples/serie1/gen4/

#Generate series n°2 - size: 50000, magnitude: 500000-1000000-2000000-4000000
python3 gen.py -s 50000  -n 10 -m 500000 -r 2001
mv -v ./samples/sample* ./samples/serie2/gen1/
python3 gen.py -s 50000  -n 10 -m 1000000 -r 2002
mv -v ./samples/sample* ./samples/serie2/gen2/
python3 gen.py -s 50000  -n 10 -m 2000000 -r 2003
mv -v ./samples/sample* ./samples/serie2/gen3/
python3 gen.py -s 50000  -n 10 -m 4000000 -r 2004
mv -v ./samples/sample* ./samples/serie2/gen4/

#Generate series n°3 - size: 50000-100000-200000-400000, magnitude: 500000-1000000-2000000-4000000
python3 gen.py -s 50000  -n 10 -m 500000 -r 3001
mv -v ./samples/sample* ./samples/serie3/gen1/
python3 gen.py -s 100000  -n 10 -m 1000000 -r 3002
mv -v ./samples/sample* ./samples/serie3/gen2/
python3 gen.py -s 200000  -n 10 -m 2000000 -r 3003
mv -v ./samples/sample* ./samples/serie3/gen3/
python3 gen.py -s 400000  -n 10 -m 4000000 -r 3004
mv -v ./samples/sample* ./samples/serie3/gen4/

#Generate series n°4 - size: 50000-100000-200000-400000, magnitude: 1000000
python3 gen.py -s 50000  -n 10 -m 1000000 -r 4001 -p 1 
mv -v ./samples/sample* ./samples/serie4/gen1/
python3 gen.py -s 100000  -n 10 -m 1000000 -r 4002 -p 1 
mv -v ./samples/sample* ./samples/serie4/gen2/
python3 gen.py -s 200000  -n 10 -m 1000000 -r 4003 -p 1 
mv -v ./samples/sample* ./samples/serie4/gen3/
python3 gen.py -s 400000  -n 10 -m 1000000 -r 4004 -p 1 
mv -v ./samples/sample* ./samples/serie4/gen4/