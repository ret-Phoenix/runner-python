import subprocess
import os

from core.worker import Worker

def walk(parseDir):
  for name in os.listdir(parseDir):
    path = os.path.join(parseDir, name)
    if os.path.isfile(path):
    	Worker(path).start() 
    else:
        walk(path)

walk("tasks/")