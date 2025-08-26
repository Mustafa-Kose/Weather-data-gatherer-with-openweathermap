import requests
import os

#Veri çağırma bilgileri
with open("apikey.txt", "r") as f:
    API_KEY = f.read()

url="https://api.openweathermap.org/data/2.5/weather"



def infoWeWant():
    city=input("""Enter the city you want to check the weather for. Example names:
        - Istanbul
        - New York
        - Paris
        - London
        - Tokyo
        - Moscow
        - Berlin
        : """).capitalize().strip()
    os.system('cls') 
    

    while True:
        unitcaller=input("""Select the unit system you want:
            -1 for Metric(°C,m/s)
            -2 for Imperial(°F,mph)
            -3 for Standart(Kelvin,m/s)
            : """).capitalize().strip()
        os.system('cls') 
        if unitcaller == "1":
            units="Metric"
            break
        elif unitcaller == "2":
            units="Imperial"
            break
        elif unitcaller == "3":
            units="Standart"
            break
        else:
             print("""Pleas choose from 1-3
                      -1 for Metric(°C,m/s)
                      -2 for Imperial(°F,mph)
                      -3 for Standart(Kelvin,m/s)       
            """,end="\r")
             continue

    try:
            #OpenWeatherMap'ten istenen veriler
            informationsFromOWM  = {
            "q": city,        
            "appid": API_KEY, 
            "units": units,
            "lang": "en"      
            }

            #bize gelen bilgiler
            cagrilar= requests.get(url, params=informationsFromOWM)
            data=cagrilar.json()
            
            #Sonuç
            print(
            "City:", data["name"],
            "Weather:", data["weather"][0]["description"],
            "Temperature:", data["main"]["temp"], "°C",
            "Feels like:", data["main"]["feels_like"], "°C",
            "Humidity:", data["main"]["humidity"], "%"
            )
    except Exception as eror:
         print(f"Eror: {eror}",end="\r")
         os.system('cls') 

while True:

    infoWeWant()
    input("")
