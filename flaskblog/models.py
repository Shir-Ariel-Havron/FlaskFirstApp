from flaskblog import db, login_manager
from datetime import datetime as dt
from flask_login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from sqlalchemy import create_engine
from sqlalchemy.dialects import postgresql


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


def add_column(app, table_name, column):
    engine = create_engine(
        app.config['SQLALCHEMY_DATABASE_URI'], convert_unicode=True)
    column_name = column.compile(dialect=engine.dialect)
    column_type = column.type.compile(engine.dialect)
    engine.execute(
        f'ALTER TABLE {table_name} ADD COLUMN {column_name} {column_type}')


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False,
                           default='default.jpeg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

    def get_reset_token(self, expires_seconds=1800):
        s = Serializer(current_app.config['SECRET_KEY'], expires_seconds)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=dt.utcnow)
    content = db.Column(db.Text, nullable=False)
    link = db.Column(db.String(2048))
    tags = db.Column(postgresql.ARRAY(db.String))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"
