import calendar
from datetime import timedelta

from dateutil.relativedelta import relativedelta
from delorean import Delorean


def get_tz_time_period(time_period, timezone_to_check):
    d = Delorean()
    now = d.shift(timezone=timezone_to_check).datetime
    today_day_start = d.shift(timezone=timezone_to_check).start_of_day
    today_day_end = d.shift(timezone=timezone_to_check).end_of_day

    week_start = today_day_start - timedelta(days=today_day_start.weekday())
    week_end = week_start + timedelta(days=6)
    month_start = today_day_start.replace(day=1)
    month_end = today_day_start.replace(
        day=calendar.monthrange(today_day_start.year, today_day_start.month)[1]
    )
    return {
        "TODAY": (today_day_start, now),
        "YESTERDAY": (
            today_day_start - relativedelta(days=1),
            today_day_end - relativedelta(days=1),
        ),
        "THIS_WEEK": (week_start, week_end),
        "THIS_MONTH": (month_start, month_end),
        "ALL": "all",
    }.get(time_period)
