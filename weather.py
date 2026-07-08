from typing import Any

import httpx
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("weather")

GEOCODE_API = "https://nominatim.openstreetmap.org/search"
WEATHER_API = "https://api.open-meteo.com/v1/forecast"

USER_AGENT = "weather-mcp/1.0"


async def make_request(url: str, params: dict | None = None) -> Any:
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "application/geo+json",
    }

    async with httpx.AsyncClient(timeout=20.0) as client:
        response = await client.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()


@mcp.tool()
async def get_coordinates(city: str) -> dict:
    """
    Convert a city name into latitude and longitude.

    Use this before get_forecast when the user provides
    a city instead of coordinates.
    """

    try:
        data = await make_request(
            GEOCODE_API,
            {
                "q": city,
                "format": "json",
                "limit": 1,
            },
        )

        if not data:
            return {
                "success": False,
                "error": f"Could not find '{city}'."
            }

        location = data[0]

        return {
            "success": True,
            "city": location["display_name"],
            "latitude": float(location["lat"]),
            "longitude": float(location["lon"]),
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }


@mcp.tool()
async def get_forecast(latitude: float, longitude: float) -> dict:
    """
    Get the current weather and 7-day forecast for any location worldwide.
    """

    try:
        data = await make_request(
            WEATHER_API,
            {
                "latitude": latitude,
                "longitude": longitude,
                "current": (
                    "temperature_2m,"
                    "relative_humidity_2m,"
                    "wind_speed_10m,"
                    "weather_code"
                ),
                "daily": (
                    "temperature_2m_max,"
                    "temperature_2m_min,"
                    "precipitation_probability_max"
                ),
                "timezone": "auto",
                "forecast_days": 7,
            },
        )

        return {
            "success": True,
            "current": data["current"],
            "daily": data["daily"],
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }

# @mcp.tool()
# async def get_alerts(state: str) -> dict:
#     """
#     Get active National Weather Service alerts for a US state.

#     Example:
#     CA
#     TX
#     NY
#     """

#     try:
#         url = f"{NWS_API}/alerts/active/area/{state.upper()}"

#         alerts = await make_request(url)

#         features = alerts["features"]

#         if not features:
#             return {
#                 "success": True,
#                 "state": state.upper(),
#                 "alerts": [],
#                 "message": "No active alerts."
#             }

#         return {
#             "success": True,
#             "state": state.upper(),
#             "alerts": [
#                 {
#                     "event": feature["properties"]["event"],
#                     "headline": feature["properties"]["headline"],
#                     "severity": feature["properties"]["severity"],
#                     "urgency": feature["properties"]["urgency"],
#                     "description": feature["properties"]["description"],
#                 }
#                 for feature in features
#             ],
#         }

#     except Exception as e:
#         return {
#             "success": False,
#             "error": str(e),
#         }


@mcp.tool(name="my_weather")
async def get_weather(city: str) -> dict:
    """
    Get the weather anywhere in the world.
    """

    coordinates = await get_coordinates(city)

    if not coordinates["success"]:
        return coordinates

    weather = await get_forecast(
        coordinates["latitude"],
        coordinates["longitude"]
    )

    if not weather["success"]:
        return weather

    return {
        "success": True,
        "location": coordinates["city"],
        "latitude": coordinates["latitude"],
        "longitude": coordinates["longitude"],
        "weather": weather,
    }   

if __name__ == "__main__":
    mcp.run(transport="stdio")