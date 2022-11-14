from flask import Flask

# Create an application object
# __name__ -> python predefined variable (are we running the script directly?)
app = Flask(__name__)

# This decorator links my page to wherever route it should be at
# In this case, it is at home page ('/')
@app.route('/')  # 127.0.0.1:5000
def index():
    return '<h1>Hello Puppy!</h1>'

@app.route('/information')  # 127.0.0.1:5000/information
def info():
    return "<h1>Puppies are cute!</h1>"

@app.route('/puppy/<name>')
def puppy(name):
    # return "<h1>This is a page for {}</h1>".format(name)
    return "100th letter: {}".format(name[100])

if __name__ == "__main__":
    # Never use debug mode when you are deploying your site to production
    app.run(debug=True)
