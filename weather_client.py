from fastmcp import Client
import asyncio

client = Client("weather_server.py")


async def get_weather_report(city: str):
    async with client:
        weather_report_response = await client.call_tool("get_weather", {"city": city})
        weather_report = weather_report_response.structured_content
        print(f"Weather in {weather_report['location']}:")
        print(f"Temperature: {weather_report['temperature_C']}°C")
        print(f"Description: {weather_report['weather_desc']}")

if __name__ == "__main__":
    city_name = input("Enter city name: ")
    asyncio.run(get_weather_report(city_name))