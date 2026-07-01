from fastapi.testclient import TestClient

from api.main import app


client = TestClient(app)


def test_popularity_endpoint():

    response = client.get(
        "/recommend/popularity?top_k=5"
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