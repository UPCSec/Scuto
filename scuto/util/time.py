import datetime

def get_timestamp(time: datetime.datetime):
    """
    Returns timestamp of datetime object in UTC
    """
    return time.replace(tzinfo=datetime.timezone.utc).timestamp()

def now():
    return datetime.datetime.utcnow().strftime('YYYY-MM-DD HH:MM:SS')