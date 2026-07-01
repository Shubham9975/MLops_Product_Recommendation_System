from src.inference.hybrid import HybridRecommender


def test_hybrid_recommendations():

    recommender = HybridRecommender()

    product_id = (
        recommender
        .content_recommender
        .product_features
        .iloc[0]["product_id"]
    )

    recommendations = recommender.recommend(
        product_id=product_id,
        top_k=5
    )

    assert len(recommendations) == 5

    assert "product_id" in recommendations[0]

    assert "similarity_score" in recommendations[0]

    assert "popularity_score" in recommendations[0]

    assert "hybrid_score" in recommendations[0]