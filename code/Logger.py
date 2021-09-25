import datetime


def getLogLableByValue(level):
    levels = ["ERROR", "WARNING", "INFO", "DEBUG"]
    return levels[level]


class LogLevel:
    ERROR = 0
    WARNING = 1
    INFO = 2
    DEBUG = 3


class Logger:

    def __init__(self, logLevel=LogLevel.INFO):
        self.logLevel = logLevel

    def output(self, logLevel, messages):
        message = ' '.join([str(x) for x in messages])
        if (self.logLevel >= logLevel):
            print("[%s] %s: %s" % (getLogLableByValue(
                logLevel), datetime.datetime.now(), message))

    def debug(self, *message):
        self.output(LogLevel.DEBUG, message)

    def info(self, *message):
        self.output(LogLevel.INFO, message)

    def warning(self, *message):
        self.output(LogLevel.WARNING, message)

    def error(self, *message):
        self.output(LogLevel.ERROR, message)
