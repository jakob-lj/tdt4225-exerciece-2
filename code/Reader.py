import os
from Types import PltFile, Environment
from Types import PltLine
from Types import UserRequest
from Utils import getDateFromDateAndTimeString

LINES_TO_SIZE_RATIO = 62.4
HEADER_SIZE = 6


class Reader:
    def __init__(self, insertService, environment=Environment.PROD, linesThreshold=2500):
        self.insertService = insertService
        self.environment = environment
        self.linesTreshhold = linesThreshold + HEADER_SIZE
        self.USER_INDEX = None
        self.lastUser = None
        self.labels = None

    def openFile(self, path, currentUser, activity, labels):

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
            currentLabel = None
            # print(parsedLines[0].date)
            # print(labels)
            if (labels != None):
                for label in labels:
                    if (parsedLines[0].date == label['start'] and parsedLines[-1].date == label['end']):
                        currentLabel = label['label']

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
            if (not "179" in root and self.environment == Environment.DEV):
                continue
            else:
                if("labels.txt" in files):
                    fileData = open(root + "/labels.txt")
                    labelsInput = [line.strip()
                                   for line in fileData.readlines()]
                    self.labels = []
                    for label in labelsInput[1:]:
                        labelData = [l.strip() for l in label.split()]
                        startDate = getDateFromDateAndTimeString(
                            labelData[0], labelData[1])
                        endDate = getDateFromDateAndTimeString(
                            labelData[2], labelData[3])
                        labelString = labelData[4]
                        self.labels.append(
                            {"start": startDate, "end": endDate, "label": labelString})

                if ("Trajectory" in root):
                    #print("starting with labels", self.labels)
                    for file in files:
                        activity = self.getActivityFromFile(file)
                        currentUser = self.getUserFromPath(root)
                        self.openFile(root + "/" + file,
                                      currentUser, activity, self.labels)
                        if (self.lastUser != currentUser):
                            if (self.lastUser != None):
                                self.labels = None
                            self.lastUser = currentUser
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
