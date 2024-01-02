# Telegram forwarder

## Installation
Python 3.10+ required.

Create and activate venv:
```shell
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:
```shell
pip install requirements.txt
```

Configure environment:
```shell
cp .env.temp .env
```
Open the .env file with vim or nano or other editor and set variables.

## Run

Activate venv (if you haven't already do that):
```shell
source venv/bin/activate
```

Startup:
```shell
python main.py
```

On a first launch you need to log in to account.
