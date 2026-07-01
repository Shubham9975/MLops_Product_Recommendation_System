from src.inference.lambdamart import (
    LambdaMARTRecommender
)


def test_lambdamart_recommendations():

    recommender = LambdaMARTRecommender()

    recommendations = recommender.recommend(
        customer_total_spend=150.0,
        customer_purchase_count=2,
        favorite_category="informatica_acessorios",
        top_k=5
    )

    assert len(recommendations) == 5

    assert "product_id" in recommendations[0]

    assert "product_category_name" in recommendations[0]

    assert "score" in recommendations[0]