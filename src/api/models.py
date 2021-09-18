from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Inbox(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(120), nullable=False)
    sender_id = db.Column(db.Integer(), nullable=False)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))  

    def __repr__(self):
        return '<Inbox %r>' % self.user_id

    def serialize(self):
        return {
            "id": self.id,
            "message": self.message,
            "sender_id": self.sender_id,
            "user_id": self.user_id
        }
    
    def getInbox(id):
        inbox = Inbox.query.filter_by(user_id=id)
        messages = list(map(lambda message: message.serialize, messages))
        return messages

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    price = db.Column(db.String(80), unique=False, nullable=False)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Product %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "user_id": self.user_id
        }

    def create_product(name, price, user_id):
        product = Product(name=name, price=price, user_id=user_id)
        db.session.add(product)
        db.session.commit()
