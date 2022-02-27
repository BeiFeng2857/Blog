from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/index', methods=["GET"])
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=51786, debug=True)