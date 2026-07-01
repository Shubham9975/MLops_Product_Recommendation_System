from functools import lru_cache
from pathlib import Path

import joblib
import pandas as pd

from src.inference.content import ContentRecommender
from src.inference.popularity import PopularityRecommender


ARTIFACTS_DIR = Path(__file__).resolve().parents[2] / "artifacts"


@lru_cache(maxsize=1)
def load_hybrid_config():

    return joblib.load(
        ARTIFACTS_DIR / "hybrid_config.pkl"
    )


class HybridRecommender:

    def __init__(self):

        self.config = load_hybrid_config()

        self.content_recommender = ContentRecommender()

        self.popularity_recommender = PopularityRecommender()

        self.similarity_weight = self.config[
            "similarity_weight"
        ]

        self.popularity_weight = self.config[
            "popularity_weight"
        ]

        self.candidate_pool_size = self.config[
            "candidate_pool_size"
        ]

    def recommend(
        self,
        product_id: str,
        top_k: int = 10
    ) -> list[dict]:

        content_recommendations = (
            self.content_recommender.recommend(
                product_id=product_id,
                top_k=self.candidate_pool_size
            )
        )

        if not content_recommendations:
            return []

        popularity_df = pd.DataFrame(
            self.popularity_recommender.popularity_df
        )[
            [
                "product_id",
                "popularity_score"
            ]
        ]

        content_df = pd.DataFrame(
            content_recommendations
        )

        hybrid_df = content_df.merge(
            popularity_df,
            on="product_id",
            how="left"
        )

        hybrid_df["popularity_score"] = (
            hybrid_df["popularity_score"]
            .fillna(0)
        )

        hybrid_df["hybrid_score"] = (
            self.similarity_weight
            * hybrid_df["similarity_score"]
            +
            self.popularity_weight
            * hybrid_df["popularity_score"]
        )

        hybrid_df = hybrid_df.sort_values(
            "hybrid_score",
            ascending=False
        )

        return (
            hybrid_df
            .head(top_k)
            .to_dict(orient="records")
        )