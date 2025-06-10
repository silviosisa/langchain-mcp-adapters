import asyncio
from dotenv import load_dotenv
import os
# from langchain_core.messages import HumanMessage
# from langchain_mcp_adapters.tools import load_mcp_tools
# from langchain_openai import ChatOpenAI
# from langgraph.prebuilt import create_react_agent
# from mcp import ClientSession, StdioServerParameters
# from mcp.client.stdio import stdio_client

load_dotenv()
print(os.getenv("OPENAI_API_KEY"))


async def main():
    print("Hello from mcp-crash-course!")


if __name__ == "__main__":
    asyncio.run(main())
