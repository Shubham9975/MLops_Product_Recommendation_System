from functools import lru_cache

from src.inference.popularity import PopularityRecommender
from src.inference.category import CategoryRecommender
from src.inference.content import ContentRecommender
from src.inference.hybrid import HybridRecommender
from src.inference.final_recommender import FinalRecommender


@lru_cache(maxsize=1)
def get_popularity_recommender():

    return PopularityRecommender()


@lru_cache(maxsize=1)
def get_category_recommender():

    return CategoryRecommender()


@lru_cache(maxsize=1)
def get_content_recommender():

    return ContentRecommender()


@lru_cache(maxsize=1)
def get_hybrid_recommender():

    return HybridRecommender()


@lru_cache(maxsize=1)
def get_final_recommender():

    return FinalRecommender()