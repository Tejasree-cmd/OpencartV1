import configparser
import os

config = configparser.RawConfigParser()
loc11 = os.path.abspath(os.curdir)
loc12 = os.path.join(loc11,"configurations")
loc13 = os.path.join(loc12,"config.ini")
print(loc13)
config.read(loc13)

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = (config.get('commonInfo','baseURL'))
        return url
    @staticmethod
    def getUseremail():
        username=(config.get('commonInfo','email'))
        return username
    @staticmethod
    def getPassword():
        password= (config.get('commonInfo','password'))
        return password