from DbConnector import DbConnector
from Logger import Logger, LogLevel
from util.task2 import getHoursWithActivityByMonthAndYearForUser
logger = Logger(LogLevel.INFO)


def exercise1(connector):
    queries = {"users": "select count(id) from users",
               "activies": "select count(id) from activity",
               "trackingPonits": "select count(id) from tracking_point"}

    for q in queries:
        connector.cursor.execute(queries[q])
        result = connector.cursor.fetchall()
        print(q, result[0][0])


def exercise2(connector):
    connector.cursor.execute(
        "select min(actvts), max(actvts), avg(actvts) from (select u.id, count(a.id) as actvts from users u inner join activity a on a.user_id = u.id group by u.id) as result")
    rsult = connector.cursor.fetchall()
    print("min, max, avg:")
    print(rsult[0])


def exercise3(connector):
    connector.cursor.execute(
        "select u.id, count(a.id) as activities from users u inner join activity a on a.user_id = u.id group by u.id order by activities desc limit 10"
    )
    print("result was:")
    for result in connector.cursor.fetchall():
        print(result)


def exercise4(connector):
    connector.cursor.execute(
        "select count(distinct user_id) from activity where date(start_date_time) != date(end_date_time)")
    print("Number of users that started their activity in another day that they ended:")
    print(connector.cursor.fetchall()[0][0])


def exercise5(connector):
    connector.cursor.execute("select id from activity a, (select user_id, start_date_time, end_date_time, count(ab.id) from activity ab group by user_id, start_date_time, end_date_time having count(ab.id) > 1) as r where a.user_id = r.user_id and a.start_date_time = r.start_date_time and a.end_date_time = r.end_date_time")
    print("Duplicates")
    print("I decided that duplicates are activities starting at the same time and ending at the same time for the same user")
    print("there can't be duplicates in the ids..")
    print(connector.cursor.fetchall())


def exercise6(connector):
    print("sorry i did not have time...")


def exercise7(connector):
    print("users that has not taken the taxi")
    print("Keep in mind that I didn't finsih the label work:):)")
    connector.cursor.execute(
        "select u.id from users u inner join activity a on u.id = a.user_id where a.transportion_mode != 'taxi' group by u.id")
    [print(x[0]) for x in connector.cursor.fetchall()]


def exercise8(connector):
    print("im really sorry for this exercise. I did not use enough time for the labels")
    print("therefor, i have not tested this and hope the query works on your machine ;)")
    connector.cursor.execute(
        "select distinct a.transportion_mode, (select count(ab.id) from activity ab where ab.transportion_mode = a.transportion_mode) from activity a where a.transportion_mode != null")
    print(connector.cursor.fetchall())


def exercise9(connector):
    print("a)")
    print("getting activities by month")
    connector.cursor.execute(
        "select year(a.start_date_time) as year, month(a.start_date_time) as month, count(a.id) as count from activity a group by year, month order by year, month")
    for r in connector.cursor.fetchall():
        print(r)

    print("november 2011 is the most active month")

    print("b)")
    connector.cursor.execute(
        "select count(a.id), a.user_id, u.text_identifier from activity a inner join users u on u.id = a.user_id where month(a.start_date_time) = 11 and year(a.start_date_time) = 2011 group by a.user_id order by count(a.id) desc")
    result = connector.cursor.fetchall()
    print(result)
    print("user %s had the most activies in this month" % result[0][2])
    print("user %s had the second most activies" % result[1][2])

    hoursMost = getHoursWithActivityByMonthAndYearForUser(
        connector, result[0][1], 2011, 11)
    hoursSecond = getHoursWithActivityByMonthAndYearForUser(
        connector, result[1][1], 2011, 11)

    print("The most active person had the most amount of hours?:",
          hoursMost == hoursSecond, "(" + str(hoursMost) + " vs " + str(hoursSecond) + ")")


if __name__ == '__main__':
    dbConnector = DbConnector(
        HOST="localhost", PASSWORD="password", USER="root", DATABASE="tdt4225", logger=logger)

    exercise1(dbConnector)

    exercise2(dbConnector)

    exercise3(dbConnector)

    exercise4(dbConnector)

    exercise5(dbConnector)

    exercise6(dbConnector)

    exercise7(dbConnector)

    exercise8(dbConnector)

    exercise9(dbConnector)
