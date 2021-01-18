import requests
from datetime import datetime

MY_LAT = 51.507351
MY_LONG = -0.127758
LOCAL_UTC_OFFSET = 6

#response = requests.get(url="http://api.open-notify.org/iss-now.json")
#response.raise_for_status()

#data= response.json()

#longitude = data["iss_position"]["longitude"]
#latitude = data["iss_position"][latitude]

#iss_position = (longiture, latitude)

#print(iss_position)

def utc_to_local(utc_hour):
	utc_hour += LOCAL_UTC_OFFSET
	if LOCAL_UTC_OFFSET > 0:
		if utc_hour > 23:
			utc_hour -= 24
	elif LOCAL_UTC_OFFSET < 0:
		if utc_hour < 0:
			utc_hour += 24
	return utc_hour

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

lt_sunrise = utc_to_local(sunrise)
lt_sunset = utc_to_local(sunset)

print(sunrise)
print(sunset)

time_now = datetime.now()
print(time_now.hour)