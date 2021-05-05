import datetime

def parse_time(date):
    time = datetime.datetime.strptime(date,'%Y-%m-%d')
    return time

