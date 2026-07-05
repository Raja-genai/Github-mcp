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

@mcp.tool()
def create_issue(owner:str, repo:str, title:str, body:str):
    "This function Creates an issue with title and body in the repository of the owner"
    
    issue={"title":title,"body":body}
    responce = requests.post(
        f"{BASE_URL}/repos/{owner}/{repo}/issues",
        json=issue,
        headers=HEADERS
    )
    if responce.status_code != 201:
        return {
            "status": responce.status_code,
            "error": responce.json()
        }
    return {
        "message": "Issue created successfully",
        "issue_url": responce.json()["html_url"]
    }

@mcp.tool()
def close_issue(owner:str,repo:str,issue_number:int):
    '''This function will close the issue using the issue number'''
    update={"state":"closed"}
    responce = requests.patch(
        f"{BASE_URL}/repos/{owner}/{repo}/issues/{issue_number}",
        json=update,
        headers=HEADERS
    )
    if responce.status_code != 200:
        return {
            "status": responce.status_code,
            "error": responce.json()
        }
    return {
        "message": "Issue closed successfully",
        "issue_url": responce.json()["html_url"]
    }

@mcp.tool()
def reopen_issue(owner:str,repo:str,issue_number:int):
    '''This function will reopen the issue using the issue number'''
    
    
    update={"state":"open"}
    responce = requests.patch(
        f"{BASE_URL}/repos/{owner}/{repo}/issues/{issue_number}",
        json=update,
        headers=HEADERS
    )
    if responce.status_code != 200:
        return {
            "status": responce.status_code,
            "error": responce.json()
        }
    return {
        "message": "Issue reopened successfully",
        "issue_url": responce.json()["html_url"]
    }

@mcp.tool()
def comment_on_issue(owner:str,repo:str,issue_number:int,comment:str):
    '''This function will create a comment on the issue using the issue number'''
    
    
    comment={"body":comment}
    responce = requests.post(
        f"{BASE_URL}/repos/{owner}/{repo}/issues/{issue_number}/comments",
        json=comment,
        headers=HEADERS
    )
    if responce.status_code != 201:
        return {
            "status": responce.status_code,
            "error": responce.json()
        }
    return {
        "message": "Comment added successfully",
        "issue_url": responce.json()["html_url"]
    }


@mcp.tool()
def get_repository_details(owner:str,repo:str):
    '''Returns the details of repository with repository name'''

    responce = requests.get(
        f"{BASE_URL}/repos/{owner}/{repo}",
        headers = HEADERS
    )
    if responce.status_code !=200:
        return {
            "status": responce.status_code,
            "error": responce.json()
        }
    repo_data = responce.json()
    

    

    return{
        "name": repo_data["name"],
        "full_name": repo_data["full_name"],
        "description": repo_data["description"],
        "url": repo_data["html_url"],
        "visibility": "Private" if repo_data["private"] else "Public",
        "default_branch": repo_data["default_branch"],
        "language": repo_data["language"],
        "stars": repo_data["stargazers_count"],
        "forks": repo_data["forks_count"],
        "open_issues": repo_data["open_issues_count"],
        "created_at": repo_data["created_at"],
        "updated_at": repo_data["updated_at"],
        "clone_url": repo_data["clone_url"]
    }

@mcp.tool()
def create_repository(name:str,description:str,private:bool,auto_init:bool):
    '''Use this tool to create a repository'''
   
    responce = requests.post(
        f"{BASE_URL}/user/repos",
        json={"name":name,"description":description,"private":private,"auto_init":auto_init},
        headers = HEADERS
    )
    if responce.status_code!=201:
        return {
            "status": responce.status_code,
            "error": responce.json()
        }
    else:
        return{
            "message":"Repository Created Successfully",
            "issue_url":responce.json()['html_url'],
            "clone_url": responce.json()["clone_url"]
        }
@mcp.tool()
def list_branches(owner: str, repo: str):
    """Returns all branches of a repository."""

    response = requests.get(
        f"{BASE_URL}/repos/{owner}/{repo}/branches",
        headers=HEADERS
    )

    if response.status_code != 200:
        return {
            "status": response.status_code,
            "error": response.json()
        }

    branches = []

    for branch in response.json():
        branches.append({
            "name": branch["name"],
            "protected": branch["protected"]
        })

    return branches

@mcp.tool()
def create_branch(owner: str, repo: str, branch_name: str):
    """Creates a new branch."""

    repo_response = requests.get(
        f"{BASE_URL}/repos/{owner}/{repo}",
        headers=HEADERS
    )

    if repo_response.status_code != 200:
        return {
            "status": repo_response.status_code,
            "error": repo_response.json()
        }

    default_branch = repo_response.json()["default_branch"]

    sha_response = requests.get(
        f"{BASE_URL}/repos/{owner}/{repo}/git/ref/heads/{default_branch}",
        headers=HEADERS
    )

    if sha_response.status_code != 200:
        return {
            "status": sha_response.status_code,
            "error": sha_response.json()
        }

    sha = sha_response.json()["object"]["sha"]

    create_response = requests.post(
        f"{BASE_URL}/repos/{owner}/{repo}/git/refs",
        json={
            "ref": f"refs/heads/{branch_name}",
            "sha": sha
        },
        headers=HEADERS
    )

    if create_response.status_code != 201:
        return {
            "status": create_response.status_code,
            "error": create_response.json()
        }

    return {
        "message": "Branch created successfully",
        "branch": branch_name
    }

@mcp.tool()
def list_pull_requests(owner: str, repo: str):
    """Returns all pull requests."""

    response = requests.get(
        f"{BASE_URL}/repos/{owner}/{repo}/pulls",
        headers=HEADERS
    )

    if response.status_code != 200:
        return {
            "status": response.status_code,
            "error": response.json()
        }

    prs = []

    for pr in response.json():
        prs.append({
            "number": pr["number"],
            "title": pr["title"],
            "state": pr["state"],
            "url": pr["html_url"]
        })

    return prs

@mcp.tool()
def create_pull_request(
    owner: str,
    repo: str,
    title: str,
    body: str,
    head: str,
    base: str
):
    """Creates a pull request."""

    response = requests.post(
        f"{BASE_URL}/repos/{owner}/{repo}/pulls",
        json={
            "title": title,
            "body": body,
            "head": head,
            "base": base
        },
        headers=HEADERS
    )

    if response.status_code != 201:
        return {
            "status": response.status_code,
            "error": response.json()
        }

    return {
        "message": "Pull request created successfully",
        "pr_url": response.json()["html_url"]
    }