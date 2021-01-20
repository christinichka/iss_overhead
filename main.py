import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = "XXXXXXXXXXX@gmail.com"
MY_PASSWORD = "XXXXXXXXXXXXX"
MY_LAT = 38.548330
MY_LONG = -90.326280


def is_iss_overhead():
	response = requests.get(url="http://api.open-notify.org/iss-now.json")
	response.raise_for_status()
	data = response.json()

	longitude = data["iss_position"]["longitude"]
	latitude = data["iss_position"]["latitude"]

	iss_position = (longitude, latitude)
 
	print(F"ISS POSITION: {iss_position}") 

	#Your position is within +5 or -5 degrees of the ISS position.
	if MY_LAT-5 <= iss_latitude  <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
		return True


def night_time():
	parameters = {
	    "lat": MY_LAT,
	    "lng": MY_LONG,
	    "formatted": 0,
	}

	response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
	response.raise_for_status()
	data = response.json()
	 
	MY_ZONE = ZoneInfo("America/Louisville")   
	time_now = str(datetime.now(tz=MY_ZONE)).split(" ")[1].split(":")
	sunrise = str(datetime.fromisoformat(data["results"]["sunrise"]).astimezone(tz=MY_ZONE)).split(" ")[1].split(":")
	sunset = str(datetime.fromisoformat(data["results"]["sunset"]).astimezone(tz=MY_ZONE)).split(" ")[1].split(":")
	 
	print(f"sunrise: {sunrise[0]}")      
	print(f"sunset: {sunset[0]}")       
	 
	time_now = datetime.now()
	 
	print(f"time_now_hour : {time_now.hour}")  

	if time_now >= sunset or time_now <= sunrise:
		return True

while True:
	time.sleep(60)
	if is_iss_overhead() and night_time():
			connection = smtplib.SMTP("smtp.gmail.com", 587)
			connection.starttls()
			connection.login(MY_EMAIL, MY_PASSWORD)
			connection.sendmail(
				from_addr=MY_EMAIL,
				to_addrs=MY_EMAIL,
				msg="Subject:Look Up ☝️\n\nThe ISS is above you in the sky.")




