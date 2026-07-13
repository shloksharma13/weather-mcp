from mcp.server.fastmcp import FastMCP

from shared.config import MCPConfig
from server.tools import register_tools


def create_server():

    server = FastMCP(

        MCPConfig.SERVER_NAME,

    )

    register_tools(server)

    return server


def main():

    server = create_server()

    server.run(transport="stdio")


if __name__ == "__main__":

    main()