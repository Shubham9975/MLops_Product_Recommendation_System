from src.inference.popularity import PopularityRecommender


def test_popularity_recommendations():

    recommender = PopularityRecommender()

    recommendations = recommender.recommend(
        top_k=5
    )

    assert len(recommendations) == 5

    assert "product_id" in recommendations[0]

    assert "popularity_score" in recommendations[0]