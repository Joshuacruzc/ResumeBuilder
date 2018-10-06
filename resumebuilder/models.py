from datetime import datetime
from flask_login import UserMixin
from resumebuilder import db, login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


experience_tag_table = db.Table('experience_tag', db.Column('experience_id', db.Integer, db.ForeignKey('experience.id'), primary_key=True),
                db.Column('experienceTag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True))


class Experience(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    proposition1 = db.Column(db.String(300))
    proposition2 = db.Column(db.String(300), nullable=True)
    proposition3 = db.Column(db.String(300), nullable=True)
    date = db.Column(db.DateTime)
    role = db.Column(db.String(60))
    host = db.Column(db.String(100))    # employer

    def __repr__(self):
        """Define a base way to print models"""
        return '%s(%s)' % (self.__class__.__name__, {
            column: value
            for column, value in self._to_dict().items()
        })

    tags = db.relationship('Tag', secondary="experience_tag", backref='experiences')

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.column(db.String(40))

class User(db.Model, UserMixin):
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column( db.String(60), nullable=False)
    password = db.Column( db.String(60), nullable=False)
    email = db.Column( db.String(50), unique=True)
    profile_picture = db.Column(db.String(120), nullable = False, default = 'default.jpg')
    registered_on = db.Column(db.DateTime, nullable= False, default=datetime.utcnow)

    def __repr__(self):
        return f"User('{self.name}')"