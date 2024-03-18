'''
Creating Database Models
'''
from app.extensions import db

class Models(db.Model):
    __tablename__ = 'Models'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    date = db.Column(db.Date)
    message = db.Column(db.Text)

    def __repr__(self):
        return f'{self.name}, {self.date}, {self.comment}'