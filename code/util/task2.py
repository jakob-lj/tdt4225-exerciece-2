
def getHoursWithActivityByMonthAndYearForUser(connector, user, year, month):
    connector.cursor.execute(
        "select sum(timestampdiff(minute, start_date_time, end_date_time))/60 from activity where user_id = '%s' and month(start_date_time) = %s and year(start_date_time) = %s" % (user, month, year))
    return connector.cursor.fetchall()[0][0]
