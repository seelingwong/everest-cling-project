# main.py
import json
from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("People Matcher")


@mcp.tool()
async def get_profile(email: str) -> str:
    """Find profiles by email."""
    path = "all_profiles.json"  # Modify fullpath of the JSON file
    with open(path, "r", encoding="utf-8") as json_file:
        profiles = json.load(json_file)
    for profile in profiles:
        if profile["owner"] == email:
            return profile
    return "Profile not found."


if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')
