#from .DatabaseSetup import DatabaseSetup
#from code.DbConenctor import DatabaseConnector
from DbConnector import DbConnector
from DatabaseSetup import DatabaseSetup
from Logger import Logger, LogLevel
from Reader import Reader
from TrackPonitInsert import TrackPointInsertStub

logger = Logger(LogLevel.INFO)


def main(dbConnector, databaseSetup):

    logger.info("Welcome to TDT4225 exercice 2")

    databaseSetup.setup()


if __name__ == '__main__':
    logger.info("Hello")

    dbConnector = DbConnector(
        HOST="localhost", PASSWORD="password", USER="root", DATABASE="tdt4225", logger=logger)

    databaseSetup = DatabaseSetup(
        cursor=dbConnector.cursor, logger=logger, pruneOnStart=True)

    trackPointInserter = TrackPointInsertStub()

    transformLayer = Reader(insertService=trackPointInserter)

    transformLayer.readFiles()

    dbConnector.close_connection()

   # main(dbConnector, databaseSetup)
