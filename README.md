# mini-project-EC463

Sprint information: https://github.com/ianballou/mini-project-EC463/projects/1<br>
Demo website: http://128.31.26.87:5000

# Pre-requirements

C compiler, general development tools installed, Python

# Steps to run:

- cd into the root directory of this project
- install `python-virtualenv`
- run `virtualenv .venv`
- run `source .venv/bin/activate`
- run `pip install flask`
- run `FLASK_APP=miniproject.py`
- run `pip install flask-wtf`
- run `pip install flask-sqlalchemy`
- run `pip install flask-migrate`
- run `pip install flask-login`
- run `pip install flask-login`
- run `pip install matplotlib`
- create `~/.config/matplotlib/matplotlibrc`
- run `echo "backend: Agg" > ~/.config/matplotlib/matplotlibrc`
- Install the python tkinter library with a package manager: `apt-get`, `yum`, `dnf`, etc
- run `flask db upgrade`
- start the site by running `flask run --host=0.0.0.0`

# Design choices:
- Web framework: Python Flask<br>
- Database management: SQLAlchemy<br>
- Authentication: Database username/email/password<br>
- Sensor simulation: Upon logging in and loading a user's homepage, sensor data is randomly (but realistically) generated and plotted.<br>

# Workflow
1) Register with username, email, password, and # of sensors.
2) View graphs of sensor data on personal homepage.
