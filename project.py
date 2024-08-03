import geocoder  # type: ignore 
import requests  # type: ignore
import matplotlib.pyplot as plt # type: ignore

URL = "https://api.openweathermap.org/data/2.5/weather?"
API = "8faa0fdf378d1e477bbe2071dc516d9f"
UNITLIST = ["standard", "metric", "imperial"]
REQUIRED_KEYS = ["name", "sys", "weather", "main", "wind"]

def get_response(city, units="metric",lang=""):
    if units.strip().lower() not in UNITLIST:
        raise ValueError("Units is incorectly defined")
    call = f"{URL}q={city}&appid={API}&units={units}&lang={lang}"
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
    match int(prompt):
        case 2:
            return input("Enter your city: ")
        case 1:
            return geocoder.ip("me").city
        case _:
            raise ValueError("Prompt is incorectly defined")

def check_response(response)-> None:
    if not all(key in response for key in REQUIRED_KEYS):
        raise ValueError("Invalid response")
def main():
    try:
        city = get_city_input(input("Retrieve city automatically or enter manually (Write 1 or 2): "))
        units = input("Enter your units (standard, metric or imperial): ")
        response = get_response(city, units)
        print_info(response)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()