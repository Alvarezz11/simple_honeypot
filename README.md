# Simple Web Honeypot (Python)

An educational Web Honeypot built in Python. It simulates a fake administration panel to capture login attempts.

## Features
It starts a web server on port `5000`.
- Displays a fake "Administration Panel".
- **Captures all credentials** (Username and Password) attempted.
- Displays stolen credentials in the console and saves them to `honeypot.log`.

## Project Map
```bash
simple_honeypot/
├── templates/
│   └── login.html      # Login panel HTML template
├── honeypot.log        # Hack attempt logs
├── main.py             # Main application (Flask)
├── requirements.txt    # Project dependencies
```

## Usage

1. **Open in VSCode**.
2. **Install Dependencies**: Run `pip install -r requirements.txt` in the terminal.
3. **Run**: Press `F5` or `python main.py`.
4. **Test**: Go to `http://localhost:5000` in your browser, enter user/pass, and watch the terminal.

## Legal Note
For educational purposes only.
