# forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class AddForm(FlaskForm):

    name = StringField('Name of Puppy: ')
    submit = SubmitField('Add Puppy')

class DelForm(FlaskForm):

    id = IntegerField("Id number of puppy to remove: ")
    submit = SubmitField('Remove Puppy')
    