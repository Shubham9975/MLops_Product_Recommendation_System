import pandas as pd


class PopularityRecommender:

    def __init__(self, recommendations_df):
        self.recommendations_df = recommendations_df

    def recommend(
        self,
        customer_id=None,
        top_k=10
    ):
        return (
            self.recommendations_df
            .head(top_k)
        )