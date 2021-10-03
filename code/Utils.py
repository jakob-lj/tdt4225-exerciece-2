import datetime


def getDateFromDateAndTimeString(date, time):
    return datetime.datetime.strptime(
        "%s %s" % (date, time), "%Y/%m/%d %H:%M:%S")
