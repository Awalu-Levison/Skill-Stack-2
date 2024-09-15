from flask import Flask, render_template
"""Flask application"""

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


if __mame__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
