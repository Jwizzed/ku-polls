## Installation and Configuration
### Using setup script
1. Clone the repository and change directory into the repo
   ```
   git clone https://github.com/Jwizzed/ku-polls.git
   cd ku-polls
   ```
2. Execute the setup script

   For Linux/MacOS:
   ```
   chmod +x setup-linux.sh
   ./setup-linux.sh
   ```
   For Windows (If it doesn't work, try `Manual Installation`):
   ```
   setup-win.bat
   ```

### Manual Installation
1. Clone the repository
   ```
   git clone https://github.com/Jwizzed/ku-polls.git
   ```
2. Change directory into the repo
   ```
   cd ku-polls
   ```
3. Create a virtual environment
   ```
   python -m venv venv
   ```
4. Activate the virtual environment:
   ```
   # On Linux or MacOS:
   source venv/bin/activate
   
   # On Windows:
   call venv\Scripts\activate
   ```
5. Install the required packages
   ```
   pip install -r requirements.txt
   ```
6. Create a .env file by copying the contents of sample.env
   
   ```
   # On Linux/MacOS:
   cp sample.env .env

   # On Windows:
   copy sample.env .env
   ```
   Note: After copying, make sure to edit the .env file to set any environment-specific values as needed.
7. Run migrations
   ```
   python manage.py migrate
   ```
8. Load fixture data
   ```
   python manage.py loaddata data/polls.json 
   python manage.py loaddata data/users.json
   ```
9. Run tests
   ```
   python manage.py test
   ```
10. Start the Django server
   ```
   python manage.py runserver
   ```