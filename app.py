from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

    
    def __repr__(self):
        return f'<User {self.name}>'

@app.route('/')
def index():
    user = User(name='John')
    db.session.add(user)
    db.session.commit()

    user = User.query.filter_by(name='John').first()

    name = user.name

    return 'Hello World !'

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
