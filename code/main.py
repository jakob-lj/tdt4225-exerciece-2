#from .DatabaseSetup import DatabaseSetup
#from code.DbConenctor import DatabaseConnector
from DbConnector import DbConnector
from DatabaseSetup import DatabaseSetup
from Logger import Logger, LogLevel
from Reader import Reader
from TrackPonitInsert import TrackPointInsert
from UserService import UserService
from ActivityService import ActivityService
from TrackingPointService import TrackingPointServiceStub, TrackingPointService

logger = Logger(LogLevel.INFO)

runReadAndInsertServices = True
activateInsertService = True
pruneOnStart = True


def main(dbConnector, databaseSetup, transformLayer, trackPointInserter, userService, activityService, runServices=False):

    logger.info("Welcome to TDT4225 exercice 2")

    if (runServices):
        databaseSetup.setup()

        userService.init()

        activityService.init()

        dbConnector.db_connection.commit()

        transformLayer.readFiles()


if __name__ == '__main__':

    dbConnector = DbConnector(
        HOST="localhost", PASSWORD="password", USER="root", DATABASE="tdt4225", logger=logger)

    userService = UserService(
        dbConnector.cursor, dbConnection=dbConnector.db_connection, logger=logger, activate=activateInsertService)

    activityService = ActivityService(
        dbConnector.cursor, dbConnection=dbConnector.db_connection, logger=logger, activate=activateInsertService)

    trackingPointService = TrackingPointService(
        dbConnector.cursor, dbConnection=dbConnector.db_connection, logger=logger, activate=activateInsertService)

    trackPointInserter = TrackPointInsert(
        cursor=dbConnector.cursor, userService=userService, activityService=activityService, trackingPointService=trackingPointService, insertServicesActivated=activateInsertService)

    transformLayer = Reader(insertService=trackPointInserter)

    logger.info("Initializing")

    databaseSetup = DatabaseSetup(
        userService=userService,
        activityService=activityService,
        trackingPointService=trackingPointService,
        cursor=dbConnector.cursor, logger=logger, pruneOnStart=pruneOnStart)

    main(dbConnector, databaseSetup, transformLayer,
         trackPointInserter, userService, activityService, runReadAndInsertServices)

    dbConnector.close_connection()
