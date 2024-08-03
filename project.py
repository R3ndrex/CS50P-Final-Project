import geocoder  # type: ignore 
import requests  # type: ignore
import matplotlib.pyplot as plt # type: ignore
import argparse

URL = "https://api.openweathermap.org/data/2.5/weather?"
API = "8faa0fdf378d1e477bbe2071dc516d9f"
UNITLIST = ["standard", "metric", "imperial"]
REQUIRED_KEYS = ["name", "sys", "weather", "main", "wind"]

def get_response(city, units="metric",lang=""):
    if units.strip().lower() not in UNITLIST:
        raise ValueError("Units is incorectly defined")
    call = f"{URL}q={city}&appid={API}&units={units}&lang={lang.strip().lower()}"
    try:
        response = requests.get(call).json()
    except requests.RequestException as e:
        raise SystemExit(e)
    if response["cod"]=="404" or response["cod"]=="400":
        raise ValueError("City not found")
    return response

def print_info(response) -> None:
    check_response(response)
    print(f"City: {response['name']} ({response["sys"]["country"]})")
    print(f"Description: {response['weather'][0]['description']}")
    print(f"Temperature: {response['main']['temp_min']}-{response['main']['temp_max']} ({response['main']['temp']})")
    print(f"Feels like: {response['main']['feels_like']}")
    print(f"Humidity: {response['main']['humidity']}")
    print(f"Visibility: {response['visibility']}")
    print(f"Wind: speed: {response['wind']['speed']}, degree: {response['wind']['deg']}")


def get_city_input(prompt=""):
    if prompt is None:
        raise ValueError("Prompt is not defined")
    if type(prompt) is int:
        raise ValueError("Prompt cant be a number")
    match prompt.strip().lower():
        case "n":
            return input("Enter your city: ")
        case "y":
            return geocoder.ip("me").city
        case _:
            raise ValueError("-n should end with y or n")

def check_response(response)-> None:
    if not all(key in response for key in REQUIRED_KEYS):
        raise ValueError("Invalid response")
    
def visualize_weather(response = "")->None:
    if response is None:
        raise ValueError("Response cant be None")
    check_response(response)
    temperatures = [
        response['main']['temp_min'],
        response['main']['temp'],
        response['main']['temp_max'],
        response['main']['feels_like']
        ]
    labels = ['Min Temp', 'Current Temp', 'Max Temp', 'Feels Like'] 
    adjusted_temperatures = [temp - -20  for temp in temperatures]
    
    plt.figure(figsize=(8, 6))
    plt.bar(labels, adjusted_temperatures, bottom=-20 )
    plt.title(f"Temperature in {response['name']} ({response['sys']['country']})",pad=25)
    plt.ylabel('Temperature')
    plt.ylim(-20, max(temperatures) + 10)
    for i, v in enumerate(temperatures):
        plt.text(i, v, f"{v:.1f}", ha='center', va='bottom')
    plt.show()

def main():
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("-r", default = "y", help = "Retrieve city automatically? (y/n): ", type=str)
        parser.add_argument("-g", default = "y", help = "Create graph for weather? (y/n): ", type=str)
        parser.add_argument("-u", default = "standard", help = "Enter your units (standard, metric or imperial): ", type=str)
        parser.add_argument("-l", default = "", help = "Enter your language (UA, TR, HI etc): ", type=str)
        args = parser.parse_args()
        city = get_city_input(args.r)
        response = get_response(city, args.u,args.l)
        print_info(response)
        if args.g.strip().lower()=="y":
            visualize_weather(response)
        elif args.g.strip().lower()!="n":
            raise ValueError("-g should end with y or n") 
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()