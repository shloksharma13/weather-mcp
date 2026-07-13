from pydantic import BaseModel


class Coordinates(BaseModel):
    city: str
    latitude: float
    longitude: float


class CurrentWeather(BaseModel):
    city: str
    temperature: float
    humidity: int
    apparent_temperature: float
    precipitation: float
    wind_speed: float
    weather_code: int
    is_day: int
    description: str


class ForecastDay(BaseModel):
    date: str
    max_temperature: float
    min_temperature: float
    wind_speed: float
    precipitation: float
    weather_code: int
    description: str


class Forecast(BaseModel):
    city: str
    forecast: list[ForecastDay]


class AirQuality(BaseModel):
    city: str
    aqi: float
    pm10: float
    pm2_5: float
    carbon_monoxide: float
    nitrogen_dioxide: float
    ozone: float


class APIError(BaseModel):
    success: bool = False
    error: str