#!/bin/bash

(( "$#" == 2 )) && \
export $(grep -v "^#" $1 | xargs -0) && \
(echo "cat <<EOF";cat $2; echo "EOF") | sh > upd_${2}