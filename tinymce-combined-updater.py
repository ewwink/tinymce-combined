# -*- coding: utf-8 -*-
"""
TinyMCE and Plugins Combined into one js file
https://github.com/ewwink/tinymce-combined
"""
import os, requests, json
from packaging.version import Version

def set_github_env_var(name, value):
    env_file = os.getenv("GITHUB_ENV")
    with open(env_file, "a") as f:
        f.write(f"{name}={value}\n")

standard_js_files = [
    "/tinymce.min.js",
    "/themes/silver/theme.min.js",
    "/models/dom/model.min.js",
    "/icons/default/icons.min.js",
    "/plugins/advlist/plugin.min.js",
    "/plugins/autolink/plugin.min.js",
    "/plugins/lists/plugin.min.js",
    "/plugins/link/plugin.min.js",
    "/plugins/image/plugin.min.js",
    "/plugins/charmap/plugin.min.js",
    "/plugins/preview/plugin.min.js",
    "/plugins/anchor/plugin.min.js",
    "/plugins/searchreplace/plugin.min.js",
    "/plugins/visualblocks/plugin.min.js",
    "/plugins/code/plugin.min.js",
    "/plugins/fullscreen/plugin.min.js",
    "/plugins/media/plugin.min.js",
    "/plugins/table/plugin.min.js",
    "/plugins/wordcount/plugin.min.js",
]

standard_css_files = [
    "/skins/ui/oxide/skin.min.css",
    "/skins/ui/oxide/content.min.css",
    "/skins/content/default/content.min.css",
]

full_js_file = []
full_css_file = []

base_url = "https://cdn.jsdelivr.net/npm/tinymce@"
version_url = "https://cdn.jsdelivr.net/npm/tinymce@latest/package.json"

os.makedirs("dist/skins/ui/oxide", exist_ok=True)
os.makedirs("dist/skins/content/default", exist_ok=True)

with open("version.txt", "r") as f:
    github_version = f.read()
    print(f"TinyMCE Github version: {github_version}")

content = requests.get(version_url, timeout=10)
tinymce_info = json.loads(content.text)
jsdelivr_version = tinymce_info["version"]
print(f"TinyMCE Jsdelivr version: {jsdelivr_version}")

if Version(jsdelivr_version) > Version(github_version):
    set_github_env_var("tinymce_version", jsdelivr_version)
    set_github_env_var("tinymce_new_version", "true")
    print(f"Updating TinyMCE...")
    js_list = []
    for path in standard_js_files:
        url = f"{base_url}{jsdelivr_version}{path}"
        print(f"Dowloading {url}..")
        js_content = requests.get(url).text
        js_list.append(js_content.strip())

    with open("dist/tinymce-combined-standard.min.js", "w", encoding="UTF-8") as f:
        js_combined = "\n\n".join(js_list)
        f.write(js_combined)

    for path in standard_css_files:
        url = url = f"{base_url}{jsdelivr_version}{path}"
        print(f"Dowloading {url}..")
        css_content = requests.get(url).text
        with open("dist" + path, "w", encoding="UTF-8") as f:
            f.write(css_content)

    with open("version.txt", "w", encoding="UTF-8") as f:
        f.write(jsdelivr_version)

    with open("README.md", "r") as f:
        readme = f.read()
        readme = readme.replace(github_version, jsdelivr_version)

    with open("README.md", "w") as f:
        f.write(readme)

    print(f"TinyMCE Updated.")
else:
    set_github_env_var("tinymce_new_version", "false")
    print(f"TinyMCE up to date.")
