@echo off
title Aqua Bandhu AI Platform
echo ========================================================
echo        AQUA BANDHU AI - SEAFOOD SUPPLY CHAIN
echo ========================================================
echo Starting FastAPI server at http://127.0.0.1:8000 ...

if exist ".venv\Scripts\python.exe" (
    ".venv\Scripts\python.exe" run.py
) else (
    py run.py
)

pause
