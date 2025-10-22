# MCP weather bot

An intelligent Weather Information Bot built using FastMCP, a Python framework that implements the Model Context Protocol (MCP) — enabling AI models and external tools to communicate in a standardized, secure way.

# What is MCP?

MCP (Model Context Protocol) is an open standard introduced by Anthropic that allows AI models (like Claude or ChatGPT) to connect to external data, APIs, and tools in a structured and safe manner.


FastMCP provides a developer-friendly Python implementation of this protocol, making it easy to build your own MCP-compatible servers and clients.

# What This Project Does

The MCP Weather Bot is a simple MCP server that exposes weather-related tools to clients or AI systems.
It demonstrates how LLMs or automation clients can dynamically fetch real-time weather data through MCP.

# How to Run It
Clone the repository
```
git clone https://github.com/jazz-min/mcp-weather-bot.git
cd mcp-weather-bot
```

# Install dependencies
```pip install -r requirements.txt```

# Start the MCP Weather Server
```python weather_server.py```
This will start the MCP server on your local machine, listening for incoming requests.

# Interact with the MCP Weather Server
You can use the provided `weather_client.py` script to interact with the server.
```python weather_client.py```
This client connects to the MCP server and requests weather information for a specified location.