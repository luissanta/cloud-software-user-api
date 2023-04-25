from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models.database import database
from datetime import datetime


class User(database.Model):
    __tablename__ = 'users'
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String(100), unique=True)
    password = database.Column(database.String(100))
    email = database.Column(database.String(100))
    created_at = database.Column(database.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = database.Column(database.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)


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
