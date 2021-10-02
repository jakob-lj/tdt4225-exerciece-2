from Crud import Crud
from Types import DatabaseColumn, DatabaseTable, InsertRequest, TrackingPoint, TrackingPointRequest

activityColumn, latitudeColumn, longitudeColumn, altitudeColumn, dateTimesColumn = DatabaseColumn("activity_id", "varchar(36)"), DatabaseColumn(
    "latitude", "double"), DatabaseColumn("longitude", "double"), DatabaseColumn("altitude", "integer"), DatabaseColumn("date_times", "timestamp")


class TrackingPointServiceStub:
    def __init__(self, cursor: any, dbConnection, logger):
        self.table = DatabaseTable("tracking_point_stub", columns=[])
        self.logger = logger

    def create(self, trackingPointRequest: TrackingPointRequest):
        self.logger.debug("Stub tracking point service does not create")


class TrackingPointService(Crud):
    def __init__(self, cursor: any, dbConnection, logger):
        Crud.__init__(self, DatabaseTable(
            name="tracking_point", columns=[
                activityColumn, latitudeColumn, longitudeColumn, altitudeColumn, dateTimesColumn
            ]),
            cursor=cursor, dbConnection=dbConnection, logger=logger)

        self.logger = logger

    def fetchActivities(self):
        return self.serializeArray(self.getAll())

    def serialize(self, data):
        return TrackingPoint(id=data[0], activityId=data[1], latitude=data[2], longitude=data[3], altitude=data[4], timestamp=data[6])

    def serializeArray(self, data):
        return [self.serialize(user) for user in data]

    def getInMemory(self, request: TrackingPointRequest):
        # for inMemActivity in self.activities:
        #     if (inMemActivity.id == activity.id):
        #         return inMemActivity
        # return None
        return None

    def create(self, trackingPointRequest: TrackingPointRequest):
        tp = self.insert([
            InsertRequest(column=activityColumn,
                          value=trackingPointRequest.activityId),
            InsertRequest(column=latitudeColumn,
                          value=trackingPointRequest.latitude),
            InsertRequest(column=longitudeColumn,
                          value=trackingPointRequest.longitude),
            InsertRequest(column=altitudeColumn,
                          value=trackingPointRequest.altitude),
            InsertRequest(column=dateTimesColumn,
                          value=trackingPointRequest.timestamp),
        ], returnData=False)
        return tp

    def getOrCreate(self, trackingPointRequest: TrackingPointRequest):
        return self.create(trackingPointRequest)
