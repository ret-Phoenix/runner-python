__author__ = 'SUShakov'

import json


class Settings:
  def __init__(self, settingsFile):
    self.fileName = settingsFile

  def getSettings(self):
    fileOptions = open(self.fileName, "r",1, 'utf8')
    settings = json.load(fileOptions)
    return settings

  def setSettings(self, settingsData):
    output = open(self.fileName, "w")
    json.dump(settingsData, output)
