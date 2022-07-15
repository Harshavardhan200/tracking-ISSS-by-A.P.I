import time

import requests
from datetime import datetime
import smtplib as sm
import pandas as pd
data = pd.read_csv('birthdays.csv')
record = data.to_dict(orient='records')
mail_name = [{'name': i['name'], 'email': i['email']} for i in record]
MY_LAT = 14.660579
MY_LONG = 78.172959

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

#If the ISS is close to my current position
while True:
    print('hello')
    time.sleep(60)
    if datetime.now().hour < 5 or datetime.now().hour > 19 or MY_LAT-5 < iss_latitude < MY_LAT+5 and MY_LONG-5 < iss_longitude < MY_LONG+5:
        with sm.SMTP_SSL('smtp.gmail.com') as mail:
            you = 'sanalakshmiprasanna79@gmail.com'
            p = 'harsha13062002@'
            mail.login(user=you, password=p)
            for i in mail_name:
                mail.sendmail(from_addr=you, to_addrs=i['email'], msg=f'subject:ISS is nearer to you\n\nmain body:{i["name"]} go out and lookup to see the iss')
                print(i)
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



