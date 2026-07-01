from functools import lru_cache
from pathlib import Path

import pandas as pd


ARTIFACTS_DIR = Path(__file__).resolve().parents[2] / "artifacts"


@lru_cache(maxsize=1)
def load_popularity_data():

    return pd.read_parquet(
        ARTIFACTS_DIR / "popularity_recommender.parquet"
    )


class PopularityRecommender:

    def __init__(self):

        self.popularity_df = load_popularity_data()

    def recommend(
        self,
        top_k: int = 10
    ) -> list[dict]:

        recommendations = (
            self.popularity_df
            .head(top_k)
            .copy()
        )

        return recommendations.to_dict(
            orient="records"
        )