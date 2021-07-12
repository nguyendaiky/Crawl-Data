import Firewild as fw
from requests import get
from time import sleep
import datetime
import csv

provincesss = [64,66,67,68,62]
provincess = [['Gia Lai',64],['Đắk Lắk',66],['Đắk Nông',67],['Kon Tum',62],['Lâm Đồng',68]]
provinces = [['Gia Lai',64]]

for province in provincess:
    line = []
    provinceCode = province[1]
    line.append(province[0])
    print(provinceCode)
    districts = fw.GetDistricts(provinceCode)
    for district in districts:
        lineDistrict = line.copy()
        districtCode = district['ma']
        lineDistrict.append(district['ten'])
        print(district['ten'])
        dateStart = datetime.datetime(2007,6,1)
        dateEnd = datetime.datetime(2020,7,1)
        while True:
            lineDate = lineDistrict.copy()
            print(dateStart)
            m = int(dateStart.strftime('%m'))
            y = int(dateStart.strftime('%Y'))
            lineDate.append(dateStart.strftime("%d/%m/%Y"))
            formatedDate = dateStart.strftime('%d!%m!%Y')
            if m-1 > 0:
                formatedDateMinus1 = dateStart.replace(month=m-1).strftime('%d!%m!%Y')
            else:
                formatedDateMinus1 = dateStart.replace(month=12, year=y-1).strftime('%d!%m!%Y')
            url = f'http://firewatchvn.kiemlam.org.vn/fwdata/search/diaphuong/{provinceCode}/{districtCode}/0/{formatedDateMinus1}/{formatedDate}/1/100'
            try:
                res = get(url,timeout=5)
            except:
                continue
            json = res.json()
            if json:
                count = 0
                for i in json:
                    count += i['sdc']
                print('so diem chay:',count)
                lineDate.append(count)
            else:
                print('so diem chay: 0')
                lineDate.append(0)
            with open(r'NewDataMonth.csv','a') as f:
                writer = csv.writer(f)
                writer.writerow(lineDate)
            if dateStart >= dateEnd:
                break 
            if m+1 < 13:
                dateStart = dateStart.replace(month=m+1)
            else:
                dateStart = dateStart.replace(month=1, year=y+1)