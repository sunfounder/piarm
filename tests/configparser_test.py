from configparser import ConfigParser
from os import path
from robot_hat.utils import log,run_command

class Config():
    def __init__(self,config_path):
        self.config = ConfigParser()
        self.path = config_path
        if not path.exists(self.path):
            log('Steps record file does not exist.Create now...')
            try:
                run_command('sudo mkdir -p '+self.path.rsplit('/',1)[0])
                run_command('sudo touch '+self.path)
                run_command('sudo chmod a+rw '+self.path)
            except Exception as e:
                log(e)
        self.config.read(self.path)

    
    def update(self):
        try:
            with open(self.path,'w')as f:
                self.config.write(f)
        except Exception as e:
            log(e)

    def add(self,section_name,message):
        self.config[section_name] = message
        self.update()

    def remove(self,section_name):
        self.config.remove_section(section_name)
        self.update()


    def clear(self):     
        self.config.clear()
        self.update()

    
    def get_sections(self):    
        names = self.config.sections()
        return names

    def get_options(self,section_name):
        names = self.config.options()
        return names

    def set_option(self,section_name,option_name,value):
        self.config.set(section_name,option_name,value)
        self.update()

    def get_value(self,section_name,option_name):
        value = self.config.get(section_name,option_name)
        return value

if __name__ == "__main__":
    cg = Config()
    # cg.update()s
    cg.clear_all()
    log(cg.get_names())

