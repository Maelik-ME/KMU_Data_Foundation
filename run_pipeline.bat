@echo off
SETLOCAL

REM --- Set project root to location of this file ---
cd /d "%~dp0"

REM --- Adjust if Anaconda is installed elsewhere ---
SET CONDA_BASE=C:\Users\Maelik\anaconda3

CALL "%CONDA_BASE%\Scripts\activate.bat"
CALL conda activate zyklop

echo Running KMU Data Pipeline...
python -m src.pipeline

echo.
echo Pipeline finished with exit code %ERRORLEVEL%
pause
