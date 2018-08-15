# Lectures in Scientific Computing in Python
This repository contains all lectures from the course 
*Scientific programming in Python* that is part of the Cognitive Science program
at the University Osnabrück. Each lecture is accompanied by a Jupyter notebook
that explains each topic with a combination of code and text. You
can view the notebooks directly on GitHub or run them locally and play
with the code.


## Recordings
All lecture recordings can be viewed on the Opencast platform.

Lecture 01 [Opencast](https://video4.virtuos.uos.de/engage/theodul/ui/core.html?cid=a18d5bd1b862d194bcd7b56bca95c32f&id=b0079cbf-51b7-47c1-8a38-21147935d249)

Lecture 02 [Opencast](https://video4.virtuos.uos.de/engage/theodul/ui/core.html?cid=a18d5bd1b862d194bcd7b56bca95c32f&id=f41dc9ef-c846-4f07-a7a8-b87b92cd82f9)

Lecture 03 [Opencast](https://video4.virtuos.uos.de/engage/theodul/ui/core.html?cid=a18d5bd1b862d194bcd7b56bca95c32f&id=fcb80388-4dc3-4336-bec4-a294ccc096de)

Lecture 04 [Opencast](https://video4.virtuos.uos.de/engage/theodul/ui/core.html?cid=a18d5bd1b862d194bcd7b56bca95c32f&id=f695daea-8ee4-473b-8684-c46cbef62586)

Lecture 05 [Opencast](https://video4.virtuos.uos.de/engage/theodul/ui/core.html?cid=a18d5bd1b862d194bcd7b56bca95c32f&id=3a01b270-efc0-4d38-8457-586ec2fc6886)

Lecture 06 [Opencast](https://video4.virtuos.uos.de/engage/theodul/ui/core.html?cid=a18d5bd1b862d194bcd7b56bca95c32f&id=0b158123-ecdb-4081-a13a-4a13c57cfeac)

Lecture 07 [Opencast](https://video4.virtuos.uos.de/engage/theodul/ui/core.html?cid=a18d5bd1b862d194bcd7b56bca95c32f&id=e077a983-89b3-40f7-818c-4cd34906f41f)

Lecture 08 [Opencast](https://video4.virtuos.uos.de/engage/theodul/ui/core.html?cid=a18d5bd1b862d194bcd7b56bca95c32f&id=4f440f84-8de7-4336-8f3f-b8f5764d84f3)

Lecture 09 [Opencast](https://video4.virtuos.uos.de/engage/theodul/ui/core.html?cid=a18d5bd1b862d194bcd7b56bca95c32f&id=79bce1f2-48e3-407b-8a1d-caf2a74e5517)

Lecture 10 [Opencast](https://video4.virtuos.uos.de/engage/theodul/ui/core.html?cid=a18d5bd1b862d194bcd7b56bca95c32f&id=634cd5c8-0227-4c19-9400-e348b53b2bf0)

Lecture 11 [Opencast](https://video4.virtuos.uos.de/engage/theodul/ui/core.html?cid=a18d5bd1b862d194bcd7b56bca95c32f&id=a34a0164-19da-406b-b1e1-3570ebcdc8d4)

Lecture 12 [Opencast](https://video4.virtuos.uos.de/engage/theodul/ui/core.html?cid=a18d5bd1b862d194bcd7b56bca95c32f&id=6d4e5f5e-727f-4834-80db-4322a86b0a96)

## Installation
Create a virtual Python environment, name e.g. *scientific*, for example using `conda`.

    $ conda create -n scientific python

Activate the environment on Linux/Mac

    $ source activate scientific
    
or Windows 

    $ activate scientific

then install all dependencies

    $ pip install -r requirements.txt

then start JupyterLab

    $ jupyter lab

JupyterLab should open in your browser. From there you can navigate to the notebooks 
and interact with them.


## Contributing
Before committing changes, run the whole notebook from top to bottom using

    $ jupyter nbconvert --execute --allow-errors --inplace <lecture.ipynb> 
