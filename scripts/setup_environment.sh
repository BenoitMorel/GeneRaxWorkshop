

SCRIPTPATH="$( cd -- "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 ; pwd -P )"
echo "$SCRIPTPATH"
root="$(dirname "$SCRIPTPATH")"
deps=${root}/deps

pargenesbin=${deps}/ParGenes/pargenes/
raxmlbin=${deps}/ParGenes/raxml-ng/bin/
generaxbin=${deps}/GeneRax/build/bin
aleraxbin=${deps}/AleRax/build/bin
asteroidbin=${deps}/Asteroid/build/bin

export PATH="${pargenesbin}:${raxmlbin}:${generaxbin}:${aleraxbin}:${asteroidbin}:${PATH}"
echo $PATH
