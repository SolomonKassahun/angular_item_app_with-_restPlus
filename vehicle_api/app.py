import re
import unicodedata
from flask import Flask,render_template, url_for, flash, redirect, request, jsonify
from flask_marshmallow import Marshmallow
from flask_restplus import Resource,Api,fields,Namespace, namespace
from sqlalchemy import Table, Column, Integer, String, Float, MetaData, null
from sqlalchemy import true
from werkzeug.utils import cached_property
from flask_cors import CORS
from datetime import datetime



from setting import *
from models import *
from marsh import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS
CORS(app,resources={"/api/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'
#app.config['content-Type'] =  'application/json'

db.init_app(app) # initialize
with app.app_context():
  db.create_all()

marsh = Marshmallow(app)

user_schema = UserSchema()
users_schema = UserSchema(many = true)

admin_schema = AdminSchema()
admins_schema = AdminSchema(many = true)


item_schema = ItemSchema()
items_schema = ItemSchema(many = true)

comment_schema = CommentSchema()
comments_schema = CommentSchema(many = true)


api = Api(app,version="1",title="App Database",description="Vehicle Information")
list_of_names = {}

User = api.model("User",{
    'username':fields.String("username"),
    'password':fields.String("password"),
    'firstName':fields.String("firstName"),
    'lastName':fields.String("lastName"),
    'address':fields.String("address"),
    'phoneNumber':fields.String("phoneNumber"),
    'age':fields.String("age"),
    'zip':fields.String("zip")
})
Admin = api.model("Admin",{
     'username':fields.String("username"),
    'password':fields.String("password")
}

)

Item = api.model("Item",{
     'name':fields.String("name"),
    'description':fields.String("description"),
    'price':fields.String("price")
}
)
Comment = api.model("Comment",{
     'firstName':fields.String("firstName"),
    'lastName':fields.String("lastName"),
    'subject':fields.String("subject"),
    'message':fields.String("message"),

}


)


@api.route("/api/LoginInfo",methods=["GET","POST"])
class LoginResource(Resource):
    def get(self):
        user = LoginInfo.query.all()
        return users_schema.dump(user)
    
    @api.expect(User)
    @api.response(201,"Successfuly created new logedin!")
    def post(self):
        user = LoginInfo()
        #request.get_json()
        print(request)
        user.username = request.json['username']
        user.password = request.json['password']
        user.firstName = request.json['firstName']
        user.lastName = request.json['lastName']
        user.address = request.json['address']
        user.phoneNumber = request.json['phoneNumber']
        user.age = request.json['age']
        user.zip = request.json['zip']

        # if request.json['username'] != null:
        #     user.username = request.json['username']
        # if request.json['password'] != null:
        #     user.password = request.json['password']
        # if request.json['firstName'] != null:
        #     user.firstName = request.json['firstName']
        # if request.json['lastName'] != null:
        #     user.lastName = request.json['lastName']
        # if request.json['address'] != null:
        #     user.address = request.json['address']
        # if request.json['phoneNumber'] != null:
        #     user.phoneNumber = request.json['phoneNumber']
        # if request.json['age'] != null:
        #     user.age = request.json['age']
        # if request.json['zip'] != null:
        #     user.zip = request.json['zip']

        

        db.session.add(user)
        db.session.commit()
        return user_schema.dump(user), 201


@api.route("/api/LoginInfo/<int:id>",methods=["GET","POST","PUT","DELETE"])
class LoginResource(Resource):
    def get(self,id):
        user = LoginInfo.query.filter_by(UserId=id).first()
        return user_schema.dump(user)
    
    @api.expect(User)
    @api.response(204,"Successfuly created new logedin!")
    def put(self,id):
        user = LoginInfo.query.filter_by(UserId=id).first()
        user.username = request.json['username']
        user.password = request.json['password']
        user.firstName = request.json['firstName']
        user.lastName = request.json['lastName']
        user.address = request.json['address']
        user.phoneNumber = request.json['phoneNumber']
        user.age = request.json['age']
        user.zip = request.json['zip']
        db.session.add(user)
        db.session.commit()
        return user_schema.dump(user), 201
    @api.response(204, 'Vehicle deleted.')
    def delete(self, id):
        user = LoginInfo.query.filter_by(UserId=id).first()
        if user is None:
            return None, 404
        db.session.delete(user)
        db.session.commit()
        return None, 204


@api.route("/api/AdminInfo",methods=["GET","POST"])
class LoginResource(Resource):
    def get(self):
        admin = AdminInfo.query.all()
        return admins_schema.dump(admin)
    
    @api.expect(Admin)
    @api.response(201,"Successfuly created new logedin!")
    def post(self):
        admin = AdminInfo()
        admin.username = request.json['username']
        admin.password = request.json['password']

        db.session.add(admin)
        db.session.commit()
        return admin_schema.dump(admin), 201


@api.route("/api/AdminInfo/<int:id>",methods=["GET","POST","PUT","DELETE"])
class LoginResource(Resource):
    def get(self,id):
        admin = AdminInfo.query.filter_by(adminId=id).first()
        return admin_schema.dump(admin)
    
    @api.expect(Admin)
    @api.response(204,"Successfuly created new logedin!")
    def put(self,id):
        user = AdminInfo.query.filter_by(adminId=id).first()
        user.username = request.json['username']
        user.password = request.json['password']
        db.session.add(user)
        db.session.commit()
        return admin_schema.dump(user), 201
    @api.response(204, 'admin deleted.')
    def delete(self, id):
        user = AdminInfo.query.filter_by(adminId=id).first()
        if user is None:
            return None, 404
        db.session.delete(user)
        db.session.commit()
        return None, 204





@api.route("/api/Item",methods=["GET","POST"])
class ItemResource(Resource):
    def get(self):
        user = ItemInfo.query.all()
        return items_schema.dump(user)
    
    @api.expect(Item)
    @api.response(201,"Successfuly created new Item!")
    def post(self):
        user = ItemInfo()
        user.name = request.json['name']
        user.description = request.json['description']
        user.price = request.json['price']
        db.session.add(user)
        db.session.commit()
        return item_schema.dump(user), 201


@api.route("/api/Item/<int:id>",methods=["GET","POST","PUT","DELETE"])
class ItemResource(Resource):
    def get(self,id):
        user = ItemInfo.query.filter_by(itemId=id).first()
        return item_schema.dump(user)
    
    @api.expect(Item)
    @api.response(204,"Successfuly updated item!")
    def put(self,id):
        item = ItemInfo.query.filter_by(itemId=id).first()
        item.name = request.json['name']
        item.description = request.json['description']
        item.price = request.json['price']
        db.session.add(item)
        db.session.commit()
        return item_schema.dump(item), 201
    @api.response(204, 'item deleted.')
    def delete(self, id):
        item = ItemInfo.query.filter_by(itemId=id).first()
        if item is None:
            return None, 404
        db.session.delete(item)
        db.session.commit()
        return None, 204





#comment 
@api.route("/api/Comment",methods=["GET","POST"])
class CommentResource(Resource):
    def get(self):
        comment = CommentInfo.query.all()
        return comments_schema.dump(comment)
    
    @api.expect(Comment)
    @api.response(201,"Successfuly created new Comment!")
    def post(self):
        comment = CommentInfo()
        comment.firstName = request.json['firstName']
        comment.lastName = request.json['lastName']
        comment.subject = request.json['subject']
        comment.message = request.json['message']
        db.session.add(comment)
        db.session.commit()
        return comment_schema.dump(comment), 201


@api.route("/api/Comment/<int:id>",methods=["GET","POST","PUT","DELETE"])
class CommentResource(Resource):
    def get(self,id):
        comment = CommentInfo.query.filter_by(commentId=id).first()
        return comment_schema.dump(comment)
    
    @api.expect(Comment)
    @api.response(204,"Successfuly created Comment!")
    def put(self,id):
        comment = CommentInfo.query.filter_by(commentId=id).first()
        comment.firstName = request.json['firstName']
        comment.lastName = request.json['lastName']
        comment.subject = request.json['subject']
        comment.message = request.json['message']
        
        db.session.add(comment)
        db.session.commit()
        return comment_schema.dump(comment), 201
    @api.response(204, 'Comment.')
    def delete(self, id):
        comment = CommentInfo.query.filter_by(commentId=id).first()
        if comment is None:
            return None, 404
        db.session.delete(comment)
        db.session.commit()
        return None, 204

