from app import db

class Realisation(db.Model):
    __tablename__ = 'realisations'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(255))
    price = db.Column(db.Float, nullable=False)
    category = db.Column(db.Text, nullable=False)
