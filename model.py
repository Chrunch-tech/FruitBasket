from . import db


class Products(db.Model):
    __tablename__ = "Products"
    productId = db.Column(db.String(20), primary_key=True)
    productName = db.Column(db.String(20), nullable=False, unique=False)
    stocks = db.Column(db.String(10), nullable=True, unique=False)
    price = db.Column(db.Integer, nullable=False, unique=False)
    description = db.Column(db.String(100), nullable=False, unique=False)
    offer = db.Column(db.String(20), nullable=True, unique=False)
    image_url = db.Column(db.String(255), nullable=False, unique=False)

    def __repr__(self):
        return f"{self.productName}, {self.price}, {self.stocks}"


class Users(db.Model):
    __tablename__ = "Users"
    userId = db.Column(db.String(20), primary_key=True)
    hash_id = db.Column(db.String(60), nullable=False, unique=True)
    username = db.Column(db.String(20), nullable=False, unique=False)
    email = db.Column(db.String(30), nullable=False, unique=True)
    profile_img = db.Column(db.String(60), nullable=False, unique=False)
    password = db.Column(db.String(100), nullable=False, unique=False)

    def __repr__(self):
        return f"{self.username}, {self.userId}"


class Orders(db.Model):
    __tablename__ = 'Orders'
    productId = db.Column(db.String(20), primary_key=True, nullable=False, unique=False)
    productName = db.Column(db.String(20), nullable=False, unique=False)
    productPrice = db.Column(db.Integer, nullable=False, unique=False)
    image_url = db.Column(db.String(255), nullable=False, unique=False)
    quantity = db.Column(db.String(4), nullable=False, unique=False)
    customerName = db.Column(db.String(20), nullable=False, unique=False)
    customerEmail = db.Column(db.String(30), nullable=False, unique=False)

    def __repr__(self):
        return f"{self.productName}, {self.customerName}, {self.productPrice}"


class FeedBacks(db.Model):
    __tablename__ = 'feedback'
    costumerId = db.Column(db.String(20), primary_key=True, unique=False)
    costumerName = db.Column(db.String(20), nullable=False, unique=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    adminResponse = db.Column(db.String(100), nullable=True, unique=False)
    message = db.Column(db.String(150), nullable=True, unique=False)

    def __repr__(self):
        return f"{self.costumerName}, {self.message}, {self.costumerId}"


class AddAdmin(db.Model):
    __tablename__ = 'Owners'
    adminId = db.Column(db.String(60), primary_key=True)
    adminName = db.Column(db.String(7), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False, unique=True)

    def __repr__(self):
        return f'Admin{self.adminId}, {self.password}'
