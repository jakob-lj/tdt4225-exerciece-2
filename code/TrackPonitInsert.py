
class TrackPointInsertStub:
    def insertPltFile(self, file):
        print("Inserting file %s" % file.fileName)

    def insertTrackingPointsAndActivityForUser(self, user, activity, trakcingPoints):
        # print(trakcingPoints)
        print(user, activity)


class TrackPointInsert:
    def insertTrackingPointsAndActivityForUser(self, user, activity, trackingPoint):
        raise "Not yet implemented"
