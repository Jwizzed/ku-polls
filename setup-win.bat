:: Step 1: Create and activate virtual environment
python -m venv .venv
.venv\Scripts\activate

:: Step 2: Create .env file
copy sample.env .env

:: Step 3: Run migrations
python manage.py migrate

:: Step 4: Load fixture data
python manage.py loaddata polls.json
python manage.py loaddata users.json

:: Step 5: Run tests
python manage.py test

:: Step 6: Install requirements
pip install -r requirements.txt

:: Step 7: Start development server
python manage.py runserver