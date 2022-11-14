# Set up your imports here!
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Welcome! Go to /puppy_latin/name to see your name in puppy latin!</h1>"

@app.route('/puppy_latin/<name>') # Fill this in!
def puppylatin(name):

    # if name[-1] != 'y':
    #     puppylatin_name = name + 'y'
    # else:
    #     puppylatin_name = name[:-1] + 'iful'

    puppylatin_name = name + 'y' if name[-1] != 'y' else name[:-1] + 'iful'

    return f"<h1>Hi {name}! Your puppyLatin name is {puppylatin_name}</h1>"

if __name__ == '__main__':
    # Fill me in!
    app.run(debug=True)
