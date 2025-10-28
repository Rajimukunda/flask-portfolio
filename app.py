from flask import Flask, render_template, request, redirect, url_for, flash
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET', 'replace-this-with-a-secure-key')


@app.route('/')
def index():
    profile = {
        'name': 'Mukunda Rajeshwari',
        'title': 'Data Analyst / Student',
        'bio': 'A short bio about me- Python, SQL, HTML, CSS, JS, FLASK, POWER BI.',
        'skills': ['Python', 'Flask', 'HTML', 'CSS'],
        'projects': [
            {'title': 'Project A', 'description': 'Short description', 'https://github.com/Rajimukunda/todo-app': '#'},
            {'title': 'Project B', 'description': 'Short description', 'https://github.com/Rajimukunda/flask-rest-api.git': '#'},
        ]
    }
    return render_template('index.html', profile=profile)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # ✅ check indentation here — this code is *inside* the function
        if not name or not email or not message:
            flash('Please fill in all fields.', 'error')
            return redirect(url_for('contact'))

        # Optional: log message to console
        print(f'Contact form submitted: {name} <{email}> — {message}')

        return render_template('thanks.html', name=name)

    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)
