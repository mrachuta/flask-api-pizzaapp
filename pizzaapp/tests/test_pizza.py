import json
import unittest
from ..app import create_app, db


class PizzaTest(unittest.TestCase):

    """
    Users Test Case
    """

    def setUp(self):

        self.app = create_app("local")
        self.app.config["TESTING"] = True
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()

    def test_create_pizza(self):

        res_one = self.client.post(
            "/api/v1/pizza/",
            headers={"Content-Type": "application/json"},
            data=json.dumps({"name": "test-pizza", "price": "22.83"}),
        )
        self.assertEqual(res_one.status_code, 201)

    def test_create_pizza_duplicate_name(self):

        res_one = self.client.post(
            "/api/v1/pizza/",
            headers={"Content-Type": "application/json"},
            data=json.dumps({"name": "test-pizza", "price": "22.83"}),
        )
        self.assertEqual(res_one.status_code, 201)

        res_two = self.client.post(
            "/api/v1/pizza/",
            headers={"Content-Type": "application/json"},
            data=json.dumps({"name": "test-pizza", "price": "22.83"}),
        )
        self.assertEqual(res_two.status_code, 400)

    def test_create_pizza_blank_name(self):

        res_one = self.client.post(
            "/api/v1/pizza/",
            headers={"Content-Type": "application/json"},
            data=json.dumps({"price": "22.83"}),
        )
        self.assertEqual(res_one.status_code, 400)

    def test_create_pizza_blank_price(self):

        res_one = self.client.post(
            "/api/v1/pizza/",
            headers={"Content-Type": "application/json"},
            data=json.dumps({"name": "test-pizza"}),
        )
        self.assertEqual(res_one.status_code, 400)

    def test_create_pizza_price_as_str(self):

        res_one = self.client.post(
            "/api/v1/pizza/",
            headers={"Content-Type": "application/json"},
            data=json.dumps({"name": "test-pizza", "price": "test-price"}),
        )
        self.assertEqual(res_one.status_code, 400)

    def test_get_all_pizzas(self):

        res_one = self.client.post(
            "/api/v1/pizza/",
            headers={"Content-Type": "application/json"},
            data=json.dumps({"name": "test-pizza", "price": "22.83"}),
        )
        self.assertEqual(res_one.status_code, 201)

        res_two = self.client.post(
            "/api/v1/pizza/",
            headers={"Content-Type": "application/json"},
            data=json.dumps({"name": "next-test-pizza", "price": "29.99"}),
        )
        self.assertEqual(res_two.status_code, 201)

        res_three = self.client.get("/api/v1/pizza/")
        self.assertEqual(res_three.status_code, 200)
        # Response from this view is serialized data
        # Each entry as separate list
        self.assertEqual(res_three.json[0].get("name"), "test-pizza")
        self.assertEqual(res_three.json[1].get("name"), "next-test-pizza")

    def test_update_pizza(self):

        res_one = self.client.post(
            "/api/v1/pizza/",
            headers={"Content-Type": "application/json"},
            data=json.dumps({"name": "test-pizza", "price": "22.83"}),
        )
        self.assertEqual(res_one.status_code, 201)
        created_pizza_id = res_one.json.get("id")

        res_two = self.client.patch(
            f"/api/v1/pizza/{created_pizza_id}",
            headers={"Content-Type": "application/json"},
            data=json.dumps({"name": "modified-test-pizza", "price": "25.12"}),
        )
        self.assertEqual(res_two.status_code, 200)
        self.assertEqual(res_two.json.get("id"), created_pizza_id)

    def test_update_non_existing_pizza(self):

        res_one = self.client.patch(
            "/api/v1/pizza/1",
            headers={"Content-Type": "application/json"},
            data=json.dumps({"name": "modified-test-pizza", "price": "25.12"}),
        )
        self.assertEqual(res_one.status_code, 404)

    def test_update_pizza_duplicate_name(self):

        res_one = self.client.post(
            "/api/v1/pizza/",
            headers={"Content-Type": "application/json"},
            data=json.dumps({"name": "test-pizza", "price": "22.83"}),
        )
        self.assertEqual(res_one.status_code, 201)
        created_pizza_id = res_one.json.get("id")

        res_two = self.client.post(
            "/api/v1/pizza/",
            headers={"Content-Type": "application/json"},
            data=json.dumps({"name": "next-test-pizza", "price": "29.99"}),
        )
        self.assertEqual(res_two.status_code, 201)

        res_three = self.client.patch(
            f"/api/v1/pizza/{created_pizza_id}",
            headers={"Content-Type": "application/json"},
            data=json.dumps({"name": "next-test-pizza", "price": "22.83"}),
        )
        self.assertEqual(res_three.status_code, 400)

    def test_update_pizza_blank_name(self):

        res_one = self.client.post(
            "/api/v1/pizza/",
            headers={"Content-Type": "application/json"},
            data=json.dumps({"name": "test-pizza", "price": "22.83"}),
        )
        self.assertEqual(res_one.status_code, 201)
        created_pizza_id = res_one.json.get("id")

        res_two = self.client.patch(
            f"/api/v1/pizza/{created_pizza_id}",
            headers={"Content-Type": "application/json"},
            data=json.dumps({"name": "", "price": "29.99"}),
        )
        self.assertEqual(res_two.status_code, 400)

    def test_delete_pizza(self):

        res_one = self.client.post(
            "/api/v1/pizza/",
            headers={"Content-Type": "application/json"},
            data=json.dumps({"name": "test-pizza", "price": "22.83"}),
        )
        self.assertEqual(res_one.status_code, 201)
        created_pizza_id = res_one.json.get("id")

        res_two = self.client.delete(
            f"/api/v1/pizza/{created_pizza_id}",
            headers={"Content-Type": "application/json"},
            data=json.dumps({"name": "test-pizza", "price": "22.83"}),
        )
        self.assertEqual(res_two.status_code, 200)

    def test_delete_non_existing_pizza(self):

        res_two = self.client.delete(
            "/api/v1/pizza/1",
            headers={"Content-Type": "application/json"},
            data=json.dumps({"name": "test-pizza", "price": "22.83"}),
        )
        self.assertEqual(res_two.status_code, 404)

    def tearDown(self):

        """
        Tear Down
        """

        with self.app.app_context():
            db.session.remove()
            db.drop_all()


if __name__ == "__main__":
    unittest.main()
