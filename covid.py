import requests
from datetime import datetime


def formatNumber(num):
    numStr = str(num)
    result = ''
    while len(numStr) > 3:
        result = f'.{numStr[-3:]}{result}'
        numStr = numStr[0:len(numStr)-3]
    if numStr:
        result = numStr + result
    return result


def main():
    print('Welcome sir, I have some infomation about Covid-19 in VietNam for you')
    while True:
        com = input('Enter "y" to get more information, or any key to close: ')
        if com == 'y':
            # get json from url
            infoJSON = requests.get(
                'https://corona.lmao.ninja/v2/countries/vn')
            # convert from json to direction
            info = infoJSON.json()
            updated = str(info['updated'])[:10]
            timeUpdate = datetime.fromtimestamp(
                float(updated)).strftime('%d-%M-%Y %H:%M:%S')
            cases = formatNumber(info['cases'])
            todayCases = formatNumber(info['todayCases'])
            deaths = formatNumber(info['deaths'])
            todayDeaths = formatNumber(info['todayDeaths'])
            recovered = formatNumber(info['recovered'])
            print(f'Date Time Update: {timeUpdate}\n')
            print(f'Case: {cases}\n')
            print(f'Today Cases: {todayCases}\n')
            print(f'Deaths: {deaths}\n')
            print(f'Today Deaths: {todayDeaths}\n')
            print(f'Recovered: {recovered}\n')
        else:
            quit()


if __name__ == '__main__':
    main()
