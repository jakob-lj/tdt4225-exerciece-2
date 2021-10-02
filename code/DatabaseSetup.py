
from tabulate import tabulate
from typing import List
from Types import DatabaseTable, DatabaseColumn


class DatabaseSetup:
    def __init__(self, logger, userService, activityService, trackingPointService, cursor, pruneOnStart=False):
        self.logger = logger
        self.cursor = cursor
        self.pruneOnStart = pruneOnStart
        self.userService = userService
        self.activityService = activityService
        self.trackingPointService = trackingPointService

    def initTables(self):
        self.logger.info("Creating tables")

        createUserTable = self.userService.table

        createActivityTable = self.activityService.table

        createTrackingPointTable = self.trackingPointService.table

        tables = [createUserTable, createActivityTable,
                  createTrackingPointTable]

        for table in tables:

            if (len(table.columns) > 0):

                tableColumnsWrittenOut = ', '.join(
                    ["%s %s" % (column.name, column.type) for column in table.columns])

                createTableQuery = "CREATE TABLE %s (id varchar(36) primary key default (UUID()), %s)" % (
                    table.name, tableColumnsWrittenOut)
                self.logger.debug("Creating table with: %s" % createTableQuery)
                self.cursor.execute(createTableQuery)

            else:
                pass  # table is not ready

    def dropTables(self, tables):

        self.logger.info("Dropping tables: %s" %
                         ', '.join([x[0] for x in tables]))

        dropTableQuery = "DROP TABLE %s"

        [self.cursor.execute(dropTableQuery % table) for table in tables]

    def setup(self):
        self.logger.info("Setting up database")

        self.logger.info("Getting tables already existing")

        self.cursor.execute("SHOW TABLES")

        tablesExistsing = self.cursor.fetchall()

        if (len(tablesExistsing) == 0):
            self.initTables()
        else:
            if self.pruneOnStart:
                self.dropTables(tablesExistsing)
                self.initTables()
            else:
                self.logger.info(
                    "Tables already exists, prune on start is set to False. Preceeding")

       # existingDatabases =

       # self.logger.info(existingDatabases)
