from pathlib import Path
from typing import Dict, List
import json


#Répertoire des données
DATA_DIR = Path(__file__).resolve().parent.parent / 'data'

def celsius_to_fahrenheit(celsius: float) -> Dict[str, float]:
    """
    Converts a temperature from Celsius to Fahrenheit.
    Args:
        celsius (float): Temperature in Celsius.
    Returns:
        dict: A dictionary containing the temperature in both Celsius and Fahrenheit.
    """
    fahrenheit = (celsius * 9 / 5) + 32
    return {
        "Celsius": celsius,
        "Fahrenheit": fahrenheit
    }

def fahrenheit_to_celsius(fahrenheit: float) -> Dict[str, float]:
    """
    Converts a temperature from Fahrenheit to Celsius.
    Args:
        fahrenheit (float): Temperature in Fahrenheit.
    Returns:
        dict: A dictionary containing the temperature in both Fahrenheit and Celsius.
    """
    celsius = (fahrenheit - 32) * 5 / 9
    return {
        "Fahrenheit": fahrenheit,
        "Celsius": celsius
    }


def convert_city_temp(filename: str) -> Dict[str, List[Dict[str, float]]]:
    """
    Converts the temperatures of each city to the opposite unit.
    Args:
        filename (str): Path to the JSON file containing the temperatures in the /data directory.
    Returns:
        dict: Original and converted temperatures for each city.
    """
    file_path = DATA_DIR / filename
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            city_data = json.load(file)
    except FileNotFoundError:
        return {"error": f"Le fichier {filename} est introuvable.", "chemin": f"{file_path}"}
    except json.JSONDecodeError:
        return {"error": f"Le fichier {filename} est mal formé."}
 
    result = {}
    for city, info in city_data.items():
        scale = info.get('scale')
        values = info.get('values', [])
        
        if scale not in ['celsius', 'fahrenheit']:
            result[city] = {"error": f"Unité de température inconnue: {scale}"}
            continue
        
        converted_list = []
        for val in values:
            if scale == 'celsius':
                converted = celsius_to_fahrenheit(val)
            elif scale == 'fahrenheit':
                converted = fahrenheit_to_celsius(val)
            converted_list.append(converted)
        result[city] = converted_list
    return result 
