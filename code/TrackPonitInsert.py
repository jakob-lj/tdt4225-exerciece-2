from TaskRunner import TaskRunnerStub


class TrackPointInsertStub:

    def __init__(self, cursor, userService, taskRunner=TaskRunnerStub()):
        self.cursor = cursor
        self.userService = userService
        self.taskRunner = taskRunner

    def insertPltFile(self, file):
        print("Inserting file %s" % file.fileName)

    def insertTrackingPointsAndActivityForUser(self, user, activity, trakcingPoints):
        # print(trakcingPoints)
        print(user, activity)


class TrackPointInsert:

    def __init__(self, cursor, userService, taskRunner=TaskRunnerStub()):
        self.cursor = cursor
        self.userService = userService
        self.taskRunner = taskRunner

    def insertTrackingPointsAndActivityForUser(self, user, activity, trackingPoint):

        userObj = self.userService.getOrCreate(user)
        self.taskRunner.run(self.insertActivityAndTranckingPoints, [
                            userObj.id, activity, trackingPoint])

    def insertActivityAndTranckingPoints(self, userReference, activity, tranckingPoints):
        print(userReference, activity)
        return "ok"
