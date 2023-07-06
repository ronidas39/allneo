#use TimeRotating file handlers
import logging

logger = logging.getLogger(__name__)


#stream_h = logging.StreamHandler()
file_h = logging.FileHandler(filename="Logs/TestLog.log")

#stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.INFO)

formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
#stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

#logger.addHandler(stream_h)
logger.addHandler(file_h)

logger.warning('This is a warning log')
logger.error('This is a Error logged in a file.')