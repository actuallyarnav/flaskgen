import os, venv, subprocess, glob,urllib.request, json

# HELPER FUNCTIONS
#write file
def write_file(project_dir, path, content):
    fullpath = os.path.join(project_dir, path)
    with open(fullpath, "w") as f:
        f.write(content)
    print(f"Created {path}")

#get latest bootstrap release using github api
def get_latest_bootstrap_release():
    api_url = "https://api.github.com/repos/twbs/bootstrap/releases/latest"

    with urllib.request.urlopen(api_url) as response:
        data = json.load(response)

    for asset in data["assets"]:
        if "dist.zip" in asset["name"]:
            return asset["browser_download_url"]

    return None

#download bootstrap from github releases
def get_bootstrap(PROJECT_DIR):
    url = get_latest_bootstrap_release()
    if url:
        subprocess.run(["wget", "--directory-prefix",PROJECT_DIR, url])
    else:
        print("ERROR: could not find Bootstrap release")
    bootstrap_zip = glob.glob(os.path.join(PROJECT_DIR, "bootstrap-*.zip"))[0]
    
    subprocess.run(["unzip", "-d", PROJECT_DIR, bootstrap_zip])
    bootstrap_folder = glob.glob(os.path.join(PROJECT_DIR, "bootstrap-*-dist"))[0]
    
    subprocess.run(["mv", os.path.join(bootstrap_folder, "css"), os.path.join(PROJECT_DIR, "static")])
    subprocess.run(["mv", os.path.join(bootstrap_folder, "js"), os.path.join(PROJECT_DIR, "static")])

    print("Cleaning up...")
    subprocess.run(["rm", bootstrap_zip])
    subprocess.run(["rmdir", bootstrap_folder])
