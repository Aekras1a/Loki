# Date: 08/31/2018
# Author: Pure-L0G1C
# Description: Finds a random path

import os
from random import randint
from getpass import getuser

class Finder(object):

 root_dir = os.path.abspath(os.path.sep) + os.path.sep + 'Users' + os.path.sep + getuser() + os.path.sep + 'AppData'
 paths = []

 def is_bad(root, dirs, files):
  return not all([len(dirs), len(files), len(os.path.normpath(root).split(os.sep)) >= randint(5, 10)])   

 def choice(items):
  for _ in range(randint(3, 10)):
   n = randint(0, len(items)-1)
  return items[n]      

 @classmethod
 def find(cls):
  for root, dirs, files in os.walk(cls.root_dir, topdown=True):
   if cls.is_bad(root, dirs, files):continue
   path = root + os.path.sep + cls.choice(dirs)
   cls.paths.append(path)
  return cls.choice(cls.paths) + os.path.sep