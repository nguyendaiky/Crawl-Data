from requests import get
import datetime
import csv
import Firewild as fw

listTinhh = [['Gia Lai',64],['Đắk Lắk',66],['Đắk Nông',67],['Kon Tum',62],['Lâm Đồng',68]]

def check_year(year): 
    return (((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0))

def day_of_month(month,year):
    if month in [1,3,5,7,8,10,12]:
        return 31
    elif month in [4,6,9,11]:
        return 30
    elif month == 2:
        if check_year(year):
            return 29
        else:
            return 28

listTinh = fw.GetAllProvinces()
for t in listTinhh:
    toado = []
    # tinhCode = t['ma']
    tinhCode = t[1]
    print(t[0])
    # toado.append(t['ten'])
    toado.append(t[0])
    listHuyen = fw.GetDistricts(tinhCode)
    for h in listHuyen:
        huyenCode = h['ma']
        print(h['ten'])
        toadoH = toado.copy()
        toadoH.append(h['ten'])
        url = f'http://firewatchvn.kiemlam.org.vn/fwdata/search/diaphuong/{tinhCode}/{huyenCode}/0/01!01!2007/05!07!2021/1/100'
        res = get(url)
        data = res.json()
        for d in data:
            print(d['xa'])
            toadoX = toadoH.copy()
            toadoX.append(d['xa'])
            print('{},{}'.format(d['y'],d['x']))
            toadoX.append(d['y'])
            toadoX.append(d['x'])
            with open(r'NewLongLat.csv','a') as f:
                writer = csv.writer(f)
                writer.writerow(toadoX)
                
            # url = 'https://dsx.weather.com/wxd/v3/PastObsAvg/en_US/{}/42/{}?format=json&apiKey=7bb1c920-7027-4289-9c96-ae5e263980bc'
            # y = round(float(d['y']),2)
            # x = round(float(d['x']),2)
            # xy = str(y)+','+str(x)
            # date = '20210101'
            # weatherRes = get(url.format(date,xy))
            # print(weatherRes.json())
            

# listProvince = [
#     ['Gia Lai','https://dsx.weather.com/wxd/v3/PastObsAvg/en_US/{}/42/13.81,108.09?format=json&apiKey=7bb1c920-7027-4289-9c96-ae5e263980bc'],
#     ['Đắk Lắk','https://dsx.weather.com/wxd/v3/PastObsAvg/en_US/{}/42/12.78,108.36?format=json&apiKey=7bb1c920-7027-4289-9c96-ae5e263980bc'],
#     ['Đắk Nông','https://dsx.weather.com/wxd/v3/PastObsAvg/en_US/{}/42/12.22,107.67?format=json&apiKey=7bb1c920-7027-4289-9c96-ae5e263980bc'],
#     ['Kon Tum','https://dsx.weather.com/wxd/v3/PastObsAvg/en_US/{}/42/14.38,107.97?format=json&apiKey=7bb1c920-7027-4289-9c96-ae5e263980bc'],
#     ['Lâm Đồng','https://dsx.weather.com/wxd/v3/PastObsAvg/en_US/{}/42/11.48,108.18?format=json&apiKey=7bb1c920-7027-4289-9c96-ae5e263980bc'],
# ]

# for p in range(len(listProvince)):
#     dateStart = datetime.datetime(2021,6,1)
#     dateEnd = datetime.datetime(2020,1,1)
#     while True:
#         print(dateStart.strftime('%d/%m/%Y'))
#         formatedDate = dateStart.strftime('%Y%m%d')
#         url = listProvince[p][1].format(formatedDate)
#         res = get(url)
#         data = res.json()
#         m = int(dateStart.strftime('%m'))
#         y = int(dateStart.strftime('%Y'))
#         count = 0
#         for i in range(day_of_month(m,y)):
#             province = listProvince[p][0]
#             max_temp = data[i]['Temperatures']['highC']
#             min_temp = data[i]['Temperatures']['lowC']
#             date = data[i]['Temperatures']['highTmISO'][:10]
#             precip = data[i]['Precips']['mtdPrecipCm']
#             date = datetime.datetime.strptime(date,'%Y-%m-%d').strftime('%d/%m/%Y')
#             wx = data[0]['WxDetails']['wx']
#             print(date)
#             print(province)
#             print(max_temp)
#             print(min_temp)
#             print(wx)
#             print(precip)
#             line = [date,province,max_temp,min_temp,wx,precip]
#             with open(r'NewWeather.csv','a') as f:
#                 writer = csv.writer(f)
#                 writer.writerow(line)
#             count += 1
#         print(count)

#         if dateStart <= dateEnd:
#             break 

#         if m-1 > 0:
#             dateStart = dateStart.replace(month=m-1)
#         else:
#             dateStart = dateStart.replace(month=12, year=y-1)




