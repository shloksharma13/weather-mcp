import asyncio
import json

from client.mcp_client import mcp_client
from client.ollama_client import ollama


SYSTEM_PROMPT = """
You are a helpful weather assistant.

You have access to three external tools.

1. get_current_weather(city)
2. get_weather_forecast(city)
3. get_air_quality(city)

IMPORTANT

If the user asks for

-current weather
-temperature
-weather
-rain
-forecast
-air quality
-pollution
-AQI

DO NOT answer from memory.

Instead reply ONLY with JSON.

Examples:

{"tool":"get_current_weather","city":"Detroit"}

{"tool":"get_weather_forecast","city":"London"}

{"tool":"get_air_quality","city":"Delhi"}

If no tool is required, answer normally.
"""


async def ask_llm(messages):

    return await ollama.chat(messages)


async def main():

    print("=" * 60)
    print("Weather MCP Chat")
    print("=" * 60)

    history = [

        {
            "role": "system",
            "content": SYSTEM_PROMPT,
        }

    ]

    while True:

        question = input("\nYou : ")

        if question.lower() == "exit":
            break

        history.append(

            {
                "role": "user",
                "content": question,
            }

        )

        response = await ask_llm(history)

        assistant = response["message"]["content"]

        #
        # Try parsing JSON
        #

        try:

            tool_request = json.loads(assistant)

            tool = tool_request["tool"]

            city = tool_request["city"]

            print(f"\nCalling MCP Tool : {tool}({city})")

            result = await mcp_client.call_tool(

                tool,

                {

                    "city": city

                }

            )

            history.append(

                {

                    "role": "assistant",

                    "content": assistant

                }

            )

            history.append(

                {

                    "role": "user",

                    "content":
f"""Tool Result:

{json.dumps(result, indent=2)}

Using ONLY the above data,
answer the user's question naturally.
"""

                }

            )

            final = await ask_llm(history)

            answer = final["message"]["content"]

            print("\nAssistant :", answer)

            history.append(

                {

                    "role": "assistant",

                    "content": answer

                }

            )

        except Exception:

            #
            # No JSON
            #

            print("\nAssistant :", assistant)

            history.append(

                {

                    "role": "assistant",

                    "content": assistant

                }

            )


if __name__ == "__main__":

    asyncio.run(main())