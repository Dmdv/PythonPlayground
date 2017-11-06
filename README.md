# PythonPlayground

1. Install python from https://www.python.org/downloads
2. Get pip from https://bootstrap.pypa.io/get-pip.py
3. Run python get-pip.py
4. Install virtualenv: pip install virtualenv
5. Install virtualenv wrapper: pip install virtualenvwrapper-win (virtualenvwrapper for linux)
6. mkproject name (linux) or mkvirtualenv name (windows)
7. only windows: 
	cd name
	setproject dir .
	
Other usefull commands:

List of available envs: workon (WORKON_HOME is environment path)
deactivate: quit env <br>
rmvirtualenv env-name: remove virtual env <br>
pip freeze > requirements.txt: save dependencies <br>
pip install -r requirements.txt: install requirements <br>

Links:

http://virtualenvwrapper.readthedocs.io/en/latest <br>
http://docs.python-guide.org/en/latest/dev/virtualenvs <br>
