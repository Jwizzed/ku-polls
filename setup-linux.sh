#!/bin/bash

# Step 1: Clone the repository
git clone https://github.com/Jwizzed/ku-polls.git

# Step 2: Change directory into the repo
cd ku-polls

# Step 3: Create a virtual environment
python -m venv .venv

# Step 4: Activate the virtual environment
source .venv/bin/activate

# Step 5: Create a .env file by copying the contents of sample.env
cp sample.env .env
echo "Note: After copying, make sure to edit the .env file to set any environment-specific values as needed."

# Step 6: Install the required packages
pip install -r requirements.txt

# Step 7: Start the Django server (This step is optional in the script, as the user might want to run the server manually)
echo "You can now start the Django server using the command: python manage.py runserver"
