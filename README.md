# PythonPlayground

## Pip

1. Install python from https://www.python.org/downloads
2. Get pip from https://bootstrap.pypa.io/get-pip.py
3. Run python get-pip.py

## Pipenv

### Installing Pipenv

Pipenv is a dependency manager for Python projects. While pip can install Python packages, Pipenv is recommended as it’s a higher-level tool that simplifies dependency management for common use cases.

``
$ pip install --user pipenv
``

### Installing packages for your project

``
$ cd myproject
``

``
$ pipenv install requests
``

### Then you can run this script using pipenv run:

``
$ pipenv run python main.py
``

## Lower level: virtualenv

``
$ pip install virtualenv
``

Test your installation

``
$ virtualenv --version
``

#### Create a virtual environment for a project:

``
$ cd my_project_folder
``

``
$ virtualenv my_project
``

virtualenv my_project will create a folder in the current directory which will contain the Python executable files, and a copy of the pip library which you can use to install other packages. The name of the virtual environment (in this case, it was my_project) can be anything; omitting the name will place the files in the current directory instead.

This creates a copy of Python in whichever directory you ran the command in, placing it in a folder named my_project.

You can also use the Python interpreter of your choice (like python2.7).

``
$ virtualenv -p /usr/bin/python2.7 my_project
``

or change the interpreter globally with an env variable in ~/.bashrc:

``
$ export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python2.7
``

#### To begin using the virtual environment, it needs to be activated:

``
$ source my_project/bin/activate
``

#### If you are done working in the virtual environment for the moment, you can deactivate it:

``
$ deactivate
``

## Virtualenvwrapper

virtualenvwrapper provides a set of commands which makes working with virtual environments much more pleasant. It also places all your virtual environments in one place.

To install (make sure virtualenv is already installed):

``
$ pip install virtualenvwrapper
``

``
$ export WORKON_HOME=~/Envs
``

Full instauctions: https://virtualenvwrapper.readthedocs.io/en/latest/install.html

### Mac

$ export WORKON_HOME=~/Envs
$ mkdir -p $WORKON_HOME
$ source /usr/local/bin/virtualenvwrapper.sh
$ mkvirtualenv my_project


## Virtualenvwrapper-win ``(for windows)``

``
$ pip install virtualenvwrapper-win
``

In Windows, the default path for WORKON_HOME is %USERPROFILE%Envs


## Basic Usage

1. Create a virtual environment 

Windows:

``
$ mkvirtualenv my_project
``

Linux:

``
$ mkproject my_project
``


This creates the ``my_project`` folder inside ``~/Envs``.

2. Work on a virtual environment:

``
$ workon my_project
``

virtualenvwrapper provides tab-completion on environment names. It really helps when you have a lot of environments and have trouble remembering their names.

workon also deactivates whatever environment you are currently in, so you can quickly switch between environments.

3. Deactivating is still the same:

``
$ deactivate
``

4. To delete:

``
$ rmvirtualenv venv
``

### Other useful commands 1

``python3 -m venv envname``

only windows:

``cd name``

``setproject dir . ``
	
### Other useful commands 2

``lsvirtualenv``

``workon``
        
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;List all of the environments.

``cdvirtualenv``

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Navigate into the directory of the currently activated virtual environment, so you can browse its site-packages, for example.

``cdsitepackages``

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Like the above, but directly into site-packages directory.

``lssitepackages``

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Shows contents of site-packages directory.


## autoenv

When you cd into a directory containing a .env, autoenv automagically activates the environment.

Install it on Mac OS X using brew:

`` $ brew install autoenv ``

And on Linux:

``$ git clone git://github.com/kennethreitz/autoenv.git ~/.autoenv``

`` $ echo 'source ~/.autoenv/activate.sh' >> ~/.bashrc ``



pip freeze > requirements.txt: save dependencies <br>
pip install -r requirements.txt: install requirements <br>

Links:

http://virtualenvwrapper.readthedocs.io/en/latest <br>
http://docs.python-guide.org/en/latest/dev/virtualenvs <br>
