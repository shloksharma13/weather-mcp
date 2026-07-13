from __future__ import annotations

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


class MCPClient:

    def __init__(self):

        self.server = StdioServerParameters(
            command="python",
            args=["-m", "server.weather"],
        )

    async def list_tools(self):
        """
        Return all tools exposed by the MCP server.
        """

        async with stdio_client(self.server) as (read, write):

            async with ClientSession(read, write) as session:

                await session.initialize()

                result = await session.list_tools()

                return result.tools

    async def call_tool(
        self,
        tool_name: str,
        arguments: dict,
    ):
        """
        Execute an MCP tool.
        """

        async with stdio_client(self.server) as (read, write):

            async with ClientSession(read, write) as session:

                await session.initialize()

                result = await session.call_tool(
                    tool_name,
                    arguments=arguments,
                )

                # Structured JSON if available
                if getattr(result, "structuredContent", None):
                    return result.structuredContent

                if getattr(result, "structured_content", None):
                    return result.structured_content

                # Otherwise extract text blocks
                output = []

                for item in result.content:

                    if hasattr(item, "text"):

                        output.append(item.text)

                return "\n".join(output)


mcp_client = MCPClient()