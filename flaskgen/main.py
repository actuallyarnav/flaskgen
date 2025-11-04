import os, venv, subprocess, glob,urllib.request, json
from templates import *
from commands import *

#MAIN SCRIPT
def main():
    print("Flask App Generator v1.0")

    PROJECT_DIR = input("Enter the project directory (. for current): ").strip()

    os.makedirs(os.path.join(PROJECT_DIR, "static"), exist_ok=True)

    write_file(PROJECT_DIR, "app.py", APP_PY_TEXT)

    IS_LOCAL_BOOTSTRAP = input("Would you like to download Bootstrap locally? (Y/n): ").strip().lower() != 'n'
    if IS_LOCAL_BOOTSTRAP:
        #download bootstrap from the cdn
        get_bootstrap(PROJECT_DIR=PROJECT_DIR)

    #create base.html
    os.makedirs(os.path.join(PROJECT_DIR, "templates"), exist_ok=True)
    print(f"Created {os.path.join(PROJECT_DIR, "templates")}")
    print("Creating base.html...")

    with open(os.path.join(PROJECT_DIR, "templates", "base.html"), "w") as f:
        f.write(BASE_HTML_P1)
        if IS_LOCAL_BOOTSTRAP:
            f.write(BASE_HTML_LOCAL)
        else:
            f.write(BASE_HTML_CDN)
        f.write(BASE_HTML_P2)

    print(f"Created {os.path.join(PROJECT_DIR, "templates/base.html")}")

    #create home.html
    write_file(PROJECT_DIR, "templates/home.html", HOME_HTML)

    #create python venv using given name
    VENV_NAME = input("Enter the name for the Python venv: ").strip()
    venv.create(os.path.join(PROJECT_DIR, VENV_NAME), with_pip=True)
    print("Created Python virtual environment")
    venv_python = os.path.join(PROJECT_DIR, VENV_NAME, "bin", "python")

    #install pip packages in venv
    subprocess.run([venv_python, "-m", "pip", "install", "--upgrade", "pip"])
    subprocess.run([venv_python, "-m", "pip", "install", "flask", "python-dotenv"])

    #create environment variable file
    write_file(PROJECT_DIR, ".env", ENV_TEXT)

    #create gitignore
    write_file(PROJECT_DIR, ".gitignore", GITIGNORE_TEXT)
    
    #create dockerignore
    write_file(PROJECT_DIR, ".dockerignore", DOCKERIGNORE_TEXT)

    #create Dockerfile
    write_file(PROJECT_DIR, "Dockerfile", DOCKERFILE_TEXT)
   
   #create requirements.txt
    result = subprocess.run([venv_python, "-m", "pip", "freeze"], capture_output=True, text=True)
    write_file(PROJECT_DIR, "requirements.txt", result.stdout)

    #create README.md
    write_file(PROJECT_DIR, "README.md", README_TEXT)
    
    #MAKE_GITHUB_ACTIONS = input("Would you like to create .github/workflows/deploy.yml?? (Y/n): ").strip().lower() != 'n'
    #if MAKE_GITHUB_ACTIONS:
        #os.makedirs(os.path.join(PROJECT_DIR, ".github", "workflows"), exist_ok=True)
        #write_file(".github/workflows/deploy.yml", GITHUB_ACTIONS_TEXT)


if __name__ == "__main__":
    main()

#files to generate:
#app.py
#bootstrap (ask user for either cdn link or local download)
#static/css (take bootstrap from cdn)
#static/js (same)
#templates/base.html (basic jinja template)
#templates/home.html (extends base.html)
#creates requirements.txt
#creates a new python env with above file

#creates .env
#.gitignore
#.dockerignore
#Dockerfile
#Basic README.md

#Basic .github/workflows/deploy.yml