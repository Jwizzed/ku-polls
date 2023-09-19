# KU polls
[![Django CI](https://github.com/Jwizzed/ku-polls/actions/workflows/django.yml/badge.svg)](https://github.com/Jwizzed/ku-polls/actions/workflows/django.yml)

The application is built using Python and the [Django] web framework. It allows creating polls with multiple choice questions that users can vote on.

This app was created as part of the [Individual Software Process](
https://cpske.github.io/ISP) course at Kasetsart University.

## Requirements
- Requires Python 3.8+ and packages listed in [requirements.txt](./requirements.txt). 
- You can also see in [Project wiki]

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
   For Windows:
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
   python -m venv .venv
   ```
4. Activate the virtual environment:
   ```
   # On Linux or MacOS:
   source .venv/bin/activate
   
   # On Windows:
   .venv\Scripts\activate
   ```
5. Create a .env file by copying the contents of sample.env
   
   ```
   # On Linux/MacOS:
   cp sample.env .env

   # On Windows:
   copy sample.env .env
   ```
   Note: After copying, make sure to edit the .env file to set any environment-specific values as needed.
6. Install the required packages
   ```
   pip install -r requirements.txt
   ```
7. Start the Django server
   ```
   python manage.py runserver
   ```
   

## Running the Application
1. Activate the virtual environment
   ```
   # On Linux or MacOS:
   source .venv/bin/activate
   
   # On Windows:
   .venv\Scripts\activate
   ```
2. Start the Django development server
   ```
   python manage.py runserver
   ```
   If you get a message that the port is unavailable, then run the server on a different port (1024 thru 65535) such as:
   ```
   python3 manage.py runserver 12345
   ```
3. Access the app in a web browser at <http://localhost:8000>
4. Exit the virtual environment by closing the window or by typing:
   ```
   deactivate
   ```
## Demo Admin Account
| Username | Password  |
|----------|-----------|
| admin    | testpass1 |

## Demo User Accounts
| Username | Password  |
|----------|-----------|
| demo1    | testpass1 |
| demo2    | testpass2 |
| demo3    | testpass3 |

## Project Documentation
### Project wiki
- [Vision Statement](https://github.com/Jwizzed/ku-polls/wiki/Vision-Statement)
- [Requirements](https://github.com/Jwizzed/ku-polls/wiki/Requirements)
- [Development Plan](https://github.com/Jwizzed/ku-polls/wiki/Development-Plan)
- [Domain Model](https://github.com/Jwizzed/ku-polls/wiki/Domain-Model)

### Iterations
- Iteration 1 [Plan](https://github.com/Jwizzed/ku-polls/wiki/Iteration-1-Plan) and [Project Board](https://github.com/users/Jwizzed/projects/1)
- Iteration 2 [Plan](https://github.com/Jwizzed/ku-polls/wiki/Iteration-2-Plan) and [Project Board](https://github.com/users/Jwizzed/projects/1/views/9)
- Iteration 3 [Plan](https://github.com/Jwizzed/ku-polls/wiki/Iteration-3-Plan) and [Project Board](https://github.com/users/Jwizzed/projects/1/views/12)
- Iteration 4 [Plan](https://github.com/Jwizzed/ku-polls/wiki/Iteration-4-Plan) and [Project Board](https://github.com/users/Jwizzed/projects/1/views/13)


[Django]: https://docs.djangoproject.com/en/3.1/intro/tutorial01/
[Project wiki]: ../../wiki 
