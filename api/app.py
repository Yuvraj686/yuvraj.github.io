from flask import Flask, render_template

# IMPORTANT: adjust template + static paths
app = Flask(
    __name__,
    template_folder="../templates",
    static_folder="../static"
)

PORTFOLIO_PROJECTS = [
    {'id': 1, 'name': 'Online Classroom Platform', 'description': 'A platform for online learning and collaboration'},
    {'id': 2, 'name': 'Drive Dreams', 'description': 'This contains dreams for F1 lovers'},
    {'id': 3, 'name': 'Portfolio Website', 'description': 'A personal portfolio website to showcase my projects and skills.'}
]

@app.route('/')
def home():
    return render_template('home.html', projects=PORTFOLIO_PROJECTS, title='My Portfolio')

# ✅ REQUIRED for Vercel
handler = app