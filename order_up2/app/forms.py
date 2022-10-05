from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, Boolean
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    employee_number = StringField("Employee Number", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")


class OrderForm(FlaskForm):
    employee_id =
    table_id = 
    finished = Boolean("Closed Table")
