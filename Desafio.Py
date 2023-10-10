import pandas as pd
import requests
import json
import openai

# Chave da API OpenWeatherMap (obtenha a sua em https://openweathermap.org/)
api_key = 'SUA_CHAVE_DA_API_OPENWEATHERMAP'

# Função para buscar e exibir informações meteorológicas
def get_weather(city_name):
    try:
        # URL da API OpenWeatherMap para buscar o clima atual
        current_weather_url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'

        # Faz a solicitação GET para a API
        current_weather_response = requests.get(current_weather_url)

        # Verifica se a solicitação foi bem-sucedida
        if current_weather_response.status_code == 200:
            current_weather_data = current_weather_response.json()
            
            # Exibe o clima atual para o usuário
            print(f"Clima atual em {city_name}:")
            print(f"Tempo: {current_weather_data['weather'][0]['description']}")
            print(f"Temperatura: {current_weather_data['main']['temp']}°C")
            print(f"Umidade: {current_weather_data['main']['humidity']}%")
            
            # URL da API OpenWeatherMap para buscar a previsão do tempo
            forecast_url = f'https://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={api_key}'
            
            # Faz a solicitação GET para a API
            forecast_response = requests.get(forecast_url)
            
            # Verifica se a solicitação foi bem-sucedida
            if forecast_response.status_code == 200:
                forecast_data = forecast_response.json()
                
                # Exibe a previsão para os próximos dias
                print("\nPrevisão para os próximos dias:")
                for forecast in forecast_data['list']:
                    date = forecast['dt_txt']
                    temperature = forecast['main']['temp']
                    description = forecast['weather'][0]['description']
                    print(f"Data: {date}, Temperatura: {temperature}°C, Tempo: {description}")
                    
            else:
                print("Não foi possível obter a previsão do tempo.")
            
        else:
            print("Não foi possível obter as informações meteorológicas.")

    except Exception as e:
        print(f"Ocorreu um erro: {str(e)}")

if _name_ == "_main_":
    city_name = input("Digite o nome da cidade para verificar o clima: ")
    get_weather(city_name)
