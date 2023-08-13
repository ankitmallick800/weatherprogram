import requests

# API endpoint for hourly weather forecast of London
api_url = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"

def get_weather_data(date):
    params = {
        "location": "London",
        "date": date
    }
    response = requests.get(api_url, params=params)
    data = response.json()
    return data

def main():
    while True:
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")

        choice = int(input("Enter your choice: "))
        
        if choice == 0:
            print("Exiting the program...")
            break
        elif choice in [1, 2, 3]:
            date = input("Enter the date (YYYY-MM-DD): ")
            weather_data = get_weather_data(date)
            
            if choice == 1:
                print(f"Temperature on {date}: {weather_data['temperature']}°C")
            elif choice == 2:
                print(f"Wind Speed on {date}: {weather_data['wind']['speed']} m/s")
            elif choice == 3:
                print(f"Pressure on {date}: {weather_data['pressure']} hPa")
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
