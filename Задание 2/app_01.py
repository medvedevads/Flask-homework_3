from flask import Flask, render_template
from models import db, Authors, Books
from random import choice, randint

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///task1.db'
db.init_app(app)

@app.cli.command("init-db")                                                          
def init_db():
    db.create_all()
    print('OK')

@app.cli.command("add-library")
def add_book():
# создаем таблицу авторы
    for j in range(1, 16):
        author = Authors(name=f'name{j}', last_name=f'last_name{j}')
        db.session.add(author)
    db.session.commit()
# создаем таблицу книги
    for i in range(1, 31):
        book = Books(book_name=f'book{i}', date=randint(1995, 2024),  quantity=choice([10, 200, 3_000, 40_000, 500_000]), authors_id=randint(1, 15))
        db.session.add(book)
    db.session.commit()

 
@app.route('/')
def index():
    book = Books.query.all()
    return render_template('index.html', book=book)


if __name__ == '__main__':
    app.run(debug=True)
