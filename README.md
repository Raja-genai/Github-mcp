# GitHub MCP Server

[![PyPI](https://img.shields.io/pypi/v/raja-github-mcp)](https://pypi.org/project/raja-github-mcp/)
[![Python](https://img.shields.io/pypi/pyversions/raja-github-mcp.svg)](https://pypi.org/project/raja-github-mcp/)
[![License](https://img.shields.io/github/license/Raja-genai/github-mcp)](LICENSE)

An MCP server that provides GitHub repository, issue, branch, and pull request management tools for AI agents and LLM applications.

---

## Installation

Install the package from PyPI:

```bash
pip install raja-github-mcp
```

---

## Usage

### Set your GitHub Personal Access Token

Create a `.env` file:

```env
GITHUB_TOKEN=your_personal_access_token
```

### Start the MCP Server

```bash
github-mcp
```

Or run directly using Python:

```bash
python -m github_mcp.main
```

---

## Available Tools

### Repository Management
- `list_repositories`
- `create_repository`
- `get_repository_details`

### Issue Management
- `list_issues`
- `create_issue`
- `close_issue`
- `reopen_issue`
- `comment_on_issue`

### Branch Management
- `list_branches`
- `create_branch`

### Pull Request Management
- `list_pull_requests`
- `create_pull_request`

---

## Example MCP Inspector Configuration

**Command**
```text
uv
```

**Arguments**
```text
run github-mcp
```

---

## Project Goal

This project aims to provide GitHub management capabilities to AI agents through the Model Context Protocol (MCP) and serves as a building block for autonomous coding agents and Cursor-like systems.
