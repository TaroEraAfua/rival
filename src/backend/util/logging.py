# coding: utf-8
import os
import sys
from logging import Formatter, handlers, StreamHandler, getLogger, DEBUG, FileHandler, handlers
import inspect


class Logger:
    def __init__(self, filename='error.log', name=__name__):
        os.makedirs('/var/log/rival/', exist_ok=True)
        self.logger = getLogger(name)
        self.logger.setLevel(DEBUG)
        formatter = Formatter("[%(asctime)s] - %(message)s")

        # stdout
        # コンソールがログだらけになるため一時コメントアウト
        # handler = StreamHandler()
        # handler.setLevel(DEBUG)
        # handler.setFormatter(formatter)
        # self.logger.addHandler(handler)

        # file
        # handler = handlers.RotatingFileHandler(filename='/www/dir/log/your_log_path.log',
        #                                        maxBytes=1048576,
        #                                        backupCount=3,
        #                                        encoding='utf-8'
        #                                        )

        e_filename = '/var/log/rival/' + filename

        error_handler = handlers.RotatingFileHandler(
            filename=e_filename,
            maxBytes=1048576,
            backupCount=3,
            encoding='utf-8'
        )
        error_handler.setFormatter(formatter)
        self.logger.addHandler(error_handler)

        # handler.setLevel(DEBUG)
        # handler.setFormatter(formatter)
        # self.logger.addHandler(handler)

    def cre_msg(self, code, msg='System error'):
        called_filename = inspect.currentframe().f_back.f_back.f_back.f_code.co_filename
        called_function = inspect.currentframe().f_back.f_back.f_back.f_code.co_name
        cre_msg = 'ERR_CODE: ' + code + ' - PGM: ' + called_filename + ' - FUNC: ' + called_function + ' - MSG: ' + msg
        return cre_msg

    def debug(self, msg):
        self.logger.debug(msg)

    def info(self, msg):
        self.logger.info(msg)

    def warn(self, msg):
        self.logger.warning(msg)

    def error(self, code, msg):
        self.logger.error(self.cre_msg(code, msg))

    def critical(self, msg):
        self.logger.critical(msg)
