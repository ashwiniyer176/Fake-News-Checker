"""This file initalises all the core components of the code and also contains all the major imports 

It is called after the run.py starts the application

it is the controller of the package which in this case is analyse
"""

from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

### Imported these files at last to prevent circular imports


from analyse import routes