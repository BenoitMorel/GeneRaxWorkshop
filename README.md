# GeneRaxWorkshop

If you have already installed the required software, you can go to the [wiki](https://github.com/BenoitMorel/GeneRaxWorkshop/wiki) to start the workshop.

# Requirements

To compile the softare, please first install the following dependencies (you might already have some of them installed):
* [git](https://git-scm.com/)
* [cmake](https://cmake.org/) 
* [gcc](https://gcc.gnu.org/)
* [python3](https://www.python.org/downloads/)
* The [ete3](http://etetoolkit.org/) python library
* [MPI](https://en.wikipedia.org/wiki/Message_Passing_Interface) (optionnal, but we'll use it to parallelize computations)

To check if you already have them installed, check that the following commands exist:
```
git --version
cmake --version
gcc --version
python3 --version
mpiexec --version # checks MPI installation

```

On ubuntu, you can install the missing dependencies with:
```
sudo apt-get install git-all  
sudo apt-get install cmake 
sudo apt install build-essential # installs gcc
# I am not sure what's the best way to install python3, so I'll let you find out
sudo apt install mpich # installs MPI
sudo pip3 install ete3
```

We will use the following tools (I provide a script to install them):
* [ParGenes](https://github.com/BenoitMorel/ParGenes)
* [GeneRax](https://github.com/BenoitMorel/GeneRax)
* [AleRax](https://github.com/BenoitMorel/AleRax)
* [Thirdkind](https://github.com/simonpenel/thirdkind) (or its [webserver](http://thirdkind.univ-lyon1.fr/))
* ASTRAL-III
* RAxML-NG

To install these tools automatically:
```
git clone https://github.com/BenoitMorel/GeneRaxWorkshop.git
cd GeneRaxWorkshop
./scripts/install.sh
```

The installation should take 5 to 10 minutes. Then, if you want to be able to run the tools from anywhere:
```
source scripts/setup_environment.sh
```

After this you should be able to run tools such as raxml-ng from anywhere:
```
raxml-ng --version
```

Note that this script adds a line to your `~/.bashrc` file, in order to set up the environment variables everytime you open a console. Feel free to remove this line from bashrc at the end of the workshop.


