import configparser

import os

config=configparser.RawConfigParser()
config.read(os.path.abspath(os.curdir)+'\\configuration\\config.ini')

class ReadConfig():

    @staticmethod
    def getApplicationURL():
        url=(config.get('commonInfo','baseURL'))
        return url

    @staticmethod
    def getEmail():
        email=(config.get('commonInfo','Email'))
        return email

    @staticmethod
    def getPassword():
        password=(config.get('commonInfo','Password'))
        return password
