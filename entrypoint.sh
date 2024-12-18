#!/bin/sh
# N.B. This is shell script for Linux/MacOS shell. For Windows, you
# would create e.g. a Batch (.bat) or PowerShell (.ps1) script.

# Create your venv in the git-ignored `.venv` dir
python -m venv .venv

# Activate venv and install Python dep's
source .venv/bin/activate  # On Windows this would be .venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt

# Whatever code you want to use to run your script, e.g. in this case:
python "src/test-script.py"
