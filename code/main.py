#from .DatabaseSetup import DatabaseSetup
#from code.DbConenctor import DatabaseConnector
from DbConnector import DbConnector
from DatabaseSetup import DatabaseSetup
from Logger import Logger, LogLevel
from Reader import Reader
from TrackPonitInsert import TrackPointInsert
from UserService import UserService

logger = Logger(LogLevel.DEBUG)


def main(dbConnector, databaseSetup, transformLayer, trackPointInserter):

    logger.info("Welcome to TDT4225 exercice 2")

    databaseSetup.setup()

    dbConnector.db_connection.commit()

    transformLayer.readFiles()


if __name__ == '__main__':

    dbConnector = DbConnector(
        HOST="localhost", PASSWORD="password", USER="root", DATABASE="tdt4225", logger=logger)

    userService = UserService(
        dbConnector.cursor, dbConnection=dbConnector.db_connection, logger=logger)

    trackPointInserter = TrackPointInsert(
        cursor=dbConnector.cursor, userService=userService)

    transformLayer = Reader(insertService=trackPointInserter)

    databaseSetup = DatabaseSetup(
        userService=userService,
        cursor=dbConnector.cursor, logger=logger, pruneOnStart=True)
    main(dbConnector, databaseSetup, transformLayer, trackPointInserter)

    dbConnector.close_connection()
