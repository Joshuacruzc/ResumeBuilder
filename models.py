from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

experiencetag = db.Table('tags', db.Column('experience_id', db.Integer, db.ForeignKey('experience.id'), primary_key=True),
                db.Column('experienceTag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True))


class Experience(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    proposition1 = db.Column(db.String(300))
    proposition2 = db.Column(db.String(300), nullable=True)
    proposition3 = db.Column(db.String(300), nullable=True)
    date = db.Column(db.String(10))
    roll = db.Column(db.String(60))
    host = db.Column(db.String(100))    # employer

    def __repr__(self):
        """Define a base way to print models"""
        return '%s(%s)' % (self.__class__.__name__, {
            column: value
            for column, value in self._to_dict().items()
        })

    tags = db.relationship('Tag', secondary=experiencetag,
                           backref=db.backref('experienceTags', lazy='dynamic'))


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tag = db.column(db.String(40))
