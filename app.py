from flask import Flask, render_template, request, url_for
"""Flask application"""

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/course')
def course():
    return render_template('course.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
