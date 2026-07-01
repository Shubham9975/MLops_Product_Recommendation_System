from functools import lru_cache
from pathlib import Path

import pandas as pd

from src.inference.lambdamart import LambdaMARTRecommender
from src.inference.popularity import PopularityRecommender


BASE_DIR = Path(__file__).resolve().parents[2]


@lru_cache(maxsize=1)
def load_interactions():

    return pd.read_parquet(
        BASE_DIR / "data/processed/model_df.parquet"
    )


class FinalRecommender:

    def __init__(self):

        self.interactions = load_interactions()

        self.lambdamart = LambdaMARTRecommender()

        self.popularity = PopularityRecommender()

    def _get_customer_features(
        self,
        customer_id: str
    ):

        customer_df = self.interactions[
            self.interactions["customer_unique_id"]
            == customer_id
        ]

        if customer_df.empty:
            return None

        customer_total_spend = customer_df[
            "price"
        ].sum()

        customer_purchase_count = len(customer_df)

        favorite_category = (
            customer_df["product_category_name"]
            .value_counts()
            .index[0]
        )

        return {
            "customer_total_spend": customer_total_spend,
            "customer_purchase_count": customer_purchase_count,
            "favorite_category": favorite_category
        }

    def _diversify(
        self,
        recommendations: list[dict],
        top_k: int,
        max_per_category: int = 3
    ) -> list[dict]:

        selected = []

        category_counts = {}

        for recommendation in recommendations:

            category = recommendation[
                "product_category_name"
            ]

            current_count = category_counts.get(
                category,
                0
            )

            if current_count < max_per_category:

                selected.append(
                    recommendation
                )

                category_counts[
                    category
                ] = current_count + 1

            if len(selected) == top_k:
                break

        return selected

    def recommend(
        self,
        customer_id: str,
        top_k: int = 10
    ) -> list[dict]:

        customer_features = self._get_customer_features(
            customer_id
        )

        # Cold start
        if customer_features is None:

            return self.popularity.recommend(
                top_k=top_k
            )

        recommendations = self.lambdamart.recommend(
            customer_total_spend=customer_features[
                "customer_total_spend"
            ],
            customer_purchase_count=customer_features[
                "customer_purchase_count"
            ],
            favorite_category=customer_features[
                "favorite_category"
            ],
            top_k=50
        )

        recommendations = self._diversify(
            recommendations,
            top_k=top_k
        )

        return recommendations