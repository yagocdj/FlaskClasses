from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/report')
def report():
    username = request.args.get('username')
    has_lower = any(char.islower() for char in username)
    has_upper = any(char.isupper() for char in username)
    has_digit = username[-1:].isdigit()
    return render_template('report.html', has_lower=has_lower, has_upper=has_upper, has_digit=has_digit)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(debug=True)
