from functools import lru_cache
from pathlib import Path

import joblib
import pandas as pd


ARTIFACTS_DIR = Path(__file__).resolve().parents[2] / "artifacts"


@lru_cache(maxsize=1)
def load_ranker():

    return joblib.load(
        ARTIFACTS_DIR / "final_ranker.pkl"
    )


@lru_cache(maxsize=1)
def load_feature_columns():

    return joblib.load(
        ARTIFACTS_DIR / "final_ranker_features.pkl"
    )


@lru_cache(maxsize=1)
def load_product_features():

    return pd.read_parquet(
        ARTIFACTS_DIR / "product_features.parquet"
    )


@lru_cache(maxsize=1)
def load_popularity():

    return pd.read_parquet(
        ARTIFACTS_DIR / "popularity_recommender.parquet"
    )[
        ["product_id", "popularity_score"]
    ]


class LambdaMARTRecommender:

    def __init__(self):

        self.ranker = load_ranker()

        self.feature_columns = load_feature_columns()

        self.product_features = load_product_features()

        self.popularity_df = load_popularity()

        self.products = (
            self.product_features
            .merge(
                self.popularity_df,
                on="product_id",
                how="left"
            )
        )

        self.products["popularity_score"] = (
            self.products["popularity_score"]
            .fillna(0)
        )

    def recommend(
        self,
        customer_total_spend: float,
        customer_purchase_count: int,
        favorite_category: str,
        top_k: int = 10
    ) -> list[dict]:

        candidates = self.products.copy()

        candidates[
            "customer_total_spend"
        ] = customer_total_spend

        candidates[
            "customer_purchase_count"
        ] = customer_purchase_count

        candidates[
            "is_favorite_category_match"
        ] = (
            candidates["product_category_name"]
            == favorite_category
        ).astype(int)

        X = candidates[self.feature_columns]

        candidates["score"] = self.ranker.predict(X)

        recommendations = (
            candidates
            .sort_values(
                "score",
                ascending=False
            )
            .head(top_k)
        )

        return recommendations[
            [
                "product_id",
                "product_category_name",
                "score"
            ]
        ].to_dict(orient="records")