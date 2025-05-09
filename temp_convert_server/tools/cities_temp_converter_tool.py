from server import mcp
from typing import Dict, List
from utils.temperature_converter import convert_city_temp
 
@mcp.tool()
def convert_city_temperatures(filename: str) -> Dict[str, List[Dict[str, float]]]:
    """
    Converts the temperatures of each city to the other unit (Celsius ↔ Fahrenheit).
    Args:
        filename (str): Name of the JSON file located in the /data folder (e.g.: temperatures.json).
    Returns:
        Dict[str, List[Dict[str, float]]]: Original and converted temperatures for each city.
    """
    return convert_city_temp(filename)
