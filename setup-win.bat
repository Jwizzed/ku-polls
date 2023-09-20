:: Step 1: Clone the repository
git clone https://github.com/Jwizzed/ku-polls.git
cd ku-polls

:: Step 2: Create and activate virtual environment
python -m venv .venv
.venv\Scripts\activate

:: Step 3: Create .env file
copy sample.env .env

:: Step 4: Run migrations
python manage.py migrate

:: Step 5: Load fixture data
python manage.py loaddata polls.json
python manage.py loaddata users.json

:: Step 6: Run tests
python manage.py test

:: Step 7: Install requirements
pip install -r requirements.txt

:: Step 8: Start development server
python manage.py runserver