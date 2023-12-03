"""
Generates 'my_package'.version.__file__ which in the GIT repo with attribute 'assume-unchanged'.
This is specific for every worktree.
"""
import importlib
import os
import re
import subprocess
import getpass
import sys
from pathlib import Path

project_name = os.path.basename(os.path.dirname(os.path.dirname(__file__)))
module_name = re.sub(r'\d+$', '', project_name)
my_package = importlib.import_module(module_name)

my_package.version = importlib.import_module(module_name + ".version")

username = getpass.getuser()

git = "git"

proc = subprocess.Popen('{0} update-index --no-assume-unchanged {1}'.format(git, my_package.version.__file__), stdout=subprocess.PIPE, shell=True)
proc.communicate()[0].decode("utf-8").rstrip()

