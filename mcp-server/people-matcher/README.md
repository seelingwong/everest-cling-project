# People Matcher

This project is the MCP server for people matcher. 

## Setup to Claude Desktop
1. Download all_profiles.json from rd_people_matcher project. And place local folder.
2. Modify main.py line 12 to location of the all_profiles.json.
3. Install main.py to claude desktop
```sh
mcp install main.py
```

4. Open Claude Desktop to verify the result.

## Example Prompt
I am looking for someone with expertise in C# ASP.NET Core API development, Entity Framework Core, Azure Portal/CLI, and resource management. Familiarity with Azure DevOps and experience in payment integration, specifically with Stripe, are essential. Additional experience with Lua and the medical industry would be highly beneficial. Looking for someone with a skillset or interest in these areas.

List of profile:
milin.paul@everest.engineering
muhammad.amir@everest.engineering
yogesh.mongar@everest.engineering
paul.davies@everest.engineering
chris.jones@everest.engineering


## Troubleshooting
**spawn uv enoent:**
Cause by the Claude Desktop setting cannot call uv command, open the setting and make sure command uv is using fullpath.


## Next/Pending Tasks
1. Update profile from local file to database.
2. Add prompt so that can use prompt from rd_people_matcher.
3. More error handling.
4. Create custom client.