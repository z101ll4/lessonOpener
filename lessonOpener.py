import subprocess
from datetime import datetime
from time import sleep

import pandas as pd


def to_normal_table(sheet):
    header = [sheet.columns.tolist()]
    rows = sheet.where(pd.notna(sheet), None).values.tolist()
    return header + rows

#enter url HERE
url = ""
table = pd.read_csv(url)
sheet = to_normal_table(table)

lessons = {}
i = 2
# получение дня
day = 2 + datetime.now().isoweekday()
# заполнение уроков
while True:
    try:
        value = sheet[i][12]
        lessons[value] = sheet[i][13]
        i += 1
    except:
        break

# получение текушего времени
now = 0
def setNow():
    global now
    _now = datetime.now()
    now = _now.hour * 60 + _now.minute


setNow()
print(now)

# ориентир на то какой шяс урок
timeCell = 3
while True:
    value = sheet[timeCell][2]
    if value != None:
        if int(value.split(",")[0]) > now:
            break
    else:
        break
    timeCell += 1
print(sheet[timeCell][2])
print(f"day: {day} timeCell: {timeCell}")
lastS = ""
# перебор
while True:
    dif = int(sheet[timeCell][2].split(",")[0]) - now
    print(dif)
    sleep(dif * 60)
    s = lessons[sheet[timeCell][day]]
    print(s)
    if lastS != s:
        subprocess.run(["firefox", s])
    lastS = s
    print(s)
    setNow()
    timeCell += 1
