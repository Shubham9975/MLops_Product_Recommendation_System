# Olist E-Commerce Recommendation System

An end-to-end recommendation system built on the Olist Brazilian E-Commerce dataset, covering data analysis, feature engineering, multiple recommendation approaches, ranking models, software engineering practices, and MLOps deployment.

---

# 1. Project Objective

Build an industrial-style recommendation system using multiple recommendation strategies and compare their strengths and weaknesses.

The project emphasizes:

- Classical Machine Learning approaches
- Recommendation system fundamentals
- Feature engineering
- Ranking models (LambdaMART)
- Software engineering best practices
- MLOps deployment on AWS

---

# 2. Business Problem

E-commerce platforms need to recommend relevant products to users based on:

- Purchase history
- Customer preferences
- Product characteristics
- Popularity trends
- Similar products

The goal is to improve:

- Customer engagement
- Average order value
- Cross-selling opportunities
- Customer retention

---

# 3. Dataset

Dataset: Olist Brazilian E-Commerce Dataset

Tables used:

| Table | Purpose |
|---------|----------|
| olist_orders_dataset | Order information |
| olist_order_items_dataset | Purchased products and quantities |
| olist_customers_dataset | Customer information |
| olist_products_dataset | Product metadata |

---

# 4. Data Processing Pipeline

## Joins Performed

```python
orders
    + customers
    + order_items
    + products
```

Final interaction dataframe:

```text
interaction_df
```

Core columns:

```text
customer_unique_id
product_id
product_category_name
price
order_purchase_timestamp
product_weight_g
product_length_cm
product_height_cm
product_width_cm
```

---

# 5. Exploratory Data Analysis (EDA)

## Customer Spending

```text
Mean Customer Spend:
142.44

Median Spend:
89.90

95th Percentile:
422.00

99th Percentile:
1013.59
```

---

## Products Per Customer

```text
Mean:
1.18

Median:
1

Maximum:
24
```

Most customers purchased only one product.

This introduces severe sparsity.

---

## Product Sales

```text
Total Products:
32,951

Mean Sales:
3.41

Median Sales:
1

Maximum Sales:
527
```

The dataset follows a long-tail distribution.

---

## Top Categories

Most purchased categories:

```text
cama_mesa_banho
beleza_saude
esporte_lazer
moveis_decoracao
informatica_acessorios
```

---

## Highest Revenue Categories

```text
beleza_saude
relogios_presentes
cama_mesa_banho
esporte_lazer
informatica_acessorios
```

---

## Monthly Trends

Strong growth observed during:

```text
2017-2018
```

Peak purchasing activity occurred during:

```text
November 2017
January 2018
March 2018
```

---

# 6. Key Findings

---

## Finding 1: Severe User Sparsity

```text
Mean Products per Customer:
1.18

Median:
1
```

Most users purchased only a single product.

This limits collaborative filtering approaches.

---

## Finding 2: Long Tail Distribution

Most products were purchased only once.

Recommendation models must account for popularity imbalance.

---

## Finding 3: Customer Category Diversity Is Low

```text
Average Categories per Customer:
1.01
```

Most users purchase from only one category.

---

## Finding 4: Physical Product Attributes Matter

Unexpectedly strong signals:

- Weight
- Length
- Height
- Width

These features act as category proxies.

---

# 7. Recommendation Models

---

# Model 1: Popularity-Based Recommender

Objective:

Recommend globally popular products.

Approach:

```text
Purchase Count
↓
Normalization
↓
Popularity Score
```

Artifacts:

```text
popularity_recommender.parquet
```

Use Cases:

- Cold-start users
- New customers
- Fallback recommendations

---

# Model 2: Category-Based Recommender

Objective:

Recommend products from a customer's favorite category.

Approach:

```text
Customer
↓
Favorite Category
↓
Top Products in Category
```

Artifacts:

```text
category_popularity.parquet
customer_favorite_category.parquet
```

---

# Model 3: Content-Based Recommender

Objective:

Recommend similar products.

Features:

```text
product_weight_g
product_length_cm
product_height_cm
product_width_cm
product_category_name
```

Technique:

```text
Nearest Neighbors
```

Artifacts:

```text
content_based_nn_model.pkl
product_feature_matrix.npy
product_id_to_index.pkl
index_to_product_id.pkl
```

---

# Model 4: Hybrid Recommender

Objective:

Combine content similarity with popularity.

Formula:

```python
hybrid_score = (
    0.7 * similarity_score
    + 0.3 * popularity_score
)
```

Configuration:

```text
similarity_weight = 0.7
popularity_weight = 0.3
candidate_pool_size = 50
```

Artifact:

```text
hybrid_config.pkl
```

---

# Model 5: LambdaMART Ranking Model

Final production model.

Algorithm:

```text
LightGBM LambdaMART
```

---

## Initial Experiment

Features:

```text
12 features
Hard negatives only
```

Problem:

```text
customer_idx
product_idx
category_idx
favorite_category_idx
```

caused ID leakage.

---

## Final Experiment

Changes:

```text
Removed:
- customer_idx
- product_idx
- category_idx
- favorite_category_idx
```

Negative sampling:

```text
50% hard negatives
50% random negatives
```

---

## Final Features

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

---

## Final Model Results

```text
Best Iteration:
1360
```

Feature importance:

```text
customer_total_spend       23384
product_weight_g           14656
popularity_score           10611
product_height_cm           9996
product_length_cm           9949
product_width_cm            9159
customer_purchase_count     5983
is_favorite_category_match   509
```

---

# 8. Model Evaluation

---

## Quantitative Evaluation

Compared:

- Popularity
- Category
- Content
- Hybrid
- LambdaMART

LambdaMART delivered the strongest performance.

---

## Qualitative Evaluation

Findings:

- Recommendations aligned with customer interests.
- Cold-start users required popularity fallback.
- Category diversity remained low due to dataset sparsity.
- Diversification logic was added to serving.

---

# 9. Inference Layer

The project separates:

```text
Training
↓
Artifacts
↓
Inference
```

---

## popularity.py

Input:

```python
top_k
```

Output:

Global popular products.

---

## category.py

Input:

```python
customer_id
```

Output:

Products from favorite category.

---

## content.py

Input:

```python
product_id
```

Output:

Similar products.

---

## hybrid.py

Input:

```python
product_id
```

Output:

Content + popularity recommendations.

---

## lambdamart.py

Input:

```python
customer_total_spend
customer_purchase_count
favorite_category
```

Output:

Ranked recommendations.

Pure ML inference.

No business logic.

---

## final_recommender.py

Input:

```python
customer_id
```

Responsibilities:

```text
Known Customer
↓
LambdaMART
↓
Diversification

Unknown Customer
↓
Popularity Fallback
```

This is the production recommendation engine.

---

# 10. Testing

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

---

# 11. Artifacts

Production artifacts:

```text
final_ranker.pkl
final_ranker_features.pkl
final_ranker_metrics.json

popularity_recommender.parquet

category_popularity.parquet
customer_favorite_category.parquet

content_based_nn_model.pkl
product_feature_matrix.npy

product_features.parquet

product_id_to_index.pkl
index_to_product_id.pkl
```

---

# 12. Project Structure

```text
olist-recommendation-system/

├── notebooks/
├── data/
├── artifacts/
├── src/
│   └── inference/
│       ├── popularity.py
│       ├── category.py
│       ├── content.py
│       ├── hybrid.py
│       ├── lambdamart.py
│       └── final_recommender.py
│
├── tests/
│   ├── test_popularity.py
│   ├── test_category.py
│   ├── test_content.py
│   ├── test_hybrid.py
│   ├── test_lambdamart.py
│   └── test_final_recommender.py
│
└── README.md
```

---

# 13. Future Work

Upcoming phases:

```text
Phase 6
--------
FastAPI

Phase 7
--------
Docker

Phase 8
--------
MLflow

Phase 9
--------
Airflow

Phase 10
---------
Terraform

Phase 11
---------
AWS Deployment

Phase 12
---------
Monitoring & CI/CD
```

---

# 14. Lessons Learned

Key takeaways:

- Real-world recommendation data is extremely sparse.
- Classical ML approaches remain highly valuable.
- Negative sampling strategy significantly affects ranking models.
- Removing ID leakage improves generalization.
- Feature engineering is more important than model complexity.
- Physical product attributes can act as strong category proxies.
- Multiple recommendation strategies provide robust fallback mechanisms.

---