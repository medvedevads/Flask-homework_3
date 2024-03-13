from flask import Flask, request, render_template, redirect, url_for
from flask_wtf.csrf import CSRFProtect
from forms import RegistrationForm
from models import db, User


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SECRET_KEY'] = 'supersecretkey'
db.init_app(app)
csrf = CSRFProtect(app)

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(first_name=form.first_name.data,
                    last_name=form.last_name.data,
                    email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('success'))
    return render_template('register.html', form=form)

@app.route('/success')
def success():
    return 'Registration successful!'

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)