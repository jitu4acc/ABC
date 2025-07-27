@echo off
echo Starting AI Chatbot Backend (Groq Only)...
echo.

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    pause
    exit /b 1
)

REM Check if pipenv is available
python -m pipenv --version >nul 2>&1
if errorlevel 1 (
    echo Installing dependencies with pip...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo Error: Failed to install dependencies
        pause
        exit /b 1
    )
    echo Starting backend with regular Python...
    python backend.py
) else (
    echo Installing dependencies with pipenv...
    python -m pipenv install
    if errorlevel 1 (
        echo Error: Failed to install dependencies with pipenv
        pause
        exit /b 1
    )
    echo Starting backend with pipenv...
    python -m pipenv run python backend.py
)

pause
