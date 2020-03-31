from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectMultipleField
from wtforms.validators import DataRequired, Optional, URL


class PostForm(FlaskForm):
    title = StringField('כותרת', validators=[DataRequired()])
    content = TextAreaField('תוכן', validators=[DataRequired()])
    link = StringField('לינק ליוטיוב', validators=[Optional(), URL()])
    # tags = StringField('תגיות, מופרדות בפסיקים', validators=[DataRequired])
    tags = SelectMultipleField(
        'תגיות', choices=[('value1', 'label1'), ('value2', 'label2')])
    submit = SubmitField('פרסום')
