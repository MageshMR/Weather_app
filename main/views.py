from django.shortcuts import render
import requests

def index(request):
    weather_data = {}
    if request.method == 'POST':
        city = request.POST.get('city')
        if city:
            api_key = 'writ your own weather api key'  # Replace with your OpenWeatherMap API key
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
               # print(f"[DEBUG] API Response Code: {response.status_code}")

                weather_data = {
                    'city': data['name'],
                    'country': data['sys']['country'],
                    'temperature': data['main']['temp'],
                    'description': data['weather'][0]['description'],
                    'icon': data['weather'][0]['icon'],
                }
                print(f"[DEBUG] Parsed Weather Data: {weather_data}")

            else:
                weather_data['error'] = 'City not found or API error.'
                

    return render(request, 'main/index.html', {'weather': weather_data})
