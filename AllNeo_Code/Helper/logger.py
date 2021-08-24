import logging as logging
import logging.config as logConfig 
from logging.handlers import TimedRotatingFileHandler

class NeoLogger:
    #logConfig.fileConfig('./Global/Logging.conf')
    
    #create logger 
    def getLogger(loggerName):
        
        allNeo_logger = logging.getLogger(loggerName)
        allNeo_logger.setLevel(logging.DEBUG)
        #following line is hardcoded and to be updated with config file setting.
        allNeo_handler = TimedRotatingFileHandler(filename='Logs/AllNeoMasterLog.Log',backupCount= 30, when= 'D', interval= 1, delay= False, utc= True)
        allNeo_format = logging.Formatter('%(asctime)s ::  %(name)s :: %(levelname)s -- %(message)s')
        
        #allNeo_handler.setLevel()        
        allNeo_handler.setFormatter(allNeo_format)
        
        allNeo_logger.addHandler(allNeo_handler)
               
        return allNeo_logger
         
    