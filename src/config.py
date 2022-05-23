import yaml
import os

def loadConfig():
    print('正在加载配置文件...')
    configFile = open(os.path.join(os.getcwd(), 'config.yml'), 'r')
    print(os.path.join(os.getcwd(), 'config.yml'))
    configYaml = yaml.safe_load(configFile)
    print(configYaml)
    print('解析完成')
    return configYaml