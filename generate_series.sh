#! /bin/bash

if [ $1 -eq 1 ]; then
  mkdir serie1/
  mkdir serie1/gen1/
  python3 gen.py -s 10  -n 10 -m 100 -r 1001 -p 0 
  mv -v ./samples/* serie1/gen1/ 
  mkdir serie1/gen2/
  python3 gen.py -s 100  -n 10 -m 100 -r 1002 -p 0 
  mv -v ./samples/* serie1/gen2/ 
  mkdir serie1/gen3/
  python3 gen.py -s 1000  -n 10 -m 100 -r 1003 -p 0 
  mv -v ./samples/* serie1/gen3/ 
  mkdir serie1/gen4/
  python3 gen.py -s 10000  -n 10 -m 100 -r 1004 -p 0 
  mv -v ./samples/* serie1/gen4/ 
fi

if [ $1 -eq 2 ]; then
  mkdir serie2/
  mkdir serie2/gen1/
  python3 gen.py -s 10  -n 10 -m 10 -r 2001 -p 0 
  mv -v ./samples/* serie2/gen1/ 
  mkdir serie2/gen2/
  python3 gen.py -s 10  -n 10 -m 100 -r 2002 -p 0 
  mv -v ./samples/* serie2/gen2/ 
  mkdir serie2/gen3/
  python3 gen.py -s 10  -n 10 -m 1000 -r 2003 -p 0 
  mv -v ./samples/* serie2/gen3/ 
  mkdir serie2/gen4/
  python3 gen.py -s 10  -n 10 -m 10000 -r 2004 -p 0 
  mv -v ./samples/* serie2/gen4/ 
fi

if [ $1 -eq 3 ]; then
  mkdir serie3/
  mkdir serie3/gen1/
  python3 gen.py -s 10  -n 10 -m 10 -r 3001 -p 0 
  mv -v ./samples/* serie3/gen1/ 
  mkdir serie3/gen2/
  python3 gen.py -s 100  -n 10 -m 100 -r 3002 -p 0 
  mv -v ./samples/* serie3/gen2/ 
  mkdir serie3/gen3/
  python3 gen.py -s 1000 -n 10 -m 1000 -r 3003 -p 0 
  mv -v ./samples/* serie3/gen3/ 
  mkdir serie3/gen4/
  python3 gen.py -s 10000  -n 10 -m 10000 -r 3004 -p 0 
  mv -v ./samples/* serie3/gen4/ 
fi

if [ $1 -eq 4 ]; then
  mkdir serie4/
  mkdir serie4/gen1/
  python3 gen.py -s 10  -n 10 -m 10 -r 4001 -p 1 
  mv -v ./samples/* serie4/gen1/ 
  mkdir serie4/gen2/
  python3 gen.py -s 100  -n 10 -m 10 -r 4002 -p 1 
  mv -v ./samples/* serie4/gen2/ 
  mkdir serie4/gen3/
  python3 gen.py -s 1000  -n 10 -m 10 -r 4003 -p 1 
  mv -v ./samples/* serie4/gen3/ 
  mkdir serie4/gen4/
  python3 gen.py -s 10000  -n 10 -m 10 -r 4004 -p 1 
  mv -v ./samples/* serie4/gen4/ 
fi


