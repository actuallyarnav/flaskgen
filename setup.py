from setuptools import find_packages, setup

setup(
    name="flaskgen",
    version="1.1",
    author="Arnav R",
    description="A CLI tool to auto-generate a Flask project boilerplate",
    packages=find_packages(),
    install_requires=["flask", "python-dotenv"],
    entry_points={
        "console_scripts": [
            "flaskgen = flaskgen.main:main",
        ],
    },
)
