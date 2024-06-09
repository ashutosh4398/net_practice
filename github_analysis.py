import time

import pandas as pd
import requests
import yaml

# Constants
GITHUB_API_URL = "https://api.github.com"
TOKEN = "<github key>"  # Replace with your GitHub token

# Headers for authentication
headers = {
    "Authorization": f"token {TOKEN}",
    "Accept": "application/vnd.github.v3+json",
}

class RateLimitError(Exception):
    pass


def retry(default_value):
    def outer(func):
        def inner(*args, **kwargs):
            try:
                resp = func(*args, **kwargs)
                return resp
            except RateLimitError:
                time.sleep(1*60*60)
                return default_value
        return inner
    return outer

@retry(default_value=[])
def fetch_github_languages():
    url = "https://raw.githubusercontent.com/github/linguist/master/lib/linguist/languages.yml"
    response = requests.get(url)
    if response.status_code == 200:
        languages = yaml.safe_load(response.content)
        return list(languages.keys())
    elif "API rate limit exceeded for user".lower() in response.text.lower():
        raise RateLimitError("Rate limit triggered!!!")
    else:
        raise Exception("Failed to fetch languages")

@retry(default_value=[])
def get_trending_repositories(language="Python", since="monthly"):
    """Fetches repositories trending in a given language and time period."""
    query_url = f"{GITHUB_API_URL}/search/repositories?q=language:{language}&sort=stars&order=desc"
    response = requests.get(query_url, headers=headers)
    if response.status_code == 200:
        """
        ['id', 'node_id', 'name', 'full_name', 'private', 'owner', 'html_url', 'description', 'fork', 'url', 'forks_url', 'keys_url', 'collaborators_url', 'teams_url', 'hooks_url', 'issue_events_url', 'events_url', 'assignees_url', 'branches_url', 'tags_url', 'blobs_url', 'git_tags_url', 'git_refs_url', 'trees_url', 'statuses_url', 'languages_url', 'stargazers_url', 'contributors_url', 'subscribers_url', 'subscription_url', 'commits_url', 'git_commits_url', 'comments_url', 'issue_comment_url', 'contents_url', 'compare_url', 'merges_url', 'archive_url', 'downloads_url', 'issues_url', 'pulls_url', 'milestones_url', 'notifications_url', 'labels_url', 'releases_url', 'deployments_url', 'created_at', 'updated_at', 'pushed_at', 'git_url', 'ssh_url', 'clone_url', 'svn_url', 'homepage', 'size', 'stargazers_count', 'watchers_count', 'language', 'has_issues', 'has_projects', 'has_downloads', 'has_wiki', 'has_pages', 'has_discussions', 'forks_count', 'mirror_url', 'archived', 'disabled', 'open_issues_count', 'license', 'allow_forking', 'is_template', 'web_commit_signoff_required', 'topics', 'visibility', 'forks', 'open_issues', 'watchers', 'default_branch', 'permissions', 'score']
        """
        return [
            {
                "repo_id": repo["id"],
                "repo_name": repo["name"],
                "repo_path": repo["full_name"],
                "forks_count": repo["forks_count"],
                "score": repo["score"],
                "open_issues_count": repo["open_issues_count"],
                "watchers_count": repo["watchers_count"],
                "stars": repo["stargazers_count"],
            }
            for repo in response.json()["items"]
        ]
    elif "API rate limit exceeded for user".lower() in response.text.lower():
        raise RateLimitError("Rate limit triggered!!!")
    else:
        raise Exception("Failed to fetch data:", response.status_code, response.text)

@retry(default_value=[])
def get_collaborators(repo_owner, repo_name):
    """Fetches collaborators for a given repository."""
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/contributors?page=2&access_token=fff"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return [x["login"] for x in response.json()]
    elif "API rate limit exceeded for user".lower() in response.text.lower():
        raise RateLimitError("Rate limit triggered!!!")
    return []

@retry(default_value={
        "user_id": None,
            "name": None,
            "company": None,
            "location": None,
            "followers": None,
    })
def get_user_info(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        """
        'login', 'id', 'node_id', 'avatar_url', 'gravatar_id', 'url',
       'html_url', 'followers_url', 'following_url', 'gists_url',
       'starred_url', 'subscriptions_url', 'organizations_url', 'repos_url',
       'events_url', 'received_events_url', 'type', 'site_admin', 'name',
       'company', 'blog', 'location', 'email', 'hireable', 'bio',
       'twitter_username', 'public_repos', 'public_gists', 'followers',
       'following', 'created_at', 'updated_at'
        """
        d = response.json()
        return {
            "user_id": d["id"],
            "dev_name": d["name"],
            "company": d["company"],
            "location": d["location"],
            "followers": d["followers"],
        }
    elif "API rate limit exceeded for user".lower() in response.text.lower():
        raise RateLimitError("Rate limit triggered!!!")
    return {
        "user_id": None,
            "name": None,
            "company": None,
            "location": None,
            "followers": None,
    }


languages = fetch_github_languages()
data_1 = []
popular_languages = ["Python", "JavaScript"]
languages = [x for x in languages if x in popular_languages]
for lang in languages:
    d = get_trending_repositories(lang)
    data_1.extend(d)

# users data
data_2 = []
for repo in data_1[:5]:
    owner_name, repo_name = repo["full_name"].split("/")
    collab_usernames = get_collaborators(owner_name, repo_name)
    for user_name in collab_usernames:
        user_info = get_user_info(user_name)
        user_info.update({"repo_id": repo["repo_id"]})
        data_2.append(user_info)

# data frames
df1 = pd.DataFrame(data_1)
df2 = pd.DataFrame(data_2)

merged_df = pd.merge(df1, df2, how="outer", on="repo_id")
print(merged_df.head())
