# import logging
#
# class LogGen():
#
#     @staticmethod
#     def loggen():
#         path = "C:\\Users\\HP\\PycharmProjects\\automationexercise\\logs\\automationexercise.log"
#         logging.basicConfig(filename=path, format='%(asctime)s: %(levelname)s: %(message)s',
#                             datefmt='%m/%d/%Y %I:%M:%S %p')
#
#         #logging.basicConfig()
#         logger=logging.getLogger()
#         logger.setLevel(logging.INFO)
#         return logger

#===================================================
import logging
import os

class LogGen:
    @staticmethod
    def loggen():
        log_dir = os.path.join(os.getcwd(), "logs")  # ✅ Ensure logs folder exists
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        log_file = os.path.join(log_dir, "automationexercise.log")

        # ✅ REMOVE existing handlers to prevent duplication
        if logging.getLogger().hasHandlers():
            logging.getLogger().handlers.clear()

        # ✅ Setup logging configuration
        logging.basicConfig(
            filename=log_file,
            format='%(asctime)s: %(levelname)s: %(message)s',
            datefmt='%m/%d/%Y %I:%M:%S %p',
            level=logging.INFO,
            filemode='a'
        )

        # ✅ Add Console Logging (Optional)
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s')
        console_handler.setFormatter(formatter)
        logging.getLogger().addHandler(console_handler)

        logger = logging.getLogger()
        return logger
