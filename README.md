# Weather Report

This program is a weather information tool that retrieves and displays (via matplotlib library) weather data for a specified city using the OpenWeatherMap API. 

## Video Demo

https://youtu.be/lCuyh47ohYQ



## Installation

Install my-project with npm

```bash
    npm install my-project
    cd my-project
```  
Install dependencies
```
    pip install -r requirements.txt
```
Usage
```
    python project.py
    Retrieve address automatically or enter manually (Write 1 or 2):
```
Enter "1" or "2". If you written "2", you will need to type city of choice. Case doesn't matter 
```
    Enter your units (standard, metric or imperial): 
```
Enter "standard", "metric" or "imperial". Case doesn't matter.

Example of a possible result
```
City: London (GB)
Description: scattered clouds
Temperature: 22.53-25.97 (23.91)
Feels like: 24.45
Humidity: 80
Visibility: 10000
Wind: speed: 3.09, degree: 240
```
## Running Tests

To run tests, run the following command

```bash
  pytest test_project.py
```


## Function explanation

#### get_response() performs the following tasks:

1. Checks whether the units parameter is specified correctly. If the value is invalid, a ValueError is thrown.
2. Generates a URL request to the OpenWeatherMap API taking into account the passed parameters.
3. Makes a request to the API and receives a response in JSON format.
4. Checks the response code (response["cod"]). If the city is not found (code 404 or 400), a ValueError is thrown.
5. Returns the API response.

#### print_info() performs the following tasks:
1. Checks the validity of the response using the check_response function.
2. Displays the city name and country code.
3. Displays a description of the current weather.
4. Displays the temperature range and current temperature.
5. Displays the perceived temperature.
6. Removes moisture.
7. Displays visibility.
8. Displays wind speed and direction.

#### get_city_input() performs the following tasks:
1. Checks that the prompt parameter is not None.
2. Depending on the prompt value:
- If prompt is 2, prompts the user to enter a city.
- If prompt is 1, automatically determines the city based on the user's IP address.
- In other cases, it throws a ValueError.

#### get_city_input() performs the following tasks:
This function checks if the API response contains all the required keys:

1. Checks that all keys from the required_keys list are present in the response.
2. If at least one key is missing, it throws a ValueError.

#### visualize_weather() visualizes temperature data as a histogram:
1. Checks the validity of the response using the check_response().
2. Extracts temperature values ​​from the response.
3. Generates a list of labels for temperatures.
4. Adapts temperatures for easy display on a graph.
5. Creates a histogram using the matplotlib library.
6. Sets the title and axis labels.
7. Displays temperature values ​​on a graph.
8. Shows a graph.

#### main() visualizes temperature data as a histogram:
1. Prompts the user to determine the city (automatically or manually).
2. Prompts the user for temperature units.
3. Retrieves the API response using the get_response function.
4. Prints weather information using the print_info function.
5. Visualizes temperature data using the visualize_weather function.
6. Processes and displays possible errors.
