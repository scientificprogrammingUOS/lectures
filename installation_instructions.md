In the following, if you are asked to *run* a command like

    $ run this command

it means that you should type `run this command` in the terminal and press <kbd>Enter</kbd>.

# Installation instructions

You only need to install Anaconda and git if you don't have it already on your computer. To check if you have git already, you can run

    $ where git

If it returns something, you have git already. To test if you have Anaconda or Miniconda, run

    $ where python

If it returns a path like ../anaconda3/bin/python, you already have the correct Anaconda/Miniconda distribution and you can skip this step.




### conda

Download  Miniconda https://conda.io/miniconda.html with Python 3.7.

##### For Linux/Mac OS
To start the installer run

    $ bash Miniconda3-latest-Linux-x86_64.sh

Most options can just be answered with yes, however you should insist on adding `conda` to your PATH when the installer asks you.

#### For Windows
Start the graphical installer, it should guide through the installation process. If you don't have another python-installation already installed, you can safely add python to your %PATH%, such that you can it from your normal `cmd`-shell. In any case, you should have a program named "Anaconda prompt" installed afterward, which you can find with the start menu. If you didn't add it to your %PATH% as instructed above, you need to run all `conda`-commands in the Anaconda prompt, otherwise you can use the normal `cmd` or `Powershell`.

If you want to install an environment, make sure you have Admin-rights for the terminal you use. To do that, hit <kbd>Win</kbd>+<kbd>X</kbd>, and select either *Powershell as Administrator* or *cmd as Administrator*, depending on what your Windows offers you.

You can test if you have the correct python-version there by typing ``python --version``, which should tell you it's Python 3.6.x

### git

#### For Linux

To install, open a terminal and run

    $ sudo apt-get install git

#### For Mac
Install Homebrew if you don't have it already from https://brew.sh/. Then run

    $ brew install git

#### For Windows

Download the `.exe` from https://git-scm.com/download/win and run the installer.

In the install wizard, make sure that git **can** be used from the command prompt, otherwise you'd have to switch between shells when coding and committing to git.To make sure your solution will be accepted once pushed, you need to set one of the two *commit unix style* options. Other than that, you'll probably go for the *openSSL* as well as *Windows default console as terminal emulator* options.

## Working on the exercise

### Clone the scientific_programming environment

Next you have to create the correct virtual environment for working on your homework. For that, you can clone our lecture-repository. To do so, enter the terminal and navigate to a directory (`cd`) where you want to put your homework. Run

    $ git clone https://github.com/scientificprogrammingUOS/lectures.git

to clone the repository. Afterwards, you can create the environment using

    $ conda env create -f lectures/environment.yml

This will create a new environment and install all the necessary packages needed for this course. Instead of cloning the repository you can also simply download the raw yaml from https://raw.githubusercontent.com/scientificprogrammingUOS/lectures/master/environment.yml and create the environment using `conda env create -f path/to/environment.yml`.


Afterwards, you need to activate the environment.

##### For Linux/Mac OS

To activate the environment, run

    $ conda activate scientific_programming

#### For Windows

If you didn't add conda-commands to your %PATH%, you'll ned to open the program Anaconda prompt. It will give you a typical Windows `cmd`-style shell. The command to activate the environment is

    $ conda activate scientific_programming

as well. Your shell should indicate the environment you are in if it worked.


Always activate the environment when you work on the homework. To deactivate the
environment again, run `conda deactivate` on all systems.

To open the Python interpreter run

    $ python

the prompt should start with something like

    Python 3.6.3 |Anaconda, Inc.|

close the interpreter again by running

    >>> quit()

