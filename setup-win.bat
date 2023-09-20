:: Step 1: Create and activate virtual environment
python -m venv venv
venv\Scripts\activate

:: Step 2: Install requirements
pip install -r requirements.txt

:: Step 3: Create .env file
copy sample.env .env

:: Step 4: Run migrations
python manage.py migrate

:: Step 5: Load fixture data
python manage.py loaddata data/polls.json
python manage.py loaddata data/users.json

:: Step 6: Run tests
python manage.py test

:: Step 7: Start development server
python manage.py runserver