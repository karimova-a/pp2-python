import datetime

def nomicro():
    today = datetime.datetime.now()
    no_micro = today.replace(microsecond=0)
    return no_micro

print("Date with no microseconds:", nomicro())