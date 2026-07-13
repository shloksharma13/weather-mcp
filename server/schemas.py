CURRENT_WEATHER_INPUT = {
    "type": "object",
    "properties": {
        "city": {
            "type": "string",
            "description": "City name (e.g. Bangalore, London, Tokyo)"
        }
    },
    "required": ["city"]
}


CURRENT_WEATHER_OUTPUT = {
    "type": "object",
    "properties": {
        "city": {"type": "string"},
        "temperature": {"type": "number"},
        "humidity": {"type": "integer"},
        "apparent_temperature": {"type": "number"},
        "wind_speed": {"type": "number"},
        "precipitation": {"type": "number"},
        "weather_code": {"type": "integer"},
        "description": {"type": "string"},
        "is_day": {"type": "integer"}
    }
}


FORECAST_INPUT = {
    "type": "object",
    "properties": {
        "city": {
            "type": "string"
        }
    },
    "required": ["city"]
}


FORECAST_OUTPUT = {
    "type": "object",
    "properties": {
        "city": {
            "type": "string"
        },
        "forecast": {
            "type": "array"
        }
    }
}


AIR_QUALITY_INPUT = {
    "type": "object",
    "properties": {
        "city": {
            "type": "string"
        }
    },
    "required": ["city"]
}


AIR_QUALITY_OUTPUT = {

    "type": "object",

    "properties": {

        "city": {
            "type": "string"
        },
        "aqi": {
            "type": "number"
        },
        "pm10": {
            "type": "number"
        },
        "pm2_5": {
            "type": "number"
        },
        "carbon_monoxide": {
            "type": "number"
        },
        "nitrogen_dioxide": {
            "type": "number"
        },
        "ozone": {
            "type": "number"
        }
    }
}