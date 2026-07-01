from fastapi.testclient import TestClient

from api.main import app
from src.inference.final_recommender import (
    FinalRecommender
)


client = TestClient(app)


def test_final_known_customer():

    recommender = FinalRecommender()

    customer_id = (
        recommender.interactions
        .iloc[0]["customer_unique_id"]
    )

    response = client.get(
        f"/recommend/final/{customer_id}?top_k=5"
    )

    assert response.status_code == 200

    data = response.json()

    assert len(
        data["recommendations"]
    ) <= 5

    assert (
        "product_id"
        in data["recommendations"][0]
    )


def test_final_unknown_customer():

    response = client.get(
        "/recommend/final/unknown_customer?top_k=5"
    )

    assert response.status_code == 200

    data = response.json()

    assert len(
        data["recommendations"]
    ) == 5

    assert (
        "product_id"
        in data["recommendations"][0]
    )