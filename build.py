import subprocess, os
from flask_frozen import Freezer
from app import app

os.system('pip freeze > requirements.txt')

freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()
