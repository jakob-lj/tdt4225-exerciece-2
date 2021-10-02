from Crud import Crud
from Types import DatabaseColumn, DatabaseTable, InsertRequest, Activity, ActivityRequest

userColumn, transportModeColumn, startColumn, endColumn = DatabaseColumn("user_id", "varchar(36)"), DatabaseColumn(
    "transportion_mode", "varchar(36)"), DatabaseColumn("start_date_time", "timestamp"), DatabaseColumn("end_date_time", "timestamp")


class ActivityService(Crud):

    def __init__(self, cursor: any, dbConnection, logger):
        Crud.__init__(self, DatabaseTable(name="activity", columns=[
            userColumn, transportModeColumn, startColumn, endColumn
        ]),
            cursor=cursor, dbConnection=dbConnection, logger=logger)
        self.activities = self.fetchActivities()
        self.logger = logger

    def fetchActivities(self):
        return self.serializeArray(self.getAll())

    def serialize(self, data):
        return Activity(id=data[0], userId=data[1], transportMode=data[2], startDateTime=data[3], endDateTime=data[4])

    def serializeArray(self, data):
        return [self.serialize(user) for user in data]

    def getInMemory(self, activity: ActivityRequest):
        # for inMemActivity in self.activities:
        #     if (inMemActivity.id == activity.id):
        #         return inMemActivity
        # return None
        return None

    def create(self, activityRequest: ActivityRequest):
        activity = self.insert([
            InsertRequest(column=userColumn, value=activityRequest.userId),
            InsertRequest(column=transportModeColumn,
                          value=activityRequest.transportMode),
            InsertRequest(column=startColumn,
                          value=activityRequest.startDateTime),
            InsertRequest(column=endColumn, value=activityRequest.endDateTime)
        ])
        self.activities.append(activity)
        return activity

    def getOrCreate(self, activity: ActivityRequest):
        inMemActivity = self.getInMemory(activity)
        if (inMemActivity == None):
            self.logger.debug("Activity does not exist, creating")
            return self.create(activity)
        self.logger.debug("Activity exists in cache")
        return inMemActivity
