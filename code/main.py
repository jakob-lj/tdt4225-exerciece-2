#from .DatabaseSetup import DatabaseSetup
#from code.DbConenctor import DatabaseConnector
from DbConnector import DbConnector
from DatabaseSetup import DatabaseSetup
from Logger import Logger, LogLevel

logger = Logger(LogLevel.DEBUG)


def main(dbConnector, databaseSetup):

    logger.info("Welcome to TDT4225 exercice 2")

    databaseSetup.setup()

    dbConnector.close_connection()


if __name__ == '__main__':
    logger.info("Hello")

    dbConnector = DbConnector(
        HOST="localhost", PASSWORD="password", USER="root", DATABASE="tdt4225", logger=logger)

    databaseSetup = DatabaseSetup(
        cursor=dbConnector.cursor, logger=logger)

    main(dbConnector, databaseSetup)
