@echo off
setlocal

set "ROOT=%~dp0"
set "VENV=%ROOT%.venv"
set "PY=%VENV%\Scripts\python.exe"

if not exist "%VENV%" (
  echo [cycwrite] creating virtual environment...
  python -m venv "%VENV%"
  if errorlevel 1 exit /b 1
)

echo [cycwrite] upgrading pip...
"%PY%" -m pip install --upgrade pip || exit /b 1

echo [cycwrite] installing pinned dependencies...
"%PY%" -m pip install -r "%ROOT%requirements-cycwrite.txt" || exit /b 1

echo [cycwrite] installing chromium for playwright...
"%PY%" -m playwright install chromium || exit /b 1

echo [cycwrite] runtime ready: %PY%
exit /b 0
