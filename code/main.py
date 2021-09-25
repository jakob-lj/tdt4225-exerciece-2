#from .DatabaseSetup import DatabaseSetup
#from code.DbConenctor import DatabaseConnector
from DbConnector import DbConnector
from Logger import Logger, LogLevel

logger = Logger(LogLevel.DEBUG)


def main():

    logger.info("Welcome to TDT4225 exercice 2")

    dbConnector = DbConnector(
        HOST="localhost", PASSWORD="password", USER="root", DATABASE="tdt4225", logger=logger)

    dbConnector.close_connection()


if __name__ == '__main__':
    logger.info("Hello")
    main()
