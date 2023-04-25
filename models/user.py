from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models.database import database


class User(database.Model):
    __tablename__ = 'users'
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String(100), unique=True)
    password = database.Column(database.String(100))
    email = database.Column(database.String(100))


class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        include_relationships = True
        include_fk = True
        load_instance = True

    id = fields.String()
    username = fields.String()
    password = fields.String()
    email = fields.String()
