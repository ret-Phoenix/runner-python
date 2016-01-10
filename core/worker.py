import threading
import time
import subprocess
import sys

from datetime import datetime, date
from core.settings import Settings


class Worker(threading.Thread):

  def __init__(self, settingsFile):
    threading.Thread.__init__(self, name="Worker: " + settingsFile)
    settignsFromFile = Settings(settingsFile)
    self.settings = settignsFromFile.getSettings()

  def writeToLog(self, category, msg):
    logFileName = self.settings["log"]
    if (logFileName == ""):
      logFileName = "running.log";
    errLogFile = open("logs/"+logFileName, "a")
    errLogFile.write("---" + '\n')
    errLogFile.write(str(datetime.today()) + '\n')
    errLogFile.write(self.name + '\n')
    errLogFile.write(str(category) + '\n')
    errLogFile.write(str(msg) + '\n')
    errLogFile.close()

  def runApplication(self):
      log = subprocess.Popen(self.settings["application"],
        shell=True, stdout=subprocess.PIPE)
      out = log.communicate()
      test = log.returncode
      if (test != 0):
        if (self.settings["logging-error"] == 1):
          self.writeToLog('ERROR',out)
      else:
        if (self.settings["logging-success"] == 1):
          self.writeToLog('SUCCESS',out)

  def run(self):
    while True:
      self.runApplication()
      time.sleep(self.settings["timeout"])
