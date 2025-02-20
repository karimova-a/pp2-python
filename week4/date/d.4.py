import datetime 
def diff(d1, d2):
    differ = (d2 - d1).total_seconds()
    return differ

d1 = datetime.datetime(2025, 2, 20)
d2 = datetime.datetime(2025, 2, 21)

print("Difference in seconds:", diff(d1, d2))