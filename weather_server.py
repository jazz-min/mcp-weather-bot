import requests
from fastmcp import FastMCP

mcp = FastMCP("Weather Server")


@mcp.tool
def get_weather(city: str) -> dict:
    """Returns weather report for the given location using wttr.in API."""
    url = f"https://wttr.in/{city}?format=j1"
    data = requests.get(url).json()
    return {
        "location": city,
        "temperature_C": data["current_condition"][0]["temp_C"],
        "weather_desc": data["current_condition"][0]["weatherDesc"][0]["value"]
    }


if __name__ == "__main__":
    mcp.run()