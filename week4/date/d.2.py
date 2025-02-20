import datetime
def ytt():
    today = datetime.datetime.now()
    yesterday = today - datetime.timedelta(days = 1)
    tomorrow = today + datetime.timedelta(days = 1)
    return yesterday, today, tomorrow

yes, to, tom = ytt()
print("Yesterday:", yes)
print("Today:", to)
print("Tomorrow:", tom)