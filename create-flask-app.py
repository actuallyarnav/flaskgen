import os, venv, subprocess

print("Flask App Generator v0.1")

PROJECT_DIR = input("Enter the project directory (. for current): ").strip()

os.makedirs(os.path.join(PROJECT_DIR, "static"), exist_ok=True)

with open(os.path.join(PROJECT_DIR, "app.py"), "w") as f:
    f.write("""from flask import Flask, render_template, request, redirect, url_for, send_from_directory, flash
from dotenv import load_dotenv
import os

from werkzeug.utils import secure_filename
load_dotenv()

app = Flask(__name__)

app.secret_key =  os.getenv("SECRET_KEY")

@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('home.html')


@app.route("/health")
def health():
    return "OK", 200

@app.route('/about', methods=['POST', 'GET'])
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)""")
print(f"Created {os.path.join(PROJECT_DIR, "app.py")}")

IS_LOCAL_BOOTSTRAP = input("Would you like to download Bootstrap locally? (Y/n): ").strip().lower() != 'n'
if IS_LOCAL_BOOTSTRAP:
    #create static folder
    os.makedirs(os.path.join(PROJECT_DIR, "static/css"), exist_ok=True)
    print(f"Created {os.path.join(PROJECT_DIR, "static/css")}")
    os.makedirs(os.path.join(PROJECT_DIR, "static/js"), exist_ok=True)
    print(f"Created {os.path.join(PROJECT_DIR, "static/js")}")

os.makedirs(os.path.join(PROJECT_DIR, "templates"), exist_ok=True)
print(f"Created {os.path.join(PROJECT_DIR, "templates")}")
print("Creating base.html...")
with open(os.path.join(PROJECT_DIR, "templates", "base.html"), "w") as f:
    f.write("""<!doctype html>
<html lang="en" data-bs-theme="dark">

<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />""")
    if IS_LOCAL_BOOTSTRAP:
        f.write("""<link href="../static/css/bootstrap.min.css" rel="stylesheet" />
    <script src="../static/js/bootstrap.min.js">

    </script>""")
    else:
        f.write("""<link
            href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.7/dist/css/bootstrap.min.css"
            rel="stylesheet"
            integrity="sha384-LN+7fdVzj6u52u30Kp6M/trliBMCMKTyK833zpbD+pXdCLuTusPj697FH4R/5mcr"
            crossorigin="anonymous"
        />
        <script
            src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.7/dist/js/bootstrap.bundle.min.js"
            integrity="sha384-ndDqU0Gzau9qJ1lfW4pNLlhNTkCfHzAVBReH9diLvGRem5+R9g2FzA8ZGN954O5Q"
            crossorigin="anonymous"
        ></script>""")
    f.write("""{% block head %}{% endblock %}
</head>

<body>
    {% with messages = get_flashed_messages(with_categories=true) %} {% if
    messages %} {% for category, message in messages %}
    <div class="alert alert-{{ category }} alert-dismissible fade show" role="alert">
        {{ message }}
        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
    </div>
    {% endfor %} {% endif %} {% endwith %}
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
        <div class="container-fluid">
            <a class="navbar-brand" href="/">Project</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav"
                aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav">
                    <li class="nav-item">
                        <a class="nav-link active" aria-current="page" href="/">Home</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>


    {% block body %}{% endblock %}
</body>

</html>""")
print(f"Created {os.path.join(PROJECT_DIR, "templates/base.html")}")

with open(os.path.join(PROJECT_DIR, "templates", "home.html"), "w") as f:
    f.write("""{% extends 'base.html' %} {% block head %}
<title>Home</title>
{% endblock %} {% block body %}
{% endblock %}
""")
print(f"Created {os.path.join(PROJECT_DIR, "templates/home.html")}")

VENV_NAME = input("Enter the name for the Python venv: ").strip()
#create python venv using given name
venv.create(os.path.join(PROJECT_DIR, VENV_NAME), with_pip=True)
print("Created Python virtual environment")
venv_python = os.path.join(PROJECT_DIR, VENV_NAME, "bin", "python")

subprocess.run([venv_python, "-m", "pip", "install", "--upgrade", "pip"])
subprocess.run([venv_python, "-m", "pip", "install", "flask", "python-dotenv"])

with open(os.path.join(PROJECT_DIR, ".env"), "w") as f:
    f.write("""# .env
SECRET_KEY=super-secret-key
""")
print(f"Created {os.path.join(PROJECT_DIR, ".env")}")

with open(os.path.join(PROJECT_DIR, ".gitignore"), "w") as f:
    f.write(""".vscode/
env/
static/uploads/
.env
test/
keys/
__pycache__/
""")
print(f"Created {os.path.join(PROJECT_DIR, ".gitignore")}")

with open(os.path.join(PROJECT_DIR, ".dockerignore"), "w") as f:
    f.write("""__pycache__/
.vscode/
env/
test/""")
print(f"Created {os.path.join(PROJECT_DIR, ".dockerignore")}")

with open(os.path.join(PROJECT_DIR, "Dockerfile"), "w") as f:
    f.write("""FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8080

CMD ["python3", "app.py"]""")
print(f"Created {os.path.join(PROJECT_DIR, "Dockerfile")}")

result = subprocess.run([venv_python, "-m", "pip", "freeze"], capture_output=True, text=True)
with open(os.path.join(PROJECT_DIR, "requirements.txt"), "w") as f:
    f.write(result.stdout)
print(f"Created {os.path.join(PROJECT_DIR, "requirements.txt")}")

with open(os.path.join(PROJECT_DIR, "README.md"), "w") as f:
    f.write("""# Project
This is a description of the project.

## Header 1

## How to run
Currently you can run this locally using Python or Docker.

```git clone {github link}```

```cd {project}```

### Python
#### requirements: python3, pip
```pip install --no-cache-dir -r requirements.txt```

```python3 app.py```


### Docker
#### requirements: docker (of course)

```docker build -t {project} .```

```docker run -p 8080:8080 {project}```

Open ```http://127.0.0.1:8080/``` in a web browser
## Currently working

## To Do
""")
MAKE_GITHUB_ACTIONS = input("Would you like to create .github/workflows/deploy.yml?? (Y/n): ").strip().lower() != 'n'
os.makedirs(os.path.join(PROJECT_DIR, ".github", "workflows"), exist_ok=True)

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