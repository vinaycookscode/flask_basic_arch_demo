#!/usr/bin/env bash
export FLASK_CONFIG=development
export FLASK_APP=wsgi.py
export FLASK_DEBUG=True
#export FLASK_RUN_PORT=5050
python -m flask run
# >> log/output.log 2>&1