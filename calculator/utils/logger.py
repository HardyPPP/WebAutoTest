import logging.handlers

class Logger:
    logger = None
    @classmethod
    def get_logger(cls):
        if cls.logger is None:
            cls.logger = logging.getLogger()
            # 获取日志器

            cls.logger.setLevel(logging.INFO)
            # 设置日志器级别

            stream_handler = logging.StreamHandler()
            # 获取控制台处理器

            time_file_handler = logging.handlers.TimedRotatingFileHandler(filename="../log/log02.log",
                                                                          when="midnight",
                                                                          interval=1,
                                                                          backupCount=30,
                                                                          encoding="utf-8")
            # 获取文件处理器

            fm = "%(asctime)s %(levelname)s [%(name)s][%(filename)s (%(funcName)s:%(lineno)d)] - %(message)s"
            formatter = logging.Formatter(fm)
            # 设置格式器

            stream_handler.setFormatter(formatter)
            time_file_handler.setFormatter(formatter)
            # 将格式器添加到控制器

            cls.logger.addHandler(stream_handler)
            cls.logger.addHandler(time_file_handler)
            # 将处理器添加到日志器
        return cls.logger
