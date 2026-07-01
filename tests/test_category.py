from src.inference.category import CategoryRecommender


def test_category_recommendations():

    recommender = CategoryRecommender()

    customer_id = (
        recommender.customer_favorites
        .iloc[0]["customer_unique_id"]
    )

    recommendations = recommender.recommend(
        customer_id=customer_id,
        top_k=5
    )

    assert len(recommendations) <= 5

    if recommendations:

        assert "product_id" in recommendations[0]

        assert "product_category_name" in recommendations[0]