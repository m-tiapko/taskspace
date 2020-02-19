#!/bin/bash

for i in {1..100}
do
    out=$i
    for3="Fizz"
    for5="Buzz"
    if [ $(($i % 3)) -ne 0 ];
    then
        for3=""
    else 
        out=""
    fi

    if [ $(($i % 5)) -ne 0 ];
    then
        for5=""
    else
        out=""
    fi
    echo -ne $out$for3$for5 " "
done