
install_benoit() {
  repo=$1
  git clone --recursive  https://github.com/BenoitMorel/${repo}.git
  cd ${repo}
  ./install.sh
  cd ..
}


mkdir -p deps
cd deps
#install_benoit "ParGenes"
install_benoit "GeneRax"
#install_benoit "AleRax"
#install_benoit "Asteroid"
cd ..



