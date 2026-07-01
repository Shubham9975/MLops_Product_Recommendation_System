from src.inference.final_recommender import (
    FinalRecommender
)


def test_known_customer():

    recommender = FinalRecommender()

    customer_id = (
        recommender.interactions
        .iloc[0]["customer_unique_id"]
    )

    recommendations = recommender.recommend(
        customer_id,
        top_k=5
    )

    assert len(recommendations) <= 5

    assert "product_id" in recommendations[0]


def test_unknown_customer():

    recommender = FinalRecommender()

    recommendations = recommender.recommend(
        "unknown_customer",
        top_k=5
    )

    assert len(recommendations) == 5

    assert "product_id" in recommendations[0]