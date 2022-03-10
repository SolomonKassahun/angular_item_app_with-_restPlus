from flask_marshmallow import Marshmallow
from models import *

marsh = Marshmallow()

class UserSchema(marsh.Schema):
    class Meta:
        fields=("UserId","username","password","firstName","lastName","address","phoneNumber","age","zip")
        model = LoginInfo
class AdminSchema(marsh.Schema):
    class Meta:
        fields=("adminId","username","password")
        model = AdminInfo
class ItemSchema(marsh.Schema):
    class Meta:
        fields=("itemId","name","description", "price")
        model = ItemInfo
class CommentSchema(marsh.Schema):
    class Meta:
        fields=("commentId","firstName","lastName", "subject","message")
        model = ItemInfo

