from app import db

#Database model for the assessments
#The title must also be unique to prevent two tests having the same name
class Assessment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), index=True, unique=True)
    module_code = db.Column(db.Integer)
    deadline_date = db.Column(db.Date)
    description = db.Column(db.String(500))
    completed = db.Column(db.Boolean)
