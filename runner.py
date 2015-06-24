import subprocess
import os

from core.worker import Worker

def walk(parse_dir):
  for name in os.listdir(parse_dir):
    path = os.path.join(parse_dir, name)
    if os.path.isfile(path):
    	Worker(path).start() 
    else:
        walk(path)

walk("tasks/")