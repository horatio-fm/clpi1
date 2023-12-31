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

from .install_hooks import hook_text_list

version_file = os.path.join(os.path.dirname(my_package.__file__), "version.py")
# if not os.path.exists(my_package.version.__file__):
if not os.path.exists(version_file):
    Path(version_file).touch()

my_package.version = importlib.import_module(module_name + ".version")

username = getpass.getuser()

git = "git"

proc = subprocess.Popen('{0} diff --exit-code'.format(git), stdout=subprocess.PIPE, shell=True)
info = proc.communicate()[0].decode("utf-8").rstrip()

if proc.returncode != 0:
    print("There are local changes in the working directory!!")
    print("There are local changes in the working directory!!")
    print("There are local changes in the working directory!!")
    print("There are local changes in the working directory!!")
    print("There are local changes in the working directory!!")
    print("DDD!!")
    sys.exit(1)

proc = subprocess.Popen('{0} update-index --assume-unchanged {1}'.format(git, my_package.version.__file__), stdout=subprocess.PIPE, shell=True)
proc.communicate()[0].decode("utf-8").rstrip()

proc = subprocess.Popen('{0} rev-list --count HEAD'.format(git), stdout=subprocess.PIPE, shell=True)
count = proc.communicate()[0].decode("utf-8").rstrip()

if count == "1":
    proc = subprocess.Popen('{0} tag v0.0.0'.format(git), stdout=subprocess.PIPE, shell=True)

proc = subprocess.Popen('{0} describe --tags'.format(git), stdout=subprocess.PIPE, shell=True)
version = proc.communicate()[0].decode("utf-8").rstrip()

proc = subprocess.Popen('{0} rev-parse --short HEAD'.format(git), stdout=subprocess.PIPE,
                        shell=True)
hashkey = proc.communicate()[0].decode("utf-8").rstrip()

proc = subprocess.Popen('{0} rev-parse --git-dir'.format(git), stdout=subprocess.PIPE, shell=True)
git_dir = proc.communicate()[0].decode("utf-8").rstrip()

if len(version.split("-")) > 1:
    version = "-".join(version.split("-")[:-1] + [hashkey])
else:
    version = "-".join([version, hashkey])

proc = subprocess.Popen('{0} rev-parse --abbrev-ref HEAD'.format(git), stdout=subprocess.PIPE,
                        shell=True)
current_branch = proc.communicate()[0].decode("utf-8").rstrip()

proc = subprocess.Popen('{0} show -s --format=%ci HEAD'.format(git), stdout=subprocess.PIPE,
                        shell=True)
time_of_commit = proc.communicate()[0].decode("utf-8").rstrip()
time_of_commit = time_of_commit.replace(" ", "_")
time_of_commit = time_of_commit.replace(":", "-")

with open(my_package.version.__file__, "w") as fp:
    fp.write(f'''"""
Warning: This file is automatically generated by the following GIT hooks:{hook_text_list}
It is in the repository but has attribute 'assume-unchanged'. It is specific for every worktree.
"""

''')
    fp.write("version = '")
    fp.write("__".join([version, time_of_commit, current_branch]))
    fp.write("'")
