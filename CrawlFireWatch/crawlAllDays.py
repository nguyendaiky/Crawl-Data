import Firewild as fw
from requests import get
from time import sleep
import datetime
import csv

provincesss = [64,66,67,68,62]
provincess = [['Gia Lai',64],['Đắk Lắk',66],['Đắk Nông',67],['Kon Tum',62],['Lâm Đồng',68]]
provinces = [['Gia Lai',64]]

# provinceList = []
# for i in range(len(provinces)):
#     arrT = [provinces[i]]
#     districtJson = fw.GetDistricts(provinces[i][1])
#     districtList = []
#     for district in districtJson:
#         arrH = [[district['ten'],district['ma']]]
#         wardJson = fw.GetWards(provinces[i][1],district['ma'])
#         wards = []
#         for ward in wardJson:
#             wards.append([ward['ten'],ward['ma']])
#         arrH.append(wards)
#         districtList.append(arrH)
#     arrT.append(districtList)
#     provinceList.append(arrT)

# for i in provinceList:
#     for j in i:
#         for k in j:
#             print(k[0])

# for province in provinceList:
#     for district in province:
#         for ward in district:
#             print(ward)

for province in provinces:
    line = []
    provinceCode = province[1]
    line.append(province[0])
    print(provinceCode)
    districts = fw.GetDistricts(provinceCode)
    for district in districts:
        lineDistrict = line.copy()
        districtCode = district['ma']
        lineDistrict.append(district['ten'])
        print(districtCode)
        wards = fw.GetWards(provinceCode,districtCode)
        for ward in wards:
            lineWard = lineDistrict.copy()
            wardCode = ward['ma']
            lineWard.append(ward['ten'])
            print(wardCode)
            dateStart = datetime.datetime(2020,12,31)
            dateEnd = datetime.datetime(2008,1,1)
            while True:
                lineDate = lineWard.copy()
                print(dateStart)
                lineDate.append(dateStart.strftime("%d/%m/%Y"))
                formatedDate = dateStart.strftime('%d!%m!%Y')
                url = f'http://firewatchvn.kiemlam.org.vn/fwdata/search/diaphuong/{provinceCode}/{districtCode}/{wardCode}/{formatedDate}/{formatedDate}/1/100'
                try:
                    res = get(url,timeout=5)
                except:
                    continue
                json = res.json()
                if json:
                    for i in json:
                        print('so diem chay:',i['sdc'])
                        lineDate.append(i['sdc'])
                else:
                    print('so diem chay: 0')
                    lineDate.append(0)
                with open(r'NewData2.csv','a') as f:
                    writer = csv.writer(f)
                    writer.writerow(lineDate)
                if dateStart <= dateEnd:
                    break 
                dateStart -= datetime.timedelta(days=1)

