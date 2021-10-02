from TaskRunner import TaskRunnerStub
from Types import ActivityRequest


class TrackPointInsertStub:

    def __init__(self, cursor, userService, activityService, taskRunner=TaskRunnerStub()):
        self.cursor = cursor
        self.userService = userService
        self.taskRunner = taskRunner
        self.activityService = activityService

    def insertPltFile(self, file):
        print("Inserting file %s" % file.fileName)

    def insertTrackingPointsAndActivityForUser(self, user, activity, trakcingPoints):
        # print(trakcingPoints)
        print(user, activity)


class TrackPointInsert:

    def __init__(self, cursor, userService, activityService, taskRunner=TaskRunnerStub()):
        self.cursor = cursor
        self.userService = userService
        self.taskRunner = taskRunner
        self.activityService = activityService

    def insertTrackingPointsAndActivityForUser(self, user, activity, trackingPoint):

        userObj = self.userService.getOrCreate(user)
        activityRequest = ActivityRequest(
            startDateTime=trackingPoint[0].date, endDateTime=trackingPoint[-1].date, transportMode="", userId=userObj.id)
        self.taskRunner.run(self.insertActivityAndTranckingPoints, [
                            userObj.id, activityRequest, trackingPoint])

    def insertActivityAndTranckingPoints(self, userReference, activity, tranckingPoints):
        activityObj = self.activityService.getOrCreate(activity)
