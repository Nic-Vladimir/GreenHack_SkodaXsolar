import requests
import json
from keys import API_KEY


def get_distance(client_address, provider_address):
    distance = "get_distance - API_ERROR :("
    # Construct the API request URL
    url = "https://maps.googleapis.com/maps/api/distancematrix/json"
    params = {
        "origins": provider_address,
        "destinations": client_address,
        "units": "metric",
        "key": API_KEY
    }

    # Make the HTTP request
    response = requests.get(url, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        distance = data['rows'][0]['elements'][0]['distance']['value']

    return (distance)



def get_coordinates(address):
    coordinates = {"lat": "ERROR_LAT", "lng": "ERROR_LNG"}
    # Construct the API request URL
    url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {
        "address": address,
        "key": API_KEY
    }

    # Make the HTTP GET request
    response = requests.get(base_url, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        coordinates = data['results'][0]['geometry']['location']

    return (coordinates)


def get_solar_data(coordinates):
    url = "https://solar.googleapis.com/v1/buildingInsights:findClosest"
    params = {
        "location.latitude": coordinates["lat"],
        "location.longitude": coordinates["lng"],
        "requiredQuality": 'HIGH',
        "key": API_KEY
    }

    response = requests.get(url, params=params)

    # Check for successful response
    if response.status_code == 200:
        data = response.json()

    else:
        print(f"Error: API request failed with status code {response.status_code}")

    solar = {
        "max_panels": data["solarPotential"]["maxArrayPanelsCount"]
        "max_panels_area" = data["solarPotential"]["maxArrayAreaMeters2"]
        "carbon_offset_factor_kgpermwh" = data["solarPotential"]["carbonOffsetFactorKgPerMwh"]
        "roof_area" = data["solarPotential"]["wholeRoofStats"]["areaMeters2"]
        "panel_capacity_watts" = data["solarPotential"]["panelCapacityWatts"]
        "one_panel_area" = data["solarPotential"]["panelHeightMeters"] * data["solarPotential"]["panelWidthMeters"]
        "panel_lifetime" = data["solarPotential"]["panelLifetimeYears"]
    }

    return (solar)



   #https://maps.googleapis.com/maps/api/distancematrix/json?destinations="Weilova 1505, 102 00 Praha 15-Hostivař"&origins="Kongresové centrum Praha, vchod 6, 5. května 1640/65, Nusle, 140 21 Praha 4"&units=metric&key=AIzaSyBIiXcNl2xidDq-YP2t0ZhJ6_QHpzeH-U0

#https://maps.googleapis.com/maps/api/geocode/json?address=Praha Kolbenova 9&key=AIzaSyBIiXcNl2xidDq-YP2t0ZhJ6_QHpzeH-U0

https://solar.googleapis.com/v1/buildingInsights:findClosest?location.latitude=37.4450&location.longitude=-122.1390&requiredQuality=HIGH&key=YOUR_API_KEY

"
