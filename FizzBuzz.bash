#!/bin/bash
set -euo pipefail
IFS=$'\n\t'

for i in {1..100}
  do
    s=""
    !(( $i % 3 )) && s+="Fizz"
    !(( $i % 5 )) && s+="Buzz"
    echo "${s:-$i}"
  done
