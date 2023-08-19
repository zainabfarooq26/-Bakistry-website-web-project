from .db import  db

class Order(db.Document):
    email = db.StringField()
    order = db.DictField()
class User(db.Document):
    Name = db.StringField(required=True)
    Email=db.StringField(required=True)
    Password=db.StringField(required=True)
class Message(db.Document):
    m_Name = db.StringField(required=True)
    m_Email=db.StringField(required=True)
    m_Subject=db.StringField(required=True)
    m_Message=db.StringField(required=True)
class Payment(db.Document):
    full_Name = db.StringField(required=True)
    user_Email=db.StringField(required=True)
    card_Number=db.StringField(required=True)
    user_Address=db.StringField(required=True)
    amount=db.FloatField(required=True)
class brdy_cake(db.Document):
    Name = db.StringField(required=True)
    Price=db.IntField(required=True)
    Quantity=db.IntField(required=True)
    Description=db.StringField(required=True)
class wed_cake(db.Document):
    Name = db.StringField(required=True)
    Price=db.IntField(required=True)
    Quantity=db.IntField(required=True)
    Description=db.StringField(required=True)
class cust_cake(db.Document):
    Name = db.StringField(required=True)
    Price=db.IntField(required=True)
    Quantity=db.IntField(required=True)
    Description=db.StringField(required=True)
class orderCust(db.Document):
    Name = db.StringField(required=True)
    Price=db.IntField(required=True)
class orderBrdy(db.Document):
    Name = db.StringField(required=True)
    Price=db.IntField(required=True)
class orderWed(db.Document):
    Name = db.StringField(required=True)
    Price=db.IntField(required=True)
class masterChef(db.Document):
    m_Name = db.StringField(required=True)
    m_Speciality=db.StringField(required=True)
    m_Email=db.StringField(required=True)
    m_Experience=db.StringField(required=True)
class getCartInfo(db.Document):
    cart_id = db.StringField(required=True, unique=True)
    items = db.ListField(db.StringField())
    total_price = db.DecimalField(required=True)


