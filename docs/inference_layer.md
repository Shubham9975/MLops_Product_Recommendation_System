# Inference Layer Design

# Overview

The project follows a strict separation between:

```text
Training
↓
Artifacts
↓
Inference
↓
API
```

Training notebooks produce artifacts that are later consumed by lightweight inference modules.

This enables:

- Faster deployment
- Independent testing
- Better maintainability
- MLOps compatibility
- Reproducible serving pipelines

---

# Architecture

```text
Client
↓
FastAPI
↓
FinalRecommender
↓
LambdaMART / Hybrid / Popularity
↓
Artifacts
```

---

# popularity.py

## Objective

Recommend globally popular products.

## Input

```python
recommend(top_k=10)
```

## Output

```python
[
    {
        "product_id": "...",
        "purchase_count": 522,
        "popularity_score": 1.0
    }
]
```

## Artifacts

```text
popularity_recommender.parquet
```

## Use Cases

- Cold-start users
- Anonymous users
- Fallback recommendations

---

# category.py

## Objective

Recommend products from a customer's favorite category.

## Input

```python
recommend(customer_id, top_k=10)
```

## Pipeline

```text
customer_id
↓
customer_favorite_category.parquet
↓
favorite category
↓
category_popularity.parquet
↓
Top-K recommendations
```

## Artifacts

```text
customer_favorite_category.parquet
category_popularity.parquet
```

---

# content.py

## Objective

Recommend similar products.

## Input

```python
recommend(product_id, top_k=10)
```

## Pipeline

```text
product_id
↓
product_id_to_index.pkl
↓
NearestNeighbors model
↓
Feature matrix
↓
Similar products
```

## Features Used

```text
product_category_name
product_weight_g
product_length_cm
product_height_cm
product_width_cm
```

## Artifacts

```text
content_based_nn_model.pkl
product_feature_matrix.npy
product_features.parquet
product_id_to_index.pkl
index_to_product_id.pkl
```

---

# hybrid.py

## Objective

Combine content similarity and popularity.

## Formula

```python
hybrid_score = (
    similarity_weight * similarity_score
    +
    popularity_weight * popularity_score
)
```

## Configuration

```text
similarity_weight = 0.7
popularity_weight = 0.3
candidate_pool_size = 50
```

## Pipeline

```text
Product
↓
Content Recommendations
↓
Popularity Merge
↓
Weighted Scoring
↓
Top-K
```

## Artifacts

```text
hybrid_config.pkl
```

---

# lambdamart.py

## Objective

Generate personalized recommendations using LightGBM LambdaMART.

## Input

```python
recommend(
    customer_total_spend,
    customer_purchase_count,
    favorite_category
)
```

## Features

```text
customer_total_spend
customer_purchase_count

product_weight_g
product_length_cm
product_height_cm
product_width_cm

popularity_score

is_favorite_category_match
```

## Pipeline

```text
Customer Features
↓
Candidate Products
↓
Feature Construction
↓
LightGBM Ranker
↓
Top-K Recommendations
```

## Characteristics

```text
Pure ML inference.

No databases.
No APIs.
No business logic.
No customer IDs.
```

---

# final_recommender.py

## Objective

Production orchestration layer.

## Input

```python
recommend(customer_id, top_k=10)
```

---

## Known Customer

```text
customer_id
↓
Historical interactions
↓
Customer features
↓
LambdaMART
↓
Diversification
↓
Top-K
```

---

## Unknown Customer

```text
customer_id
↓
Popularity fallback
↓
Top-K
```

---

## Diversification Strategy

```text
Maximum:
3 products per category
```

Purpose:

- Prevent category domination
- Improve exploration
- Increase recommendation variety

---

# Design Principles

The inference layer follows:

```text
Single Responsibility Principle
```

Each file has exactly one responsibility:

```text
popularity.py
→ Global recommendations

category.py
→ Category recommendations

content.py
→ Similar products

hybrid.py
→ Hybrid recommendations

lambdamart.py
→ ML ranking

final_recommender.py
→ Business orchestration
```

---

# Testing

Implemented tests:

```text
test_popularity.py
test_category.py
test_content.py
test_hybrid.py
test_lambdamart.py
test_final_recommender.py
```

Current status:

```text
All tests passing.
```
