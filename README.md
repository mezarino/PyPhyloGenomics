#PyPhyloGenomics
A package to work on Phylogenomics.

[[In development.]]

##Developers
* Carlos Peña (email: carlos.pena@utu.fi)
* Victor Solis
* Pavel Matos
* Chris Wheat


##Installing PyPhyloGenomics
The installer of PyPhyloGenomics will try to download and install all its dependencies as well. 
To install PyPhyloGenomics use `setup.py`:

    python setup.py build  
    python setup.py install

If it fails you can install the dependencies manually:

##Install dependencies:

###requests:
The package ``requests`` from [here](http://docs.python-requests.org/en/latest/user/install/). Or try:

    sudo apt-get install python-requests

###Parallel Python (pp):
If you are using Ubuntu Linux or related:

    sudo apt-get install python-pp

Otherwise, [download](http://www.parallelpython.com/content/view/15/30/) the source code and install `pp`:

    unzip pp-1.6.4.zip
    cd pp-1.6.4
    python setup.py install

###BioPython:
Download and install from [here](http://biopython.org/wiki/Download). Or:

    sudo apt-get install python-biopython

### BeatutifulSoup
Download and install from [here](http://www.crummy.com/software/BeautifulSoup/). Or:

    sudo apt-get install python-bs4

###MUSCLE
It is necessary that you install MUSCLE so that PyPhyloGenomics can use it to align sequences. 
Download and install from [here](http://www.drive5.com/muscle/downloads.htm).

If you are using Windows you can download the executable file **muscle3.8.31_i86win32.exe** 
and save it in your Python folder (C:\Python27\) as **muscle.exe**.

### BLAST
Download and install the BLAST+ executables from the
[NCBI website](http://blast.ncbi.nlm.nih.gov/Blast.cgi?CMD=Web&PAGE_TYPE=BlastDocs&DOC_TYPE=Download). Or try:

    sudo apt-get install ncbi-blast+

### fastx-toolkit
Download and install from [here](http://hannonlab.cshl.edu/fastx_toolkit/). Or:

    sudo apt-get install fastx-toolkit

## Reading PyPhyloGenomics' documentation:
Read the online documentation here: [http://carlosp420.github.io/PyPhyloGenomics/](http://carlosp420.github.io/PyPhyloGenomics/)

Or, after installling do the following:

    cd doc  
    make html

Then open the file `_build/html/index.html` in your web-browser.

## Reproduce our analysis:
You can reproduce all the steps detailed in our [Getting started with PyPhylogenomics] guide. 
Just use the command line in the same folder as the ``Makefile`` and type make ???
