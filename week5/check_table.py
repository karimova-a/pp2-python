import re
import csv

f = open("row.txt", "r",encoding="utf-8")
text = f.read()


BINPattern = r"\nБИН\s(?P<BIN>[0-9]+)"
BINResult = re.search(BINPattern, text).group("BIN")
print(BINResult)

CheckPattern = r"\nЧек\s(?P<Check>№[0-9]+)"
CheckResult = re.search(CheckPattern, text).group("Check")
print(CheckResult)
ItemPattern = r"(?P<ItemRowNumber>.*)\n(?P<ItemName>.*)\n(?P<ItemsCount>.*)\sx\s(?P<ItemPrice>.*)\n(?P<TotalItemPrice1>.*)\nСтоимость\n(?P<TotalItemPrice2>.*)"

prog = re.compile(ItemPattern)
ItemIterator1 = prog.finditer(text)

with open('data.csv', 'w', newline='',encoding="utf8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['ItemRowNumber', 'ItemName', 'ItemPrice'])
    for ItemResult in ItemIterator1:
         writer.writerow([ItemResult.group("ItemRowNumber"), ItemResult.group("ItemName"), ItemResult.group("ItemPrice")])

print("#" * 100)

ItemIterator2 = prog.findall(text)

col_width_num = 15
col_width_name = 90
col_width_price = 10



print(f"{'ItemRowNumber':<{col_width_num}} | {'ItemName':<{col_width_name}} | {'ItemPrice':<{col_width_price}}")
print("-" * (col_width_num + col_width_name + col_width_price + 5)) # 8 - это ширина разделителей (|)


for ItemResult in ItemIterator2:
    print(f"{ItemResult[0]:<{col_width_num}} | {ItemResult[1]:<{col_width_name}} | {ItemResult[3]:<{col_width_price}}")