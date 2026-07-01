from fastapi import APIRouter
from api.schemas import HealthResponse

from fastapi import APIRouter, Depends
from api.dependencies import (
    get_popularity_recommender,
    get_category_recommender,
    get_content_recommender,
    get_hybrid_recommender,
    get_final_recommender
)
from api.schemas import (
    HealthResponse,
    RecommendationResponse
)

from src.inference.popularity import PopularityRecommender
from src.inference.category import CategoryRecommender
from src.inference.content import ContentRecommender
from src.inference.hybrid import HybridRecommender
from src.inference.final_recommender import FinalRecommender

router = APIRouter()


@router.get(
    "/health",
    response_model=HealthResponse
)
def health():

    return {
        "status": "healthy"
    }


@router.get(
    "/recommend/popularity",
    response_model=RecommendationResponse
)
def recommend_popularity(
    top_k: int = 10,
    recommender: PopularityRecommender = Depends(
        get_popularity_recommender
    )
):

    recommendations = recommender.recommend(
        top_k=top_k
    )

    return {
        "recommendations": recommendations
    }


@router.get(
    "/recommend/category/{customer_id}",
    response_model=RecommendationResponse
)
def recommend_category(
    customer_id: str,
    top_k: int = 10,
    recommender: CategoryRecommender = Depends(
        get_category_recommender
    )
):

    recommendations = recommender.recommend(
        customer_id=customer_id,
        top_k=top_k
    )

    return {
        "recommendations": recommendations
    }


@router.get(
    "/recommend/content/{product_id}",
    response_model=RecommendationResponse
)
def recommend_content(
    product_id: str,
    top_k: int = 10,
    recommender: ContentRecommender = Depends(
        get_content_recommender
    )
):

    recommendations = recommender.recommend(
        product_id=product_id,
        top_k=top_k
    )

    return {
        "recommendations": recommendations
    }


@router.get(
    "/recommend/hybrid/{product_id}",
    response_model=RecommendationResponse
)
def recommend_hybrid(
    product_id: str,
    top_k: int = 10,
    recommender: HybridRecommender = Depends(
        get_hybrid_recommender
    )
):

    recommendations = recommender.recommend(
        product_id=product_id,
        top_k=top_k
    )

    return {
        "recommendations": recommendations
    }


@router.get(
    "/recommend/final/{customer_id}",
    response_model=RecommendationResponse
)
def recommend_final(
    customer_id: str,
    top_k: int = 10,
    recommender: FinalRecommender = Depends(
        get_final_recommender
    )
):

    recommendations = recommender.recommend(
        customer_id=customer_id,
        top_k=top_k
    )

    return {
        "recommendations": recommendations
    }