from dataclasses import dataclass


@dataclass(frozen=True)
class APIConfig:
    OPEN_METEO = "https://api.open-meteo.com/v1/forecast"

    AIR_QUALITY = "https://air-quality-api.open-meteo.com/v1/air-quality"

    GEOCODING = "https://nominatim.openstreetmap.org/search"

    USER_AGENT = "weather-mcp/1.0"


@dataclass(frozen=True)
class WeatherConfig:
    FORECAST_DAYS = 5

    CURRENT_FIELDS = [
        "temperature_2m",
        "relative_humidity_2m",
        "apparent_temperature",
        "precipitation",
        "weather_code",
        "wind_speed_10m",
        "is_day",
    ]

    DAILY_FIELDS = [
        "weather_code",
        "temperature_2m_max",
        "temperature_2m_min",
        "precipitation_sum",
        "wind_speed_10m_max",
        "sunrise",
        "sunset",
    ]


@dataclass(frozen=True)
class OllamaConfig:
    BASE_URL = "http://localhost:11434"

    #MODEL = "llama3:8b"
    MODEL = "mistral:latest"


@dataclass(frozen=True)
class MCPConfig:
    SERVER_NAME = "Weather MCP Server"

    VERSION = "1.0.0"