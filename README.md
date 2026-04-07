# Energy Database API

This project is a backend API built with FastAPI and SQLite.

## Technologies
- Python
- FastAPI
- Uvicorn
- SQLite
- SQLAlchemy

## Features
- Save energy values into a database
- Read all stored energy values
- Get summary statistics
- Add new values using a POST request

## Endpoints
- /
- /energy
- /add-energy
- /summary

## Run the project

Install dependencies:

pip install -r requirements.txt

Start the server:

py -m uvicorn main:app --reload

## Run with Docker

Build the image:

```bash
docker build -t energy-database-api .