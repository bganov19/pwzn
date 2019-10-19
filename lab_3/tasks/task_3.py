"""
Zadanie za 2 pkt.

Uzupełnij funckję parse_dates tak by zwracała przygotowaną wiadomość
z posortowanymi zdarzeniami.
Funkcja przyjmuje ciag zdarzeń (zapisanych w formie timestampu w dowolnej strefie czasowej),
przetwarza je na zdarzenia w strefie czasowej UTC i sortuje.
Posortowane zdarzenia są grupowane na dni i wypisywane od najnowszych do najstarszych.

Na 1pkt. Uzupełnij funkcję sort_dates, która przyjmuje dwa parametry:
- log (wielolinijkowy ciąg znaków z datami) zdarzeń
- format daty (podany w assercie format ma być domyślnym)
Zwraca listę posortowanych obiektów typu datetime w strefie czasowej UTC.

Funkcje group_dates oraz format_day mają pomoc w grupowaniu kodu.
UWAGA: Proszę ograniczyć użycie pętli do minimum.
"""
import datetime


def sort_dates(date_str, date_format=datetime.timezone.utc):
    """
    Parses and sorts given message to list of datetimes objects descending.

    :param date_str: log of events in time
    :type date_str: str
    :param date_format: event format
    :type date_format: str
    :return: sorted desc list of utc datetime objects
    :rtype: list
    """
    month = {"Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6,
             "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12}

    date_list = date_str.split("\n")
    date_list = [elem.split() for elem in date_list if not elem.isspace() and elem]
    date_list = [sublist[1:] for sublist in date_list]

    for elem in date_list:
        day = int(elem[0])
        elem[0] = int(elem[2])
        elem[1] = month[elem[1]]
        elem[2] = day

        bufstr = elem.pop()
        bufstr2 = elem[3].split(":")
        elem.pop()

        bufstr2 = [int(i) for i in bufstr2]
        elem.extend(bufstr2)

        h = int(bufstr[:3])
        m = int(bufstr[3:])

        elem[3] -= h
        elem[4] -= m

    dt_list = [datetime.datetime(*elem, tzinfo=date_format) for elem in date_list]
    return dt_list


def group_dates(dates):
    """
    Groups list of given days day by day.

    :param dates: List of dates to group.
    :type dates: list
    :return:
    """

    days = []
    times = []

    for elem in dates:
        if elem.date() not in days:
            days.append(elem.date())
            times.append([elem.time()])
        else:
            times[-1].extend([elem.time()])

    events = [(day, time) for day, time in zip(days, times)]
    return events


def format_day(day, events):
    """
    Formats message for one day.

    :param day: Day object.
    :type day: datettime.datetime
    :param events: List of events of given day
    :type events: list
    :return: parsed message for day
    :rtype: str
    """

    s = str(day)+"\n"

    for elem in events:
        s += "\\t"+str(elem)+"\n"

    s += "----" + "\n"
    return s


def parse_dates(date_str, date_format=datetime.timezone.utc):
    """
    Parses and groups (in UTC) given list of events.

    :param date_str: log of events in time
    :type date_str: str
    :param date_format: event format
    :type date_format: str
    :return: parsed events
    :rtype: str
    """

    dt_list = sort_dates(date_str, date_format=date_format)
    events = group_dates(dt_list)

    s = ""
    for day, event in events:
        s += format_day(day, event)

    return s[:-6]


if __name__ == '__main__':
    dates = """
    Sun 10 May 2015 13:54:36 -0700
    Sun 10 May 2015 13:54:36 -0000
    Sat 02 May 2015 19:54:36 +0530
    Fri 01 May 2015 13:54:36 -0000
    """

    sort_dates(dates)

    assert sort_dates(dates) == [
        datetime.datetime(2015, 5, 10, 20, 54, 36, tzinfo=datetime.timezone.utc),
        datetime.datetime(2015, 5, 10, 13, 54, 36, tzinfo=datetime.timezone.utc),
        datetime.datetime(2015, 5, 2, 14, 24, 36, tzinfo=datetime.timezone.utc),
        datetime.datetime(2015, 5, 1, 13, 54, 36, tzinfo=datetime.timezone.utc),
    ]

    assert parse_dates(dates) == """2015-05-10
    \t20:54:36
    \t13:54:36
    ----
    2015-05-02
    \t14:24:36
    ----
    2015-05-01
    \t13:54:36"""

#Nie mam pojęcia w czym jest problem, funkcja zwraca dokładnie to samo co jest w assercie
