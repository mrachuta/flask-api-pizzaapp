import datetime
from . import db
from marshmallow import fields, Schema, ValidationError

# Found on SO
# https://marshmallow.readthedocs.io/en/3.0/examples.html


def must_not_be_blank(data):
    if not data:
        raise ValidationError("This filed cannot be blank")


class PizzaModel(db.Model):

    """
    Pizza Model
    """

    # Table name
    __tablename__ = "pizza"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False, unique=True)
    price = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime)
    modified_at = db.Column(db.DateTime)

    # Class constructor
    def __init__(self, data):

        """
        Class constructor
        """

        self.name = data.get("name")
        self.price = data.get("price")
        self.ingeridients = data.get("ingeridients")
        self.created_at = datetime.datetime.utcnow()
        self.modified_at = datetime.datetime.utcnow()

    @staticmethod
    def get_all_pizzas():
        return PizzaModel.query.all()

    @staticmethod
    def get_pizza_by_id(id):
        return PizzaModel.query.get(id)

    # Not necessary yet
    # @staticmethod
    # def get_pizza_by_name(name):
    #     return PizzaModel.query.filter_by(name=name)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        for key, item in data.items():
            setattr(self, key, item)
        self.modified_at = datetime.datetime.utcnow()
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr(self):
        return "<name {}>".format(self.name)


class PizzaSchema(Schema):

    """
    Pizza Schema
    """

    id = fields.Int(dump_only=True)
    # Validation here
    name = fields.Str(required=True, unique=True, validate=must_not_be_blank)
    price = fields.Float(required=True, validate=must_not_be_blank)
    created_at = fields.DateTime(dump_only=True)
    modified_at = fields.DateTime(dump_only=True)
