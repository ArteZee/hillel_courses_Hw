import requests

city_name: str = input('please fill up your city ')
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?'
API_KEY = 'd82759ebf4a4a5ed987117c4027b9dfa'  # if api_key not works, generate yours on website
complete_url = BASE_URL + "appid=" + API_KEY + "&q=" + city_name
response = requests.get(complete_url)
r_data: dict = response.json()
# Kelvins degrees  to change in celsius degrees
KELVIN = 273.15


def get_weather():
    """
    Output information about weather in users city

    :return: str: information od weather or City did not find
    """
    if r_data["cod"] != "200":
        name_city = r_data["name"]
        temp_inform = r_data['main']
        current_t = round((temp_inform['temp'] - KELVIN))
        current_p = temp_inform["pressure"]
        wind_inform = r_data["wind"]
        speed_wind = wind_inform["speed"]
        return (f'Today in {name_city} \n'
                f'temperature - {current_t}°C\n'
                f'pressure - {current_p}\n'
                f'speed of wind - {speed_wind} m/s\n')
    else:
        return "City did not find "


def speed_wind():
    """ Information of winds speed """
    wind_inform = r_data["wind"]
    speed_winds = wind_inform["speed"]

    return f'wind is {speed_winds}, m/s'


def temperature(user_city):
    """
    function that get temperature of city and output Hot if temp more than 25 else output Warm
    :param user_city:str -Name of city

    :return:str: Hot or Warm
    """

    complete_url = BASE_URL + "appid=" + API_KEY + "&q=" + user_city
    response = requests.get(complete_url)
    r_data = response.json()
    KELVIN = 273.15
    temp_inform = r_data['main']
    current_t = round((temp_inform['temp'] - KELVIN))
    if current_t >= 25:
        return 'Hot'
    else:
        return 'Warm'


if __name__ == "__main__":
    print(get_weather())
    print(temperature("Odessa"))
    print(temperature("London"))
    print(speed_wind())
