from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Optional, URL


class PostForm(FlaskForm):
    title = StringField('כותרת', validators=[DataRequired()])
    content = TextAreaField('תוכן', validators=[DataRequired()])
    link = StringField('לינק ליוטיוב', validators=[Optional(), URL()])
    submit = SubmitField('פרסום')
