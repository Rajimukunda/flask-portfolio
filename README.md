# 🌐 Flask Portfolio Website

A simple and elegant **personal portfolio website** built with **Flask**, **HTML**, and **CSS**.  
This project lets you showcase your profile, skills, and projects, and includes a working **contact form**.  

---

## 🚀 Project Overview

This is a real-world mini web app developed using Flask — a lightweight Python web framework.  
It demonstrates:
- Flask routing and template rendering  
- HTML + CSS layout and styling  
- Handling contact form submissions  
- Dynamic data rendering (name, skills, projects, etc.)

---

## 🧰 Tools & Technologies

| Tool | Purpose |
|------|----------|
| **Python 3** | Main programming language |
| **Flask** | Web framework for backend and routing |
| **HTML5** | Page structure and layout |
| **CSS3** | Styling and responsiveness |
| **Jinja2** | Flask’s templating engine for dynamic content |
| **Virtual Environment (venv)** | Isolate dependencies |

---

## 🏗️ Project Structure

flask-portfolio/
├─ app.py
├─ requirements.txt
├─ templates/
│ ├─ base.html
│ ├─ index.html
│ ├─ contact.html
│ └─ thanks.html
├─ static/
│ └─ css/
│ └─ style.css
## ⚙️ Setup & Run Locally

Follow these simple steps to run the project on your local machine:

### 1️⃣ Clone the repository
```bash
git clone https://github.com/YOUR-USERNAME/flask-portfolio.git
cd flask-portfolio
2️⃣ Create a virtual environment
bash
Copy code
python -m venv venv
# Activate it:
venv\Scripts\activate   # for Windows
# or
source venv/bin/activate  # for macOS/Linux
3️⃣ Install dependencies
bash
Copy code
pip install -r requirements.txt
4️⃣ Run the Flask app
bash
Copy code
python app.py
Now open your browser and visit:
👉 http://127.0.0.1:5000

💡 Features
🏠 Home Page: Displays your personal information, bio, and projects

⚙️ Dynamic Content: Skills and projects are rendered dynamically via Flask

📩 Contact Form: Simple form to collect name, email, and message

🎨 CSS Styling: Clean, responsive, and easy to customize

🧱 Modular Templates: Uses Flask’s base.html inheritance for easy maintenance

🧩 Example Customization
Edit the profile dictionary inside app.py:

python
Copy code
profile = {
    'name': 'Your Name',
    'title': 'Software Engineer / Student',
    'bio': 'A short bio about you — your skills, interests, and goals.',
    'skills': ['Python', 'Flask', 'HTML', 'CSS'],
    'projects': [
        {'title': 'Project A', 'description': 'Short description', 'url': '#'},
        {'title': 'Project B', 'description': 'Short description', 'url': '#'},
    ]
}


