#from github_mcp.tools import mcp   # write this when you are deploying 
from tools import mcp
def main():
    print("Starting GitHub MCP...")
    mcp.run(transport="stdio")
if __name__ == "__main__":
    main()