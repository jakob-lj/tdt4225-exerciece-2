from TaskRunner import TaskRunnerStub
from Types import ActivityRequest, TrackingPointRequest


class TrackPointInsertStub:

    def __init__(self, cursor, userService, activityService, trackingPointService, taskRunner=TaskRunnerStub(), insertServicesActivated=False):
        self.cursor = cursor
        self.userService = userService
        self.taskRunner = taskRunner
        self.activityService = activityService
        self.trackingPointService = trackingPointService

    def insertPltFile(self, file):
        print("Inserting file %s" % file.fileName)

    def insertTrackingPointsAndActivityForUser(self, user, activity, trakcingPoints, currentLabel):
        # print(trakcingPoints)
        print(user, activity)


class TrackPointInsert:

    def __init__(self, cursor, userService, activityService, trackingPointService, taskRunner=TaskRunnerStub(), insertServicesActivated=False):
        self.cursor = cursor
        self.userService = userService
        self.taskRunner = taskRunner
        self.activityService = activityService
        self.trackingPointService = trackingPointService
        self.insertServicesActivated = insertServicesActivated

    # based on the dataset structure, this will always be a new activity
    def insertTrackingPointsAndActivityForUser(self, user, activity, trackingPoint, currentLabel):
        tm = ""
        if (currentLabel != None):
            tm = currentLabel

        if (self.insertServicesActivated):

            userObj = self.userService.getOrCreate(user)
            activityRequest = ActivityRequest(
                startDateTime=trackingPoint[0].date, endDateTime=trackingPoint[-1].date, transportMode="", userId=userObj.id)
            self.taskRunner.run(self.insertActivityAndTranckingPoints, [
                                userObj.id, activityRequest, trackingPoint])

    def insertActivityAndTranckingPoints(self, userReference, activity, tranckingPoints):
        if (self.insertServicesActivated):
            activityObj = self.activityService.getOrCreate(activity)
            for trackingPoint in tranckingPoints:
                self.trackingPointService.create(trackingPointRequest=TrackingPointRequest(
                    activityId=activityObj.id,
                    latitude=trackingPoint.latitude,
                    longitude=trackingPoint.longitude,
                    altitude=trackingPoint.altitude,
                    timestamp=trackingPoint.date
                ))
            return "ok"
