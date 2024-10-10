# edukist-service

<h3>Python 3.11 is required, get it from <a href="https://www.python.org/downloads/release/python-3110/"> here</a></h3>

<h3>First time setup  command line :</h3>

1. Create python virtual environment: `python -m venv venv`

2. If you haven’t configured the PATH and PATHEXT variables (only Windows): `C:/Users/Name/AppData/Local/Programs/Python/Python311/python -m venv venv`

3.  Activate the created python virtual environment  : `./venv/Scripts/activate`

4.  Optional  To install packages on pythons virtual environment: `python -m pip install <package-name>`

5.  Install requirements and dependencies from terminal:  `pip install -r requirements.txt`


<h3>First time setup  PyCharm :</h3>

1. You can configure python interpreter from :

    1.1  For Windows and Linux:  File | Settings | Project: <project name> | Python Interpreter. *Select as virtual environment 

    1.2  For macOS:  PyCharm | Preferences | Project: <project name> | Python Interpreter for macOS. *Select as virtual environment

2.  Install requirements and dependencies  - Open a project with the requirements file specified, a notification bar is displayed on top of any Python or requirements file opened in Editor - click Install Requirements

3. Alternatively to Install requirements and dependencies run the following command on terminal:` pip install -r requirements.txt`

<h3>Check swagger documentation</h3>
1. To access swagger documentation please go to the following url: <span style="font-size: 14px">http://localhost:{your_port}/swagger<span>.  
2. Example to access swagger of your port is 5000: http://127.0.0.1:5000/swagger/


