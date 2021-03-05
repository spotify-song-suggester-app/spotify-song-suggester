


import pandas as pd
from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField,\
				StringField, SelectField, DecimalField,\
				DateField
from wtforms.validators import DataRequired, ValidationError


class MyForm(FlaskForm):
	name = StringField(label='Song Name')
	artist = StringField(label='Artist')
	submit = SubmitField(label='Submit')

