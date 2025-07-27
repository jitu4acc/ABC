@echo off
echo Starting AI Chatbot Frontend...
echo.
echo Make sure the backend is running on http://127.0.0.1:9999
echo.

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    pause
    exit /b 1
)

REM Start Streamlit
echo Starting Streamlit frontend...
streamlit run frontend.py --server.port 8501

pause
