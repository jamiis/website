import subprocess, os
from flask_frozen import Freezer
from app import app

os.system('pip freeze > requirements.txt')

# TODO compile less files. 
#      could use recess's watch functionality or the
#      python pkg watchdog to watch .less file changes

freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()
