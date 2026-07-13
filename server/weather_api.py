from typing import Any

import httpx

from shared.config import APIConfig, WeatherConfig
from shared.models import Coordinates
from server.weather_codes import weather_description


class WeatherAPI:

    def __init__(self):

        self.headers = {
            "User-Agent": APIConfig.USER_AGENT
        }

    async def request(
        self,
        url: str,
        params: dict | None = None
    ) -> dict[str, Any]:

        async with httpx.AsyncClient(timeout=30) as client:

            response = await client.get(
                url,
                params=params,
                headers=self.headers,
            )

            response.raise_for_status()

            return response.json()

    async def coordinates(
        self,
        city: str
    ) -> Coordinates:

        data = await self.request(

            APIConfig.GEOCODING,

            {
                "q": city,
                "format": "json",
                "limit": 1
            }
        )

        if not data:
            raise ValueError(f"City '{city}' not found.")

        result = data[0]

        return Coordinates(

            city=result["display_name"],

            latitude=float(result["lat"]),

            longitude=float(result["lon"])
        )

    async def current_weather(
        self,
        city: str
    ):

        location = await self.coordinates(city)

        weather = await self.request(

            APIConfig.OPEN_METEO,

            {
                "latitude": location.latitude,

                "longitude": location.longitude,

                "current": ",".join(
                    WeatherConfig.CURRENT_FIELDS
                )
            }
        )

        current = weather["current"]

        return {

            "city": location.city,

            "temperature": current["temperature_2m"],

            "humidity": current["relative_humidity_2m"],

            "apparent_temperature":
                current["apparent_temperature"],

            "precipitation":
                current["precipitation"],

            "wind_speed":
                current["wind_speed_10m"],

            "weather_code":
                current["weather_code"],

            "description":
                weather_description(
                    current["weather_code"]
                ),

            "is_day":
                current["is_day"]
        }

    async def forecast(
        self,
        city: str
    ):

        location = await self.coordinates(city)

        weather = await self.request(

            APIConfig.OPEN_METEO,

            {

                "latitude": location.latitude,

                "longitude": location.longitude,

                "forecast_days":
                    WeatherConfig.FORECAST_DAYS,

                "daily":
                    ",".join(
                        WeatherConfig.DAILY_FIELDS
                    )
            }
        )

        daily = weather["daily"]

        result = []

        for i in range(len(daily["time"])):

            result.append({

                "date":
                    daily["time"][i],

                "max_temperature":
                    daily["temperature_2m_max"][i],

                "min_temperature":
                    daily["temperature_2m_min"][i],

                "wind_speed":
                    daily["wind_speed_10m_max"][i],

                "precipitation":
                    daily["precipitation_sum"][i],

                "sunrise":
                    daily["sunrise"][i],

                "sunset":
                    daily["sunset"][i],

                "weather_code":
                    daily["weather_code"][i],

                "description":
                    weather_description(
                        daily["weather_code"][i]
                    )
            })

        return {

            "city": location.city,

            "forecast": result
        }
    
    async def air_quality(self, city: str):
        location = await self.coordinates(city)

        data = await self.request(

            APIConfig.AIR_QUALITY,

            {
                "latitude": location.latitude,

                "longitude": location.longitude,

                "current": ",".join([
                    "european_aqi",
                    "pm10",
                    "pm2_5",
                    "carbon_monoxide",
                    "nitrogen_dioxide",
                    "ozone"
                ])
            }
        )

        current = data["current"]

        return {

            "city": location.city,

            "aqi":
                current.get("european_aqi"),

            "pm10":
                current.get("pm10"),

            "pm2_5":
                current.get("pm2_5"),

            "carbon_monoxide":
                current.get("carbon_monoxide"),

            "nitrogen_dioxide":
                current.get("nitrogen_dioxide"),

            "ozone":
                current.get("ozone")
        }


weather_api = WeatherAPI()