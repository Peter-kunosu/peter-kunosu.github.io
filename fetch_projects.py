#!/usr/bin/env python3
"""Fetch recent public, non-fork GitHub repositories at build time."""
import json
import os
from pathlib import Path
from urllib.request import Request, urlopen

USER = "peter-kunosu"
url = f"https://api.github.com/users/{USER}/repos?sort=updated&direction=desc&per_page=100&type=owner"
headers = {"Accept": "application/vnd.github+json", "User-Agent": "hugo-portfolio-build", "X-GitHub-Api-Version": "2022-11-28"}
if os.environ.get("GH_TOKEN"):
    headers["Authorization"] = f"Bearer {os.environ['GH_TOKEN']}"
with urlopen(Request(url, headers=headers), timeout=25) as response:
    repos = json.load(response)
if not isinstance(repos, list):
    raise RuntimeError("GitHub returned an unexpected response")
projects = [
    {key: repo.get(key) for key in ("name", "description", "html_url", "language", "stargazers_count", "updated_at")}
    for repo in repos if not repo.get("fork") and not repo.get("archived") and repo.get("name") != f"{USER}.github.io"
][:8]
path = Path("data/github.json")
path.parent.mkdir(parents=True, exist_ok=True)
path.write_text(json.dumps({"projects": projects}, indent=2), encoding="utf-8")
print(f"Loaded {len(projects)} repositories for {USER}")
