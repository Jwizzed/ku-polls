@echo off
setlocal

:: Function to find Python executable
call :find_python PYTHON_CMD
if "%PYTHON_CMD%"=="" (
    echo No suitable Python version found. Exiting.
    exit /b 1
)

:: Step 1: Create and activate virtual environment
%PYTHON_CMD% -m venv venv
call venv\Scripts\activate

:: Step 2: Install requirements
pip install -r requirements.txt

:: Step 3: Create .env file
copy sample.env .env

:: Step 4: Run migrations
%PYTHON_CMD% manage.py migrate

:: Step 5: Load fixture data
%PYTHON_CMD% manage.py loaddata data/polls.json
%PYTHON_CMD% manage.py loaddata data/users.json

:: Step 6: Run tests
%PYTHON_CMD% manage.py test

:: Step 7: Start development server
%PYTHON_CMD% manage.py runserver

:: End of script
exit /b 0

:: Function to find Python executable
:find_python
    for %%i in (python3, python) do (
        where /q %%i
        if errorlevel 1 (
            echo %%i not found
        ) else (
            set "%1=%%i"
            exit /b 0
        )
    )
exit /b 1
