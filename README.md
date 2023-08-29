# KU polls

The application is built using Python and the [Django] web framework. It allows creating polls with multiple choice questions that users can vote on.

This app was created as part of the [Individual Software Process](
https://cpske.github.io/ISP) course at Kasetsart University.

## Requirements
- Requires Python 3.8+ and packages listed in [requirements.txt](./requirements.txt). 

## Installation and Configuration
- Follow the installation steps in the [Installation]

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
- Iteration 1 [Plan](https://github.com/Jwizzed/ku-polls/wiki/Iteration-1-Plan) and [Project Board]()
- Iteration 2 [Plan](https://github.com/Jwizzed/ku-polls/wiki/Iteration-2-Plan) and [Project Board]()
- Iteration 3 [Plan](https://github.com/Jwizzed/ku-polls/wiki/Iteration-3-Plan) and [Project Board]()
- Iteration 4 [Plan](https://github.com/Jwizzed/ku-polls/wiki/Iteration-4-Plan) and [Project Board]()


[Django]: https://docs.djangoproject.com/en/3.1/intro/tutorial01/
[Installation]: ../../wiki/Installation 