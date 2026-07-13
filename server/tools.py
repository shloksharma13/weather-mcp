from mcp.server.fastmcp import FastMCP

from server.weather_api import weather_api


def register_tools(mcp: FastMCP):

    @mcp.tool(
        name="get_current_weather",
        description="""
Returns the current weather conditions for any city.

Input:
- city (string)

Returns:
- temperature
- humidity
- apparent temperature
- wind speed
- precipitation
- weather condition
"""
    )
    async def get_current_weather(city: str):

        return await weather_api.current_weather(city)

    @mcp.tool(
        name="get_weather_forecast",
        description="""
Returns a 5-day weather forecast.

Includes:

- Max Temperature
- Min Temperature
- Wind Speed
- Sunrise
- Sunset
- Weather Condition
"""
    )
    async def get_weather_forecast(city: str):

        return await weather_api.forecast(city)

    @mcp.tool(
        name="get_air_quality",
        description="""
Returns current air quality for a city.

Includes:

- AQI
- PM2.5
- PM10
- CO
- NO2
- Ozone
"""
    )
    async def get_air_quality(city: str):

        return await weather_api.air_quality(city)