#!/bin/bash

usage(){
    echo "Usage: $0 <envfile> <inputfile> [ -o outputfile]" 1>&2
    exit 1
}

viafile(){
    while getopts ":o:" opt; do
                case "${opt}" in 
                    o)
                        outputfile=${OPTARG}
                        (echo "cat <<EOF";cat "${inputfile}";) | sh 2>/dev/null  1>$outputfile
                        ;;
                    *)
                        usage
                        ;;
                esac
            done
}

if [[ "$#" -lt 2 ]]; then 
    usage
fi

envfile=$1
inputfile=$2
shift; shift
if [[ -e ${envfile} && -r ${envfile} && -s ${envfile} ]]; then
    export $(grep -v "^#" ${envfile} | xargs -0)
    echo "Exported"
    if [[ -e ${inputfile} && -r ${inputfile} && -s ${inputfile} ]]; then
        echo "Checked"
        if [[ $# -eq 0 ]]; then 
            echo "I here"
            (echo "cat <<EOF";cat "${inputfile}";) | sh 2>/dev/null
        elif [[ $# -eq 2 ]]; then
            viafile $@
        else 
            usage
        fi
    else 
        usage
    fi

else 
    usage
fi
