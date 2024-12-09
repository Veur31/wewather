import requests
import os
def clear():
    choice = input("Go back to main menu? (Y/N): ").upper()
    if choice == 'Y':
        os.system('cls')
        main()
    else:
        os.system('cls')
def line():
    print("-" * 50)

def weather(api, city):
    url =   "http://api.openweathermap.org/data/2.5/weather" 
    params = {
        "q" : city,
        "appid" : api,
        "units" : "metric"
    }
    try:
        response = requests.get(url, params)
        response.raise_for_status()
        data = response.json()
        print(data)
        city_name = data["name"]
        country = data["sys"]["country"]
        temperature = data["main"]["temp"]
        weather =data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        sea_level = data["main"]["sea_level"]
        weather1 =data["weather"][0]["main"]
        print()
        print(f"City name: {city_name}")
        print(f"Country: {country}")
        print(f"Temperature: {temperature}")
        print(f"Weather: {weather}. Main weather: {weather1}")
        print(f"Humidity: {humidity}")
        print(f"Sea level: {sea_level}")
    except requests.exceptions.HTTPError as error:
        print(f"There had been a problem accessing the url, {error}")
    except requests.exceptions.RequestException as e:
        print(f"There had been a problem accessing the url, {e}")
    except KeyError:
        print("Your request has been denied")
def main():
    print("Welcome to weather PROGRAM")
    api = "4579dbc809c4fd75dc94ac920f0a14c3"

    while True:
        print()
        print("1. Check the weather\n2. Exit")
        print()
        choice = int(input("Enter your choice: "))
        try:
            if choice == 1:
                print()
                line()
                city = input("Enter city name: ").strip()
                weather(api, city)
                clear()
                line()
            elif choice == 2:
                print("Exiting the program")
                break
            else:
                print("Please, Input valid choice")
        except ValueError:
            print("Please, Input valid choice")
main()
        

            
            
            








































"""
import requests

def weather(city, api):
    base_url = "http://api.openweathermap.org/data/2.5/weather" 
    params = {
        "q": city,
        "appid": api,
        "units": "metric"
    }
    try:
        response = requests.get(base_url, params)
        response.raise_for_status()
        data =response.json()
        print(data)
        city_name = data["name"]
        country = data["sys"]["country"]
        temperature = data["main"]["temp"]
        weather = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        wind_speed =data["wind"]["speed"]

        print(f"\nWeather in {city_name}, {country}:")
        print(f"Temperature: {temperature}°C")
        print(f"Condition: {weather.capitalize()}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
    except requests.exceptions.HTTPError as http_err:
        print("HTTP error occurred:", http_err)
    except requests.exceptions.RequestException as req_err:
        print("Request error:", req_err)
    except KeyError:
        print("City not found or unexpected response format!")
def main():
    print("Welcome to the Weather App!")
    api_key = "4579dbc809c4fd75dc94ac920f0a14c3"  # Replace with your actual API key

    while True:
        print("\nMenu:")
        print("1. Check Weather")
        print("2. Exit")
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                city = input("Enter the city name: ").strip()
                weather(city, api_key)
            elif choice == 2:
                print("Thank you for using the Weather App. Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Run the app
main()
"""