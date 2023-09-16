:: Step 1: Create a virtual environment
python -m venv .venv

:: Step 2: Activate the virtual environment
.venv\Scripts\activate

:: Step 3: Create a .env file by copying the contents of sample.env
copy sample.env .env
echo Note: After copying, make sure to edit the .env file to set any environment-specific values as needed.

:: Step 4: Install the required packages
pip install -r requirements.txt

:: Step 5: Start the Django server (This step is optional in the script, as the user might want to run the server manually)
echo You can now start the Django server using the command: python manage.py runserver
