import json
import urllib.request
from pprint import pprint


def get_local_weather():

    weather_base_url = 'http://forecast.weather.gov/MapClick.php?FcstType=json&'

    places = {
        'Austin': ['30.3074624', '-98.0335911'],
        'Portland': ['45.542094', '-122.9346037'],
        'NYC': ['40.7053111', '-74.258188']
    }

    for place in places:
        latitude, longitude = places[place][0], places[place][1]
        weather_url = weather_base_url + "lat=" + latitude + "&lon=" + longitude
        # Show the URL we use to get the weather data. (Paste this URL into your browser!)
        # print("Getting the current weather for", place, "at", weather_url, ":")

        page_response = urllib.request.urlopen(weather_url).read()
        weather_data = json.loads(page_response.decode('utf-8'))

        # (Ugly) print the raw JSON data that we get back from the URL.
        # print(weather_data)

        forecast = parse_weather_data(weather_data)

        print("Today's date is", forecast['date'],
            "and the current temperature in", place, forecast['state'],
            "is", forecast['temp'], "degrees")

def parse_weather_data(json_object):
    # What type of object is json_object?
    # print(type(json_object))
    
    # Pretty Print the JSON data that we get back from the URL.
    # pprint(json_object)

    weather_obj = json_object

    todays_date = weather_obj['currentobservation']['Date']
    current_temp = weather_obj['currentobservation']['Temp']
    outlook = weather_obj['currentobservation']['Weather']
    state = weather_obj['currentobservation']['state']

    current_weather = {
        'date': todays_date,
        'temp': current_temp,
        'outlook': outlook,
        'state': state,
    }

    return current_weather


def main():
    get_local_weather()

if __name__ == "__main__":
    main()
