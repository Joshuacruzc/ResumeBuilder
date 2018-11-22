from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

from resumebuilder.models import User


class RegistrationForm(FlaskForm):
    name = StringField('Name',
                       validators=[DataRequired(),Length(min=3, max=20),])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                             validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField('Confirm Password',
                                     validators =[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('An account with this email has already been registered')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                             validators=[DataRequired(), Length(min=8)])
    submit = SubmitField('Login')


class ExperienceForm(FlaskForm):
    proposition1 = StringField('Experience Summary',
                           validators=[DataRequired(), Length(min=3, max=300), ])
    proposition2 = StringField('Experience Summary (Optional)',
                           validators=[Length(min=0, max=300), ])
    proposition3 = StringField('Extra Details (Optional)',
                               validators=[Length(min=0, max=300), ])
    host = StringField('Host Name',
                           validators=[DataRequired(), Length(min=3, max=100), ])
    role = StringField('Role',
                       validators=[DataRequired(), Length(min=3, max=60), ])
    date = DateField('Start Date', format='%m/%d/%Y', validators=[DataRequired(),])

    tags = StringField('Experience tags', validators=[DataRequired(),])

    submit = SubmitField('Submit Experience')
