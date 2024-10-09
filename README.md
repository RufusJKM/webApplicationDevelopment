Activating venv = source flask/bin/activate
Must be deactivated by "deactivate"

To activate the venv on a new terminal enter these two lines
export FLASK_APP=run.py
export FLASK_DEBUG=1

to run, simply put flask [name of executable]

when changing a model, run flask db migrate then flask db upgrade