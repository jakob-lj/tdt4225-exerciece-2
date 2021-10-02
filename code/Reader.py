import os
from Types import PltFile, Environment
from Types import PltLine
from Types import UserRequest

LINES_TO_SIZE_RATIO = 62.4
HEADER_SIZE = 6


class Reader:
    def __init__(self, insertService, environment=Environment.PROD, linesThreshold=2500):
        self.insertService = insertService
        self.environment = environment
        self.linesTreshhold = linesThreshold + HEADER_SIZE
        self.USER_INDEX = None

    def openFile(self, path, currentUser, activity):
        size = os.stat(path).st_size
        # remove all files that should be outside the avarage of liens to size ratio
        if (size < LINES_TO_SIZE_RATIO*self.linesTreshhold * 2):
            file = open(path, "r").readlines()
            # only consider lines smaller than 2500 tracking points
            if (len(file) >= self.linesTreshhold):
                return

            lines = [x.strip() for x in file[6:]]

            splittedLines = [x.split(",") for x in lines]

            parsedLines = [PltLine(
                latitude=x[0],
                longitude=x[1],
                altitude=x[3],
                date=x[5],
                time=x[6]
            ) for x in splittedLines]

            self.insertService.insertTrackingPointsAndActivityForUser(
                UserRequest(textIdentifier=currentUser, hasLables=False), activity, parsedLines)

    def readFiles(self):
        # data = open(
        #    "../dataset/dataset/Data/000/Trajectory/20081023025304.plt", "r").readlines()
        # print(data)
        finished000 = False
        labels = None
        for root, dir, files in os.walk("../dataset"):
            # skipp all other than 000 in development
            if (not "000" in root and self.environment == Environment.DEV):
                continue
            else:
                if("labels.txt" in files):
                    labels = open("labels.txt")
                if ("Trajectory" in root):
                    for file in files:
                        activity = self.getActivityFromFile(file)
                        currentUser = self.getUserFromPath(root)
                        if (labels != None):
                            # TODO: Calculate if activity had label
                            pass
                        #self.openFile(root + "/" + file, currentUser, activity)
                        labels = None
            # for file in files:
                # print(file)
            # sself.insertService.insertPltFile(PltFile(fileName = ))

    def getUserFromPath(self, path):
        if (self.USER_INDEX == None):
            elementsWithLenghtThree = 0
            foundElement = None
            userIndex = 0
            for element in path.split("/"):
                if len(element) == 3:
                    elementsWithLenghtThree += 1
                    foundElement = element
                userIndex += 1
            if (elementsWithLenghtThree != 1):
                raise "Could not automatically find user"
            USER_INDEX = userIndex
            return foundElement
        else:
            return path.split("/")[USER_INDEX]

    def getActivityFromFile(self, file):
        return file.split(".")[0]
