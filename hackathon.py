
# import required modules
import requests, json
  
# Enter your API key here
api_key = "72cded68516eb3ae5ba966facd25e937"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name = input("Enter city name : ")
complete_url = base_url + "appid=" + api_key + "&q=" + city_name
response = requests.get(complete_url)
x = response.json()

if x["cod"] != "404":
    y = x["main"]
    z = x["weather"]
    w = z[0]["description"]
    
    
    if w == 'clear sky' or w == 'few clouds':
        print("Clear")
    elif w == 'scattered clouds' or w == 'broken clouds' or w == 'shower rain' or w == 'rain' or w == 'thunderstorm':
        print("Bad")
    else:
        print("Ugly")
        
