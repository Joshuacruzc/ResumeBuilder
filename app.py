from flask import Flask
from models import db

app = Flask(__name__)

POSTGRES = {
    'user': 'postgres',
    'pw': 'ResumeBuilderDB',
    'db': 'resume_db',
    'host': 'localhost',
    'port': '5432',
}

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
db.init_app(app)


if __name__ == '__main__':
    app.config['DEBUG'] = True
    app.run()
