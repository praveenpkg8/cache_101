from models import db
import uuid


class User(db.Model):

    __tablename__ = 'user'

    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String(120))
    email = db.Column(db.String(120))
    phone_number = db.Column(db.String(120))

    def __init__(self, name, email, phone_number):
        self.id = str(uuid.uuid4())
        self.name = name
        self.email = email
        self.phone_number = phone_number

    @staticmethod
    def create_user(user):
        db.session.add(user)
        db.session.commit()


    @staticmethod
    def get_user_by_email(email):
        user = User.query.filter_by(email=email).first()
        user_dict = user.__dict__
        return user_dict



