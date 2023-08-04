This application is polls application built with Python and Django.

# Navigating the app using venv

1. Clone the Git repository to your computer

2. Create and activate a venv environment and install the requirments by entering the following commands,     assuming you already have Python installed:

    py -m pip install pip
    py -m pip install --user virtualenv
    py -m pip install --user virtualenvwrapper-win
    py -m venv capstone
    
    If that doesn't work, try replacing "py" with "python" or "python3"

    Then to activate the virtual environment:

    .\capstone\Scripts\activate

    Then install all the necessary requirements:
    
    pip install -r requirements.txt

3. Run the server:

    py manage.py runserver
    OR
    python manage.py runserver

# Navigating the app using Docker

1. Clone the repository to your computer

2. Build a Docker image and container using the following commands:
    docker build -t polls ./
    docker run -p 8000:8000 polls app

3. Visit 'http://localhost:8000/'
