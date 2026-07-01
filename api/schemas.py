from pydantic import BaseModel


class RecommendationItem(BaseModel):

    product_id: str

    product_category_name: str | None = None

    score: float | None = None

    popularity_score: float | None = None

    similarity_score: float | None = None

    hybrid_score: float | None = None


class RecommendationResponse(BaseModel):

    recommendations: list[RecommendationItem]


class HealthResponse(BaseModel):

    status: str