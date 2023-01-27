from datetime import datetime, timedelta


def date_range(start_datetime, end_datetime):
    for n in range(int((start_datetime - end_datetime).days)):
        yield start_datetime - timedelta(n)


def utc_day(start_datetime, end_datetime):
    """gets datetime interval, iterates between, and for each calculates utc start & end timestamp

    Args:
        start_datetime and end_datetime
        datetime(2023, 1, 27, 0, 0)
    Returns:
        list of tuples: for each datetime, a tuple with before and after utc values
        ('16/01/23', 1673909999, 1673823600) utc values representing 23:59:59 and 00:00:00 of date
    """
    tuple_list_result = list()

    for single_date in date_range(start_datetime, end_datetime):
        after = int(single_date.timestamp())  # 2023-01-27 00:00:00
        before = int((after + 86399))  # 2023-01-27 23:59:59

        before_after_interval = (
            single_date.strftime("%d/%m/%y"),
            before,
            after,
        )
        tuple_list_result.append(before_after_interval)
    return tuple_list_result
