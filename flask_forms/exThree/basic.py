from flask import Flask, render_template, flash, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)

app.config['SECRET_KEY'] = 'kmykey'

class SimpleForm(FlaskForm):

    submit = SubmitField('Click me.')
    breed = StringField("What breed are you? ")

@app.route('/', methods=['GET','POST'])
def index():
    
    form = SimpleForm()

    if form.validate_on_submit():
        session['breed'] = form.breed.data
        # flash('You just clicked the button!')
        flash(f"The breed that you have choosen is: {session['breed']}")
        # we could have more than one flash message
        # flash('Hey, how is it going?')

        return redirect(url_for('index'))

    return render_template('index.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)