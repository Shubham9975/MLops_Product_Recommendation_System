from src.inference.content import ContentRecommender


def test_content_recommendations():

    recommender = ContentRecommender()

    product_id = (
        recommender.product_features
        .iloc[0]["product_id"]
    )

    recommendations = recommender.recommend(
        product_id=product_id,
        top_k=5
    )

    assert len(recommendations) == 5

    assert "product_id" in recommendations[0]

    assert "product_category_name" in recommendations[0]

    assert "similarity_score" in recommendations[0]