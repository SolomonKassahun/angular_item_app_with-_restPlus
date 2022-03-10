from audioop import add
from datetime import date, datetime
from email import message
from email.policy import default
from sqlalchemy import Table, Column, Integer, String, Float, MetaData
import imp
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import DateTime
#from app import db

db = SQLAlchemy()


class LoginInfo(db.Model):
      __tablename__ = 'user'
      UserId = db.Column(db.Integer, primary_key=True,autoincrement=True)
      username = db.Column(db.String,nullable=False)
      password = db.Column(db.String,nullable=False)
      firstName = db.Column(db.String,nullable=False)
      lastName = db.Column(db.String,nullable=False)
      address = db.Column(db.String,nullable=False)
      phoneNumber = db.Column(db.String,nullable=False)
      age = db.Column(db.String,nullable=False)
      zip = db.Column(db.String,nullable=False)
      
      
class AdminInfo(db.Model):
      __tablename__ = 'admin'
      adminId = db.Column(db.Integer, primary_key=True,autoincrement=True)
      username = db.Column(db.String,nullable=False)
      password = db.Column(db.String,nullable=False)
class ItemInfo(db.Model):
      __tablename__ = 'item'
      itemId = db.Column(db.Integer, primary_key=True,autoincrement=True)
      name = db.Column(db.String,nullable=False)
      description = db.Column(db.String,nullable=False)
      price = db.Column(db.String,nullable=False)
class CommentInfo(db.Model):
      __tablename__ = 'comment'
      commentId = db.Column(db.Integer, primary_key=True,autoincrement=True)
      firstName = db.Column(db.String,nullable=False)
      lastName = db.Column(db.String,nullable=False)
      subject = db.Column(db.String,nullable=False)
      message = db.Column(db.String,nullable=False)



   





     