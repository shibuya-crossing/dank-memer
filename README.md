# Dank memer

## Installation

- `git clone https://github.com/shibuya-crossing/dank-memer.git`
- add a .env file containing `TOKEN="Xxxxxxxxxxxxxxxxx"`
- add a config.json containing
```json
{
  "channels": {
    "token": 696969696996,
  }
}
```
where the value of channels.token is your channel id

- python -m venv venv
- activate venv (commands vary depending on your os)
  - windows: `venv\Scripts\Activate.ps1`
  - linux: `source venv/bin/activate`
- `pip install -r requirements.txt`
- `python dank.py -u token`