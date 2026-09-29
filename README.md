# Book Information Server

A Flask server that provides book information through a REST API endpoint.

## Prerequisites

Before starting, install:

- Python 3.10 or newer
- Git

The server uses port 5000.

## Install

Clone the repository:

bash
git clone https://github.com/whiteob04/server-assignment.git
cd server-assignment

## Create a virtual environment 
py -m venv .venv 
python3 -m venv .venv for mac/linux

## Activate the virtual environment:
.venv\Scripts\Activate.ps1
source .venv/bin/activate for mac/linux

## Install the dependencies:
python -m pip install -r requirements.txt
python -m pip install Flask (if No module named 'flask' error.)

## From the repository root, start the server:
python app.py

The server runs on:
http://127.0.0.1:5000

## Browser
Open:
http://127.0.0.1:5000/books

## Windows PowerShell
Open a second terminal and run:
curl.exe http://127.0.0.1:5000/books
curl http://127.0.0.1:5000/books for mac/linux

## Example Response
[
  {
    "author": "F. Scott Fitzgerald",
    "id": 1,
    "title": "The Great Gatsby",
    "year": 1925
  },
  {
    "author": "Toni Morrison",
    "id": 2,
    "title": "Beloved",
    "year": 1987
  }
]

Endpoint
Method	Route	Description
GET	    /books	Returns a list of books