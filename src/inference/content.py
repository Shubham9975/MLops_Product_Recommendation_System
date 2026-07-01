from functools import lru_cache
from pathlib import Path

import joblib
import numpy as np
import pandas as pd


ARTIFACTS_DIR = Path(__file__).resolve().parents[2] / "artifacts"


@lru_cache(maxsize=1)
def load_nn_model():

    return joblib.load(
        ARTIFACTS_DIR / "content_based_nn_model.pkl"
    )


@lru_cache(maxsize=1)
def load_feature_matrix():

    return np.load(
        ARTIFACTS_DIR / "product_feature_matrix.npy"
    )


@lru_cache(maxsize=1)
def load_product_features():

    return pd.read_parquet(
        ARTIFACTS_DIR / "product_features.parquet"
    )


@lru_cache(maxsize=1)
def load_product_id_to_index():

    return joblib.load(
        ARTIFACTS_DIR / "product_id_to_index.pkl"
    )


@lru_cache(maxsize=1)
def load_index_to_product_id():

    return joblib.load(
        ARTIFACTS_DIR / "index_to_product_id.pkl"
    )


class ContentRecommender:

    def __init__(self):

        self.nn_model = load_nn_model()

        self.feature_matrix = load_feature_matrix()

        self.product_features = load_product_features()

        self.product_id_to_index = load_product_id_to_index()

        self.index_to_product_id = load_index_to_product_id()

    def recommend(
        self,
        product_id: str,
        top_k: int = 10
    ) -> list[dict]:

        if product_id not in self.product_id_to_index:
            return []

        product_index = self.product_id_to_index[product_id]

        distances, indices = self.nn_model.kneighbors(
            self.feature_matrix[product_index].reshape(1, -1),
            n_neighbors=top_k + 1
        )

        recommendations = []

        for distance, index in zip(
            distances[0][1:],
            indices[0][1:]
        ):

            similar_product_id = self.index_to_product_id[index]

            product_row = self.product_features[
                self.product_features["product_id"]
                == similar_product_id
            ].iloc[0]

            recommendations.append(
                {
                    "product_id": similar_product_id,
                    "product_category_name": product_row[
                        "product_category_name"
                    ],
                    "similarity_score": float(
                        1 - distance
                    )
                }
            )

        return recommendations