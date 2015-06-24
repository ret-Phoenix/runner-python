import threading
import time
import subprocess

from datetime import datetime, date
from core.settings import Settings


class Worker(threading.Thread):

  def __init__(self, settings_file):
    threading.Thread.__init__(self, name="Worker: " + settings_file)
    settignsFromFile = Settings(settings_file)
    self.settings = settignsFromFile.get_settings()

  def writeToErrLog(self, msg):
    err_log_file = open("error.log", "a")
    err_log_file.write("---" + '\n')
    err_log_file.write(str(datetime.today()) + '\n')
    err_log_file.write(self.name + '\n')
    err_log_file.write(str(msg) + '\n')
    err_log_file.close()

  def run_application(self):
    log = subprocess.Popen(self.settings["application"],
      shell=True, stdout=subprocess.PIPE)
    out = log.communicate()
    test = log.returncode
    if (test != 0):
      self.writeToErrLog(out)    	

  def run(self):
    while True:
      self.run_application()
      time.sleep(self.settings["timeout"])
