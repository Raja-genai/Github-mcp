from fastmcp import FastMCP
from .github_client import HEADERS, BASE_URL
import requests
mcp = FastMCP()

@mcp.tool()
def list_repositories():
    '''Returns all repositories of authenticated GitHUB user'''

    responce = requests.get(
        f"{BASE_URL}/user/repos",
        headers = HEADERS
    )
    if responce.status_code !=200:
        return f"Error : {responce.status_code}"
    repos = []

    for repo in responce.json():

        repos.append({
            "name": repo["name"],
            "url": repo["html_url"],
            "visibility": "Private" if repo["private"] else "Public"
        })

    return repos


@mcp.tool()
def list_issues(owner:str, repo:str):
    '''Returns all the issues of the user repository'''

    responce =requests.get(
        f"{BASE_URL}/repos/{owner}/{repo}/issues",
        headers = HEADERS
    )
    if responce.status_code != 200:
        return f"Error:{responce.status_code}"
    
    issues =[]
    for issue in responce.json():
        if "pull_request" in issue:
            continue

        issues.append({
            "id" :issue["id"],
            "state":issue["state"],
            "title":issue["title"],
            "body":issue["body"],
            "url":issue["html_url"]
        })
    
    return issues
