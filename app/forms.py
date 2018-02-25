from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileAllowed,FileRequired

class Upload(FlaskForm):
    images = FileField('Images', validators=[FileRequired(),FileAllowed(['jpg','png','jpeg'])])
    
