from flask_wtf import FlaskForm
from wtforms import SubmitField, RadioField
from flask_wtf.file import FileField, FileAllowed, FileRequired

class UploadForm(FlaskForm):
    upload = FileField('Image', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png'], 'Images only!')
    ])

    base = RadioField('Base', choices=[('Piano','Piano'),('Acoustic','Acoustic'), ("Electronic", "Pop/Electronic")])

    submit = SubmitField("Submit")