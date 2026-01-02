# Simple Web Honeypot (Python)

An educational Web Honeypot built in Python. It simulates a fake administration panel to capture login attempts.

## Features
It starts a web server on port `5000`.
- Displays a fake "Administration Panel".
- **Captures all credentials** (Username and Password) attempted.
- Displays stolen credentials in the console and saves them to `honeypot.log`.

  ## How it works
This honeypot operates by simulating a real web environment:
1. **Flask Server**: Initializes a lightweight server to handle HTTP requests.
2. **Redirection**: Any visit to the root `/` is redirected to the login panel.
3. **POST Capture**: When someone attempts to "log in," the script extracts:
    - **Username and Password**: Entered in the form.
    - **IP Address**: Identifies where the "attack" is coming from.
4. **Storage**: Logs every attempt in `honeypot.log` with a timestamp.
5. **Error Simulation**: The attacker sees an "Invalid credentials" message, which tricks them into trying more combinations while we continue capturing their data.

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

1. **Install Dependencies**: Run `pip install -r requirements.txt` in the terminal.
2. **Run**: `python main.py`.
3. **Test**: Go to `http://localhost:5000` in your browser, enter user/pass, and watch the `honeypot.log`.

## Legal Note
For educational purposes only.


