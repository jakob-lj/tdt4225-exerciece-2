
from tabulate import tabulate


class DatabaseSetup:
    def __init__(self, logger, cursor):
        self.logger = logger
        self.cursor = cursor

    def setup(self):
        self.logger.debug("Setting up database")

        self.logger.debug("Getting tables already existing")
        print(self.cursor.execute("SHOW TABLES"))

       # existingDatabases =

       # self.logger.debug(existingDatabases)
