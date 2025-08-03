# fastapi-template

## Prerequisites

[Python](https://www.python.org/downloads/)

Please check you have python in your system or not by pasting the code in the terminal.

```
python3 --version
```

If python is installed in your system you will see something like this. Other than this please install python according to your platform.

## Project Setup

```sh
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip

# Activate the virtual environment
python3 -m venv venv
source venv/bin/activate
```

**Installing FastAPI and uvicorn**

```sh
pip install fastapi uvicorn
```

By this command we are installing fastapi and asynchronous server for running our backend. In case if you don’t know what is pip, pip is a python package manage just like npm and composer in node and php.

## Simple Project Structure

This is this basic project structure for FastAPI projects. Depending on the projects nature it can be more complex.

```sh
my_fastapi_project/
├── app/
│   ├── main.py            # Main entry point of the FastAPI app
│   ├── models.py          # Database models (if using SQLAlchemy, etc.)
│   ├── schemas.py         # Pydantic schemas for request/response validation
│   ├── crud.py            # Basic CRUD operations
│   ├── database.py        # Database connection setup
│   └── routes.py          # API routes
├── .env                   # Environment variables (e.g., DATABASE_URL)
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

## Run the app

```sh
uvicorn app.main:app --reload
```

By this command we are telling that run the [main.py](http://main.py/) which the entry point for our app where we instantiated the app. —reload flag enables the hot reload so that the changes can automatically updated.

```sh
uvicorn app.main:app --host 0.0.0.0 --port 8000
```
