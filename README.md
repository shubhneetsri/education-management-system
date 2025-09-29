Setup Poetry for Dependency Management:

pip install poetry
poetry config --unset virtualenv.create
poetry --version
poetry init --no-interaction

Setup Virtual env in local Folder:

poetry config --local virtualenvs.in_project true
poetry env list
poetry env remove python  # [If Already Exists]
poetry install
poetry shell  # activate environment
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process  # [If PowerShell]
.\.venv\Scripts\activate.ps1

Setup UV for fast Installation of packages:

pip install uv
pip freeze > requirements.txt
OR
poetry self add poetry-plugin-export  # [Latest]
poetry export -f requirements.txt --output requirements.txt --without-hashes

Ah, this is a common point of confusion. You don’t strictly need a requirements.txt if you’re using Poetry — your pyproject.toml and poetry.lock already define all dependencies.

Deployment to environments that don’t support Poetry:
Many hosting services, CI/CD pipelines, or container setups (like AWS Lambda, Docker, Heroku, ECS, etc.) expect a requirements.txt to install dependencies via pip.
Poetry isn’t always installed in the target environment, so pip install -r requirements.txt is simpler and standard.

1️⃣ poetry export
Tell Poetry to export your project’s dependencies in a format that other tools can understand, usually for pip.

2️⃣ -f requirements.txt
-f means format.
Here, it specifies that the exported file should be in pip requirements.txt format.

3️⃣ --output requirements.txt
Writes the output to a file named requirements.txt in the current directory.
Without this, the exported text would just print to the terminal.

4️⃣ --without-hashes
Poetry can generate dependencies with hashes for security (to verify package integrity).
--without-hashes removes those hashes, making the requirements.txt cleaner and compatible with standard pip install -r requirements.txt.

uv pip sync requirements.txt
uv doesn’t resolve dependencies itself — it just installs them very fast, much faster than Poetry or pip alone.

Why use it if Poetry already installed them?
Local dev: You usually don’t need uv — Poetry install is fine.
CI/CD / Docker builds / large projects:
Poetry install is slower, especially if there are 100+ dependencies.
Using uv pip sync requirements.txt reuses the lockfile but installs much faster.

This is why many companies combine them:
Poetry → lockfile management (source of truth)
uv → fast installation during builds

Think of it as “Poetry manages what should be installed, uv just does it faster”.

Ah! This is an important concept for why FastAPI uses Uvicorn (an ASGI server) instead of the traditional WSGI servers.
WSGI (used by Flask, Django traditional apps).
Uvicorn is a lightweight ASGI server written in Rust + Python.

Run the app with autoreload:

uvicorn education_management_system.main:app --reload

Pull postgres:

docker run --name my_postgres -e POSTGRES_USER=myuser -e POSTGRES_PASSWORD=mypassword -e POSTGRES_DB=mydb -p 5432:5432 -d postgres:latest

Add alembic and initialize migrations:

poetry add alembic
alembic init migrations
