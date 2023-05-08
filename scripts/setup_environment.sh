

SCRIPTPATH="$( cd -- "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 ; pwd -P )"
echo "$SCRIPTPATH"
root="$(dirname "$SCRIPTPATH")"
deps=${root}/deps

pargenesbin=${deps}/ParGenes/pargenes/
raxmlbin=${deps}/ParGenes/raxml-ng/bin/
generaxbin=${deps}/GeneRax/build/bin
aleraxbin=${deps}/AleRax/build/bin
asteroidbin=${deps}/Asteroid/build/bin

toadd="${pargenesbin}:${raxmlbin}:${generaxbin}:${aleraxbin}:${asteroidbin}"

export PATH="${toadd}:${PATH}"



bashrcline="export PATH=\"${toadd}:\${PATH}\""

echo "" >> ~/.bashrc
echo "$bashrcline" >> ~/.bashrc

echo "Adding the following paths to the PATH variable: ${toadd}"
echo "Adding the following line to your ~/.bashrc file: $bashrcline" 


