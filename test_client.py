import asyncio

from client.mcp_client import mcp_client


async def main():

    tools = await mcp_client.list_tools()

    for tool in tools:
        print(tool.name)


asyncio.run(main())