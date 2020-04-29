import requests
import datetime as dt
from bs4 import BeautifulSoup
from plyer import notification
import time

res = requests.get("https://www.worldometers.info/coronavirus/").text
soup = BeautifulSoup(res, 'html.parser')
soup.encode('utf-8')
cases = soup.find("div", {"class": "maincounter-number"}).get_text().strip()
city_time = dt.datetime.utcnow() + dt.timedelta(hours=3)
f_time = city_time.strftime("%H:%M")

def notifyMe(title, message):
    notification.notify(
        title = title,
        message = message,
        timeout = 15
    )

cou = '0'
while True:
    print (f'Общее число случаев {cases} на {f_time}')
    if cases > cou:
        notifyMe('Общее число случаев', cases)
        cou = cases  
    res = requests.get("https://www.worldometers.info/coronavirus/").text
    soup = BeautifulSoup(res, 'html.parser')
    soup.encode('utf-8')
    cases = soup.find("div", {"class": "maincounter-number"}).get_text().strip()
    city_time = dt.datetime.utcnow() + dt.timedelta(hours=3)
    f_time = city_time.strftime("%H:%M")
    time.sleep(10)
time.sleep(1000)
input()