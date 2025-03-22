# MCP Server

This folder contains a collection of self-created AI tools. Each tool is designed to perform specific tasks related to artificial intelligence and machine learning. Below is a brief description of the tools included in this folder:

## Set up your environment
1. Install uv by following [step](https://github.com/astral-sh/uv)
2. Setup project by using uv.
```sh
# Create a new directory for our project
uv init people-matcher
cd people-matcher

# Create virtual environment and activate it
uv venv
source .venv/bin/activate

# Install dependencies
uv add "mcp[cli]"

# Create our server file
touch main.py
```