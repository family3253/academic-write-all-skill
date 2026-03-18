@echo off
setlocal

set "ROOT=%~dp0"
set "PY=%ROOT%.venv\Scripts\python.exe"

if not exist "%PY%" (
  echo [cycwrite] runtime missing, bootstrapping first...
  call "%ROOT%bootstrap_cycwrite_runtime.bat" || exit /b 1
)

"%PY%" "%ROOT%scripts\cycwrite_cli.py" %*
exit /b %errorlevel%
