import calendar
from datetime import datetime
from datetime import timedelta
from enum import Enum

from dateutil.relativedelta import relativedelta
from delorean import Delorean

NOW = datetime.now()
TODAY_DATE = NOW.date()
WEEK_START = TODAY_DATE - timedelta(days=TODAY_DATE.weekday())
WEEK_END = WEEK_START + timedelta(days=6)
MONTH_START = TODAY_DATE.replace(day=1)
MONTH_END = TODAY_DATE.replace(
    day=calendar.monthrange(TODAY_DATE.year, TODAY_DATE.month)[1]
)


class PeriodQueryParamsEnums(Enum):
    TODAY = Delorean().start_of_day, NOW
    YESTERDAY = (
        Delorean().start_of_day - relativedelta(days=1),
        Delorean().end_of_day - relativedelta(days=1),
    )
    THIS_WEEK = WEEK_START, WEEK_END
    THIS_MONTH = MONTH_START, MONTH_END
    ALL = "all"
