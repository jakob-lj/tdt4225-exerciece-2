from enum import Enum
import datetime


class PltFile:
    def __init__(self, fileName, lines):
        self.fileName = fileName
        self.lines = lines


class PltLine:
    def __init__(self, latitude, longitude, altitude, date, time):

        self.latitude = float(latitude)
        self.longitude = float(longitude)
        self.altitude = altitude
        self.date = datetime.datetime.strptime(
            "%s %s" % (date, time), "%Y-%m-%d %H:%M:%S")

    def __repr__(self):
        return "(%.2f,%.2f)^%s@%s" % (self.latitude, self.longitude, self.altitude, self.date)


class Environment(Enum):
    DEV = "DEV"
