from fastapi.testclient import TestClient

from api.main import app
from src.inference.content import ContentRecommender


client = TestClient(app)


def test_hybrid_endpoint():

    recommender = ContentRecommender()

    product_id = (
        recommender.product_features
        .iloc[0]["product_id"]
    )

    response = client.get(
        f"/recommend/hybrid/{product_id}?top_k=5"
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

    assert (
        "hybrid_score"
        in data["recommendations"][0]
    )

    assert (
        "similarity_score"
        in data["recommendations"][0]
    )

    assert (
        "popularity_score"
        in data["recommendations"][0]
    )