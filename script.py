import requests

API_KEY = "b6907d289e10d714a6e88b30761fae22"
BASE_URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly?"
CITY = "London,us"

def get_weather_data():
    url = f"{BASE_URL}q={CITY}&appid={API_KEY}"
    response = requests.get(url)
    return response.json()

def get_temperature_by_date(date):
    data = get_weather_data()
    for forecast in data['list']:
        if date in forecast['dt_txt']:
            return forecast['main']['temp']

def get_wind_speed_by_date(date):
    data = get_weather_data()
    for forecast in data['list']:
        if date in forecast['dt_txt']:
            return forecast['wind']['speed']

def get_pressure_by_date(date):
    data = get_weather_data()
    for forecast in data['list']:
        if date in forecast['dt_txt']:
            return forecast['main']['pressure']

def main():
    while True:
        print("Choose an option:")
        print("1. Get temperature")
        print("2. Get wind speed")
        print("3. Get pressure")
        print("0. Exit")
        
        choice = int(input())
        
        if choice == 0:
            break
        
        date = input("Enter the date (YYYY-MM-DD HH:MM:SS): ")
        
        if choice == 1:
            temperature = get_temperature_by_date(date)
            print(f"Temperature on {date}: {temperature} K")
        elif choice == 2:
            wind_speed = get_wind_speed_by_date(date)
            print(f"Wind Speed on {date}: {wind_speed} m/s")
        elif choice == 3:
            pressure = get_pressure_by_date(date)
            print(f"Pressure on {date}: {pressure} hPa")

if __name__ == "__main__":
    main()
