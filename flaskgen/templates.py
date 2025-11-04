# START TEXT CHUNKS
APP_PY_TEXT = """from flask import Flask, render_template, request, redirect, url_for, send_from_directory, flash
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
    app.run(host="0.0.0.0", port=8080, debug=True)"""

BASE_HTML_P1 = """<!doctype html>
<html lang="en" data-bs-theme="dark">

<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />"""

BASE_HTML_CDN = """<link
            href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.7/dist/css/bootstrap.min.css"
            rel="stylesheet"
            integrity="sha384-LN+7fdVzj6u52u30Kp6M/trliBMCMKTyK833zpbD+pXdCLuTusPj697FH4R/5mcr"
            crossorigin="anonymous"
        />
        <script
            src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.7/dist/js/bootstrap.bundle.min.js"
            integrity="sha384-ndDqU0Gzau9qJ1lfW4pNLlhNTkCfHzAVBReH9diLvGRem5+R9g2FzA8ZGN954O5Q"
            crossorigin="anonymous"
        ></script>"""

BASE_HTML_LOCAL = """<link href="../static/css/bootstrap.min.css" rel="stylesheet" />
    <script src="../static/js/bootstrap.min.js">

    </script>"""


BASE_HTML_P2 = """{% block head %}{% endblock %}
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

</html>"""

HOME_HTML = """{% extends 'base.html' %} {% block head %}
    <title>Home</title>
    {% endblock %} {% block body %}
    {% endblock %}
    """

ENV_TEXT = """# .env
    SECRET_KEY=super-secret-key
    """

GITIGNORE_TEXT = """.vscode/
    env/
    static/uploads/
    .env
    test/
    keys/
    __pycache__/
    """

DOCKERIGNORE_TEXT = """__pycache__/
    .vscode/
    env/
    test/"""

DOCKERFILE_TEXT = """FROM python:3.11-slim

    ENV PYTHONDONTWRITEBYTECODE=1
    ENV PYTHONUNBUFFERED=1

    WORKDIR /app

    COPY requirements.txt .

    RUN pip install --no-cache-dir -r requirements.txt

    COPY . .

    EXPOSE 8080

    CMD ["python3", "app.py"]"""

README_TEXT = """# Project
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
    """

#GITHUB_ACTIONS_TEXT = """"""

# END TEXT CHUNKS