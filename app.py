from flask import Flask, render_template, request
"""Flask application"""


app = Flask(__name__, template_folder='templates')


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        username = request.form.get('password')


        if username == 'skill' and password == 'password':
            return 'Success'
        else:
            return 'Failure'


#Custom filter function
@app.template_filter('reverse_string')
def reverse_string(s):
    return s[::-1]


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
