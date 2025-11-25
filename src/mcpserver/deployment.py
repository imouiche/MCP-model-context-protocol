from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Demo")

@mcp.tool(description="Add two numbers")
def add(a: int, b: int) -> int:
    """ Add two numbers"""

    return a + b