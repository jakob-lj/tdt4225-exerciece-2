from enum import Enum
import datetime


class User:
    def __init__(self, id, textIdentifier, hasLables):
        self.id: String = id
        self.textIdentifier: String = textIdentifier
        self.hasLables: Boolean = hasLables

    def __repr__(self):
        return "%s - %s" % (self.textIdentifier, self.hasLables)


class UserRequest:
    def __init__(self, textIdentifier, hasLables):
        self.textIdentifier: String = textIdentifier
        self.hasLables: Boolean = hasLables

    def __repr__(self):
        return "%s - %s" % (self.textIdentifier, self.hasLables)


class DatabaseColumn:
    def __init__(self, name, type):
        self.name: String = name
        self.type: String = type


class DatabaseTable:
    def __init__(self, name, columns):
        self.name: String = name
        self.columns: List[DatabaseColumn] = columns


class InsertRequest:
    def __init__(self, column, value):
        self.column = column
        self.value = value


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
