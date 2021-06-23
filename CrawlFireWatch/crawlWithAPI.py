from datetime import datetime
import datetime
import pandas as pd
import requests
import json

# Hòa Bình, Điện Biên, Sơn La, Lai Châu, Thanh Hóa ✔, Nghệ An ✔, Hà Tĩnh ✔, 
# Quảng Bình ✔, Quảng Trị ✔, Thừa Thiên Huế ✔, Quảng Nam ✔, Quảng Ngãi ✔, Bình Định ✔, 
# Phú Yên ✔, Khánh Hòa ✔ và thành phố Đà Nẵng ✔
listTinh = [['Gia Lai',64],['Đắk Lắk',66],['Đắk Nông',67],['Kon Tum',62],['Lâm Đồng',68],['Thanh Hoá',38],['Nghệ An',40],['Hà Tĩnh',42],['Quảng Bình',44],['Quảng Trị',45],['Thừa Thiên Huế',46]]
listTinh2 = [['Đà Nẵng',48],['Quảng Nam',49],['Quảng Ngãi',51],['Bình Định',52],['Phú Yên',54],['Khánh Hòa',56],['Ninh Thuận',58],['Bình Thuận',60]]
listTinh3 = [['Hòa Bình',17],['Điện Biên',11],['Sơn La',14],['Lai Châu',12],['Bắc Giang',24],['Bắc Kạn','06'],['Cao Bằng','04'],['Lạng Sơn',20],['Quảng Ninh','22'],['Hà Giang','02'],['Lào Cai',10],['Phú Thọ',25],['Thái Nguyên',19],['Tuyên Quang','08'],['Yên Bái',15]]
def take_data():
    start = datetime.datetime.now().strftime("%H:%M:%S")
    dateStart = datetime.datetime(2019,6,30)
    dateEnd = datetime.datetime(2007,1,1)
    tinhName = listTinh3[13][0]
    tinhCode = listTinh3[13][1]
    while True:
        line = {}
        date = dateStart.strftime('%d!%m!%Y')
        url = 'http://firewatchvn.kiemlam.org.vn/fwdata/search/diaphuong/{tinhCode}/0/0/{date}/{date}/1/100'.format(date=date,tinhCode=tinhCode)
        t = requests.get(url).text
        dfTinh = pd.json_normalize(json.loads(t))

        print('==============================================================================================================')
        line['Ngay'] = dateStart.strftime("%d/%m/%Y")
        print(dateStart.strftime("%d/%m/%Y"))
        line['Tinh'] = tinhName
        print(tinhName)
        try:
            huyen = dfTinh[['code','huyen']]
            print(huyen)
            huyenCode = huyen['code'].values
            huyenName = huyen['huyen'].values
            for i in range(len(huyenName)):
                line['Huyen'] = huyenName[i]
                print(huyenName[i])
                x = requests.get('http://firewatchvn.kiemlam.org.vn/fwdata/search/diaphuong/{tinhCode}/{huyenCode}/0/{date}/{date}/1/100'.format(date=date,tinhCode=tinhCode,huyenCode=huyenCode[i]))
                x = x.text
                dfHuyen = pd.json_normalize(json.loads(x))

                xa = dfHuyen[['xa','hp']]
                xaName = xa['xa'].values
                xaTD = xa['hp'].values
                print(xaName)
                TD = []
                for j in range(len(xaName)):
                    line['Xa'] = xaName[j]
                    print(xaName[j])
                    for k in range(len(xaTD[j])):
                        dataAPI = line.copy()
                        dfXa = pd.json_normalize(xaTD[j][k])
                        print(dfXa[['x','y']])
                        dataAPI['Kinh Do'] = dfXa['x'].values[0]
                        dataAPI['Vi Do'] = dfXa['y'].values[0]
                        with open('DataAPI.txt','a') as f:
                            json.dump(dataAPI,f)
                            f.write('\n')
        except:
            print('None')
        if dateStart <= dateEnd:
            break 
        dateStart -= datetime.timedelta(days=1)
    end = datetime.datetime.now().strftime("%H:%M:%S")
    print('Done! (start: {start}, end: {end})'.format(start=start,end=end))

def convert_to_csv(path):
    with open(path,'rb') as f:
        data = f.readlines()
    data = map(lambda x: x.rstrip(),data)
    data_json_string = b'[' + b','.join(data) + b']'
    # data_df = pd.read_json(data_json_string)
    data_df = pd.json_normalize(json.loads(data_json_string))
    print(data_df.head(10))
    data_df.to_csv('GiaLai.csv',index=None,encoding='utf-8-sig')

if __name__ == "__main__":
    # take_data()
    convert_to_csv('Data\GiaLai.txt')
