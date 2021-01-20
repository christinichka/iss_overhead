import requests
from datetime import datetime
from zoneinfo import ZoneInfo
# import dateutil.parser
# from pytz import timezone

MY_LAT = 38.548330
MY_LONG = -90.326280
LOCAL_UTC_OFFSET = 6

#------ ISS POSITION
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()

latitude = data["iss_position"]["latitude"]
longitude = data["iss_position"]["longitude"]

iss_position = (longitude, latitude)

print(f"ISS Position: {iss_position}")

#-------LOCAL TIME
parameters = {
	"lat": MY_LAT,
	"lng": MY_LONG,
	"formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

# for tz in pytz.all_timezones:
#     print(tz)

MY_ZONE = ZoneInfo("America/Kentucky/Louisville") 
time_now = str(datetime.now(tz=MY_ZONE)).split(" ")[1].split(":")
sunrise = str(datetime.fromisoformat(data["results"]["sunrise"].astimezone(tz=MY_ZONE)).split(" ")[1].split(":"))
sunset = str(datetime.fromisoformat(data["results"]["sunset"].astimezone(tz=MY_ZONE)).split(" ")[1].split(":"))


print(f"sunrise: {sunrise[0]}")
print(f"sunset: {sunset[0]}")

time_now = datetime.now()

print(f"time_now.hour : {time_now.hour}")