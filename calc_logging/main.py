import logging
import logging.config

# Load logging configuration
logging.config.fileConfig('logging.conf')
student_logger = logging.getLogger(__name__)

# Example logging
student_logger.debug("This is a debug message from the student")
student_logger.info("This is an info message from the student")
student_logger.warning("This is a warning message from the student")
student_logger.error("This is an error message from the student")
student_logger.critical("This is a critical message from the student")
