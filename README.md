# DevOps CI/CD Lab

A small Flask service with automated tests and a Jenkins pipeline. The pipeline creates a Python virtual environment, installs the project dependencies, runs the test suite, and publishes a JUnit report.

## Requirements

- Python 3.10 or newer
- Jenkins with the Pipeline and JUnit plugins
- Python available on the Jenkins agent

## Run locally

On Windows PowerShell:

```powershell
py -3 -m venv .venv
.\.venv\Scripts\python -m pip install -r requirements.txt
.\.venv\Scripts\python -m pytest -q
.\.venv\Scripts\python app\app.py
```

On macOS or Linux:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m pytest -q
.venv/bin/python app/app.py
```

The service responds at `http://127.0.0.1:5000/` and exposes a health check at `/health`.
