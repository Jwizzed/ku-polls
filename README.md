# KU polls
[![Django CI](https://github.com/Jwizzed/ku-polls/actions/workflows/django.yml/badge.svg)](https://github.com/Jwizzed/ku-polls/actions/workflows/django.yml)
<hr>
The application is built using Python and the [Django] web framework. It allows creating polls with multiple choice questions that users can vote on.

This app was created as part of the [Individual Software Process](
https://cpske.github.io/ISP) course at Kasetsart University.

## Requirements
- Requires Python 3.8+ and packages listed in [requirements.txt](./requirements.txt). 
- You can also see in [Project wiki]

## Installation and Configuration
1. Clone the repository
   ```
   git clone https://github.com/Jwizzed/ku-polls.git
   ```
2. Change directory into the repo
   ```
   cd ku-polls
   ```
3. Configure your settings in settings.ini or through environment variables. See settings.example.ini for reference.
4. Run the setup script for your OS:
   - Linux/Mac: ./setup-linux.sh
   - Windows: ./setup-win.ps1
5. Follow the prompts to complete installation.
6. Activate the virtual environment:
   ```
   source .venv/bin/activate
   ```
7. Start the Django server
   ```
   python manage.py runserver
   ```
   or
      ```
   python3 manage.py runserver
   ```
   

## Running the Application
1. Activate the virtual environment
    ```
    # activate the virtualenv for this project. On Linux or MacOS:
    source env/bin/activate
    # on MS Windows:
    env\Scripts\activate
    
    # start the django server
    python3 manage.py runserver
    ```
2. Start the Django development server
    ```
   Starting development server at http://127.0.0.1:8000/
   Quit the server with CONTROL-C.
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


## Demo User Accounts
Soon.

## Project Documentation
### Project wiki
- [Vision Statement](https://github.com/Jwizzed/ku-polls/wiki/Vision-Statement)
- [Requirements](https://github.com/Jwizzed/ku-polls/wiki/Requirements)
- [Development Plan](https://github.com/Jwizzed/ku-polls/wiki/Development-Plan)

### Iterations
- Iteration 1 [Plan](https://github.com/Jwizzed/ku-polls/wiki/Iteration-1-Plan) and [Project Board](https://github.com/users/Jwizzed/projects/1)
- Iteration 2 [Plan](https://github.com/Jwizzed/ku-polls/wiki/Iteration-2-Plan) and [Project Board](https://github.com/users/Jwizzed/projects/1/views/9)
- Iteration 3 [Plan](https://github.com/Jwizzed/ku-polls/wiki/Iteration-3-Plan) and [Project Board]()
- Iteration 4 [Plan](https://github.com/Jwizzed/ku-polls/wiki/Iteration-4-Plan) and [Project Board]()


[Django]: https://docs.djangoproject.com/en/3.1/intro/tutorial01/
[Project wiki]: ../../wiki 
