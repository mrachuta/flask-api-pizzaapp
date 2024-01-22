"""
This is a definiton of available views
"""

from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError
from flask import request, json, Response, Blueprint
from ..models.pizza_model import PizzaModel, PizzaSchema

pizza_api = Blueprint("pizza", __name__)
pizza_schema = PizzaSchema()

already_exists_msg = 'Pizza with this name already exists'
not_exists_msg = 'Pizza with this id does not exists'
blank_field_msg = 'Name and/or price can\'t be blank'


@pizza_api.route("/", methods=["POST"])
def create_pizza():
    """
    Create a Pizza
    """

    req_data = request.get_json()

    try:
        data = pizza_schema.load(req_data)

        pizza = PizzaModel(data)
        pizza.save()

    except ValidationError:
        message = {"error": blank_field_msg}
        return custom_response(message, 400)

    except IntegrityError:
        message = {"error": already_exists_msg}
        return custom_response(message, 400)

    message = {"message": "Pizza created", "id": pizza.id}
    return custom_response(message, 201)


@pizza_api.route("/", methods=["GET"])
def get_all_pizzas():
    """
    Get all pizzas
    """

    pizzas = PizzaModel.get_all_pizzas()

    if pizzas:
        serialized_pizzas = pizza_schema.dump(pizzas, many=True)
        return custom_response(serialized_pizzas, 200)

    message = {"error": "No pizzas were found"}
    return custom_response(message, 404)


@pizza_api.route("/<int:pizza_id>", methods=["GET"])
def get_single_pizza(pizza_id):
    """
    Get a single pizza
    """

    pizza = PizzaModel.get_pizza_by_id(pizza_id)

    if not pizza:
        message = {"error": not_exists_msg}
        return custom_response(message, 404)

    serialized_pizza = pizza_schema.dump(pizza)

    return custom_response(serialized_pizza, 200)


@pizza_api.route("/<int:pizza_id>", methods=["PATCH"])
def update_pizza(pizza_id):
    """
    Update a pizza
    """

    req_data = request.get_json()

    try:
        data = pizza_schema.load(req_data)
        pizza = PizzaModel.get_pizza_by_id(pizza_id)
        pizza.update(data)

    except ValidationError:
        message = {"error": blank_field_msg}
        return custom_response(message, 400)

    except IntegrityError:
        message = {"error": already_exists_msg}
        return custom_response(message, 400)

    except AttributeError:
        message = {"error": not_exists_msg}
        return custom_response(message, 404)

    message = {"message": "Pizza updated", "id": pizza.id}
    # In case of response 204, message is not displayed
    return custom_response(message, 200)


@pizza_api.route("/<int:pizza_id>", methods=["DELETE"])
def delete_pizza(pizza_id):
    """
    Delete a pizza
    """

    try:
        pizza = PizzaModel.get_pizza_by_id(pizza_id)
        pizza.delete()

    except AttributeError:
        message = {"error": not_exists_msg}
        return custom_response(message, 404)

    message = {"message": "Pizza deleted", "id": pizza.id}
    # In case of response 204, message is not displayed
    return custom_response(message, 200)


def custom_response(res, status_code):
    """
    Custom Response
    """

    return Response(
        mimetype="application/json", response=json.dumps(res), status=status_code
    )
