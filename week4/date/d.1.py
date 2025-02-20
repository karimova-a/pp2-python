import datetime
def prev5():
    today = datetime.datetime.now()
    result = today - datetime.timedelta(days=5)
    return result 

print("Five days from today:", prev5())