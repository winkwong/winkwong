import requests
import re
import os

USERNAME = "winkwong"
# Fetch public repos sorted by creation date (newest first)
url = f"https://api.github.com/users/{USERNAME}/repos?per_page=100&sort=created&direction=desc"
response = requests.get(url)
repos = response.json()

# Filter for repos that end with '-Mod'
mod_repos = [repo for repo in repos if repo['name'].endswith('-Mod')]

# Generate the Markdown string
markdown_content = ""
for repo in mod_repos:
    name = repo['name']
    repo_url = repo['html_url']
    badge_url = f"https://badgen.net/github/assets-dl/{USERNAME}/{name}?label=DOWNLOADS"
    
    markdown_content += f"### [{name}]({repo_url}) [![{name} Downloads]({badge_url})]({repo_url})\n\n"

# Read the current README
with open("README.md", "r") as file:
    readme = file.read()

# Replace the content between the markers
pattern = r"(<!-- VENGE_MODS_START -->\n).*?(\n<!-- VENGE_MODS_END -->)"
new_readme = re.sub(pattern, rf"\g<1>{markdown_content}\g<2>", readme, flags=re.DOTALL)

# Write the updated README
with open("README.md", "w") as file:
    file.write(new_readme)

print("README.md updated successfully with newest mods first!")
