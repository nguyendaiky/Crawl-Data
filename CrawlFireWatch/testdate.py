import datetime

dateStart = datetime.datetime(2021,6,15)
dateEnd = datetime.datetime(2021,1,1)
while True:
    print(dateStart.strftime("%d/%m/%Y")) 
    if dateStart == dateEnd:
        break 
    dateStart -= datetime.timedelta(days=1)