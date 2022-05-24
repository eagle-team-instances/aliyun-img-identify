import yaml
import os

def loadConfig():
    configFile = open(os.path.join(os.getcwd(), 'config.yml'), 'r')
    configYaml = yaml.safe_load(configFile)
    return configYaml