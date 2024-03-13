from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Authors(db.Model):
    id_ = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(120), nullable=False)
    book = db.relationship('Books', backref=db.backref('authors'), lazy=True)


    def __repr__(self):
        return f'Author({self.name}, {self.last_name})'


class Books(db.Model):
    id_ = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(80), nullable=False)
    date = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    authors_id = db.Column(db.Integer, db.ForeignKey('authors.id_'), nullable=False)
    author = db.relationship('Authors', backref=db.backref('books'), lazy=True)





    def __repr__(self):
        return f'Book({self.book_name})'