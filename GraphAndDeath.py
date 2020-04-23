import time
import matplotlib.pyplot as plt
import requests
import datetime
from datetime import timedelta
import numpy as np

def graph(country):
    gdate = str(time.strftime(r"%m-%d-%Y", time.localtime()))
    dm1 = f'{gdate[3]}{gdate[4]}'
    dm2 = str((int(dm1))-1)
    gdate = gdate.replace(dm1, dm2)
    sdate = ('01-22-2020')
    gdate2 = datetime.date.today()
    gdate3 = datetime.date(2020, 1, 22)
    dayspass = str(gdate2-gdate3)
    zerotime = dayspass.find('0:00:0')
    numdaypass = dayspass[:zerotime-7]
    numdaypass = (int(numdaypass))
    x = []
    y = []
    for i in range(0, numdaypass):
        g = str(datetime.date(2020, 1, 22) + timedelta(days=i))
        year = f'{g[0]}{g[1]}{g[2]}{g[3]}'
        month = f'{g[5]}{g[6]}'
        date = f'{g[8]}{g[9]}'
        ndate = f'{month}-{date}-{year}'

        url = f"https://covid1910.p.rapidapi.com/data/confirmed/country/{country}/date/{ndate}"
        headers = {
            'x-rapidapi-host': "covid1910.p.rapidapi.com",
            'x-rapidapi-key': "96c395c12bmsh7977f2a7f725335p156aa1jsn3256842e9bbc"}
        response = requests.request("GET", url, headers=headers)
        rt = response.text
        rt = rt.replace('"', '')
        rt = rt.replace('[', '')
        rt = rt.replace('{', '')
        rt = rt.replace('}', '')
        rt = rt.replace(']', '')
        rt1 = rt.find('med:')
        confirmed = rt[rt1+4:]
        y.append(confirmed)
        x.append(i)

    plt.plot(x, y)
    print(y)
    plt.xlabel('Days')
    plt.ylabel('Cases')
    if country == 'us':
        capcountry3 = 'U.S.A.'
    else:
        capcountry1 = ord(country[0])-32
        capcountry2 = chr(capcountry1)
        capcountry3 = country.replace(country[0], capcountry2)
    plt.title(f'Cases in {capcountry3}')

    plt.yticks(np.arange(min(x), 70, 4.0))

    plt.show()

def death(country):
    gdate = str(time.strftime(r"%m-%d-%Y", time.localtime()))
    dm1 = f'{gdate[3]}{gdate[4]}'
    dm2 = str((int(dm1))-1)
    gdate = gdate.replace(dm1, dm2)
    sdate = ('01-22-2020')
    gdate2 = datetime.date.today()
    gdate3 = datetime.date(2020, 1, 22)
    dayspass = str(gdate2-gdate3)
    zerotime = dayspass.find('0:00:0')
    numdaypass = dayspass[:zerotime-7]
    numdaypass = (int(numdaypass))
    x = []
    y = []
    for i in range(0, numdaypass):
        g = str(datetime.date(2020, 1, 22) + timedelta(days=i))
        year = f'{g[0]}{g[1]}{g[2]}{g[3]}'
        month = f'{g[5]}{g[6]}'
        date = f'{g[8]}{g[9]}'
        ndate = f'{month}-{date}-{year}'

        url = f"https://covid1910.p.rapidapi.com/data/death/country/{country}/date/{ndate}"
        headers = {
            'x-rapidapi-host': "covid1910.p.rapidapi.com",
            'x-rapidapi-key': "96c395c12bmsh7977f2a7f725335p156aa1jsn3256842e9bbc"}
        response = requests.request("GET", url, headers=headers)
        rt = response.text
        rt = rt.replace('"', '')
        rt = rt.replace('[', '')
        rt = rt.replace('{', '')
        rt = rt.replace('}', '')
        rt = rt.replace(']', '')
        rt1 = rt.find('ath:')
        confirmed = rt[rt1+4:]
        y.append(confirmed)
        x.append(i)

    plt.plot(x, y)
    print(y)
    plt.xlabel('Days')
    plt.ylabel('Death')
    if country == 'us':
        capcountry3 = 'U.S.A.'
    else:
        capcountry1 = ord(country[0])-32
        capcountry2 = chr(capcountry1)
        capcountry3 = country.replace(country[0], capcountry2)
    plt.title(f'Deaths in {capcountry3}')

    plt.yticks(np.arange(min(x), 70, 4.0))

    plt.show()

if __name__ == "__main__":
    graph("united kingdom")
