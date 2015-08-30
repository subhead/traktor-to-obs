from distutils.core import setup
import py2exe
import socket
import sys
import re
import string
import time
import os

setup(
    options = {'py2exe': {'bundle_files': 1, 'compressed': True}},
    console = ['traktor-to-obs.py'],
    zipfile = None,
)
