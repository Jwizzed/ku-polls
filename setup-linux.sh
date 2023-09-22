#!/bin/bash

# Function to find Python executable
find_python() {
  if command -v python3 &>/dev/null; then
    echo "python3"
  elif command -v python &>/dev/null; then
    echo "python"
  else
    echo "No suitable Python version found. Exiting."
    exit 1
  fi
}

# Step 1: Create and activate a virtual environment
PYTHON=$(find_python)
$PYTHON -m venv venv

# Check if venv was successfully created
if [ $? -ne 0 ]; then
  echo "Virtual environment creation failed. Exiting."
  exit 1
fi

source venv/bin/activate

# Step 2: Install requirements
pip install -r requirements.txt

# Step 3: Create .env file
cp sample.env .env

# Step 4: Run migrations
$PYTHON manage.py migrate

# Step 5: Load fixture data
$PYTHON manage.py loaddata data/polls.json
$PYTHON manage.py loaddata data/users.json

# Step 6: Run tests
$PYTHON manage.py test

# Step 7: Start development server
$PYTHON manage.py runserver
