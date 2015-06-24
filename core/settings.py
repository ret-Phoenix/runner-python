__author__ = 'SUShakov'

import json


class Settings:
  def __init__(self, settings_file):
    self.file_name = settings_file

  def get_settings(self):
    file_options = open(self.file_name, "r",1, 'utf8')
    settings = json.load(file_options)
    return settings

  def set_settings(self, settings_data):
    output = open(self.file_name, "w")
    json.dump(settings_data, output)
