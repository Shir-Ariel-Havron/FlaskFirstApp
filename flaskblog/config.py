import os


class Config:
    SECRET_KEY = 'bba2894ae248caf20c394f74a58914c2'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'matan.arielhavron1'
    MAIL_PASSWORD = 'gmMATANSKI17'
