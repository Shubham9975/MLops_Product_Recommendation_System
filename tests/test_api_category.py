from fastapi.testclient import TestClient

from api.main import app
from src.inference.category import CategoryRecommender


client = TestClient(app)


def test_category_endpoint():

    recommender = CategoryRecommender()

    customer_id = (
        recommender.customer_favorites
        .iloc[0]["customer_unique_id"]
    )

    response = client.get(
        f"/recommend/category/{customer_id}?top_k=5"
    )

    assert response.status_code == 200

    data = response.json()

    assert len(
        data["recommendations"]
    ) <= 5

    if data["recommendations"]:

        assert (
            "product_id"
            in data["recommendations"][0]
        )