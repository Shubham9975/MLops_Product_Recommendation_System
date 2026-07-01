# Model Results

# Model 1 - Popularity Recommender

## Objective

Recommend globally popular products.

## Advantages

- Simple
- Fast
- Excellent cold-start support

## Limitations

- No personalization
- Popularity bias

---

# Model 2 - Category Affinity Recommender

## Objective

Recommend products from a customer's preferred category.

## Advantages

- Simple personalization
- Interpretable

## Limitations

- Low category diversity
- Sparse customer histories

---

# Model 3 - Content-Based Recommender

## Features

```text
product_category_name
product_weight_g
product_length_cm
product_height_cm
product_width_cm
```

## Algorithm

```text
Nearest Neighbors
Cosine Similarity
```

## Advantages

- No customer history required
- Similar product recommendations

## Limitations

- Limited exploration
- Strong category clustering

---

# Model 4 - Hybrid Recommender

## Formula

```python
hybrid_score = (
    0.7 * similarity_score
    +
    0.3 * popularity_score
)
```

## Advantages

- Combines relevance and popularity
- Better ranking stability

## Limitations

- Still item-centric
- No deep personalization

---

# Model 5 - LambdaMART

---

# Initial Version

## Features

```text
12 features
```

Included:

```text
customer_idx
product_idx
category_idx
favorite_category_idx
```

---

# Problems

These features introduced:

```text
ID Leakage
```

The model learned identities instead of patterns.

---

# Final Version

## Removed

```text
customer_idx
product_idx
category_idx
favorite_category_idx
```

---

## Negative Sampling

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

# Best Iteration

```text
1360
```

---

# Feature Importance

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

# Key Findings

---

## Customer Spending Matters Most

The strongest personalization signal:

```text
customer_total_spend
```

---

## Physical Dimensions Matter

Unexpectedly powerful features:

```text
weight
height
length
width
```

These act as category proxies.

---

## Popularity Remains Important

Global demand information significantly improves ranking quality.

---

## Category Match Has Small Influence

The model learned broader patterns rather than relying only on favorite categories.

---

# Final Production Model

```text
Algorithm:
LightGBM LambdaMART

Features:
8

Negative Sampling:
50% Hard
50% Random

Best Iteration:
1360
```
