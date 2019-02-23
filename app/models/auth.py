from app import db, app

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    is_admin = db.Column(db.Boolean, nullable=False, default=False)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'is_admin': self.is_admin
        }

    @classmethod
    def get_all(cls):
        return [x.to_dict() for x in User.query.all()]

    @classmethod
    def delete_all(cls):
        db.session.query(cls).delete()
        db.session.commit()

    @classmethod
    def get_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
