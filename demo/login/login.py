from flask import *

app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != '123456':
            error = "sorry"
        else:
            return redirect(url_for('index'))
    return render_template('login.html', error=error)


@app.route("/index")
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8080,
        debug=True)