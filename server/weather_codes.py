WEATHER_CODES = {

    0: "Clear Sky",

    1: "Mainly Clear",

    2: "Partly Cloudy",

    3: "Overcast",

    45: "Fog",

    48: "Depositing Rime Fog",

    51: "Light Drizzle",

    53: "Moderate Drizzle",

    55: "Dense Drizzle",

    56: "Light Freezing Drizzle",

    57: "Dense Freezing Drizzle",

    61: "Slight Rain",

    63: "Moderate Rain",

    65: "Heavy Rain",

    66: "Light Freezing Rain",

    67: "Heavy Freezing Rain",

    71: "Slight Snow",

    73: "Moderate Snow",

    75: "Heavy Snow",

    77: "Snow Grains",

    80: "Rain Showers",

    81: "Moderate Rain Showers",

    82: "Violent Rain Showers",

    85: "Snow Showers",

    86: "Heavy Snow Showers",

    95: "Thunderstorm",

    96: "Thunderstorm With Small Hail",

    99: "Thunderstorm With Heavy Hail",
}


def weather_description(code: int) -> str:
    return WEATHER_CODES.get(code, "Unknown")