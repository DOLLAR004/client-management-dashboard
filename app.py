from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# A simple local storage mimicking a database for easy setup
# In-memory storage that resets when the app stops, perfect for a local showcase repo
clients_db = [
    {"id": 1, "name": "Alvin Omondi", "email": "alvin@example.com", "service": "Web Development", "status": "Active"},
    {"id": 2, "name": "Mary Wanjiku", "email": "mary@example.com", "service": "Graphic Design", "status": "Pending"}
]

@app.route('/')
def dashboard():
    # Renders the main dashboard template and injects our client data
    return render_template('dashboard.html', clients=clients_db)

@app.route('/add_client', methods=['POST'])
def add_client():
    if request.method == 'POST':
        new_id = len(clients_db) + 1
        new_client = {
            "id": new_id,
            "name": request.form['name'],
            "email": request.form['email'],
            "service": request.form['service'],
            "status": request.form['status']
        }
        clients_db.append(new_client)
        return redirect(url_for('dashboard'))

if __name__ == '__main__':
    # Runs the local development server
    app.run(debug=True)