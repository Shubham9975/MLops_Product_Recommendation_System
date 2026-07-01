from functools import lru_cache
from pathlib import Path

import pandas as pd


ARTIFACTS_DIR = Path(__file__).resolve().parents[2] / "artifacts"


@lru_cache(maxsize=1)
def load_category_popularity():

    return pd.read_parquet(
        ARTIFACTS_DIR / "category_popularity.parquet"
    )


@lru_cache(maxsize=1)
def load_customer_favorites():

    df = pd.read_parquet(
        ARTIFACTS_DIR / "customer_favorite_category.parquet"
    )

    return df.rename(
        columns={
            "product_category_name":
            "favorite_category"
        }
    )


class CategoryRecommender:

    def __init__(self):

        self.category_popularity = load_category_popularity()

        self.customer_favorites = load_customer_favorites()

    def recommend(
        self,
        customer_id: str,
        top_k: int = 10
    ) -> list[dict]:

        customer_row = self.customer_favorites[
            self.customer_favorites["customer_unique_id"] == customer_id
        ]

        if customer_row.empty:
            return []

        favorite_category = customer_row.iloc[0]["favorite_category"]

        recommendations = (
            self.category_popularity[
                self.category_popularity["product_category_name"]
                == favorite_category
            ]
            .head(top_k)
            .copy()
        )

        return recommendations.to_dict(
            orient="records"
        )