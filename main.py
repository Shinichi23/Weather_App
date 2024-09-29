import requests

api_key = "YOUR API_KEY"

def get_weather():
    city = input("Enter City: ").strip()
    
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        desc = data['weather'][0]['description']
        humidity = data['main']['humidity']
        
        temp_celsius = temp - 273.15
        
        print(f'\nWeather in {city}:')
        print(f'Temperature: {temp_celsius:.2f}°C')
        print(f'Description: {desc.capitalize()}')
        print(f'Humidity: {humidity}%\n')
        
    else:
        print(f"Error fetching weather data for '{city}'. Please check the city name.")

while True:
    get_weather()
    
    while True:
        another_city = input("Would you like to check another city? (yes/no): ").strip().lower()
        
        if another_city == 'yes':
            break  
        elif another_city == 'no':
            print("Goodbye!")
            exit() 
        else:
            print("Please answer with 'yes' or 'no'.")  
