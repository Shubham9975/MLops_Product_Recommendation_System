# Exploratory Data Analysis (EDA) Findings

## Project

Personalized Product Recommendation System using Olist E-Commerce Dataset

---

# 1. Dataset Overview

| Metric                    |   Count |
| ------------------------- | ------: |
| Total Customers           |  96,096 |
| Total Orders              |  99,441 |
| Total Products            |  32,951 |
| Total Categories          |      73 |
| Total Interaction Records | 112,650 |

The interaction dataset was created by joining:

* olist_customers_dataset
* olist_orders_dataset
* olist_order_items_dataset
* olist_products_dataset

The resulting interaction dataset contains customer-product purchase interactions and serves as the primary dataset for recommendation modeling.

---

# 2. Customer Analysis

## Orders Per Customer

Analysis showed that the majority of customers placed only a single order.

### Distribution

| Orders | Customers |
| ------ | --------: |
| 1      |    92,507 |
| 2      |     2,673 |
| 3      |       192 |
| 4+     |  Very Few |

### Key Findings

* Approximately 96.95% of customers placed only one order.
* Repeat purchase behavior exists but is limited.
* Customer history is highly sparse.

### Implications

User-based collaborative filtering may be less effective due to limited historical behavior available for most customers.

---

## Products Purchased Per Customer

### Statistics

* Mean: 1.18
* Median: 1
* Maximum: 24

### Findings

* Most customers purchased only one product.
* A small number of customers purchased multiple products.

---

## Category Diversity Per Customer

### Statistics

* Mean: 1.01
* Median: 1
* Maximum: 5

### Findings

* Most customers purchased products from only one category.
* Cross-category purchasing behavior is limited.

### Implications

Customer preference profiles are shallow, making deep personalization difficult using customer history alone.

---

## Customer Spend Analysis

### Spend Distribution

| Percentile |   Spend |
| ---------- | ------: |
| 25%        |   47.90 |
| 50%        |   89.90 |
| 75%        |  155.00 |
| 90%        |  284.00 |
| 95%        |  422.00 |
| 99%        | 1013.59 |

### Findings

* Spending distribution is highly right-skewed.
* A small percentage of customers contribute significantly higher revenue.
* Distinct customer value segments exist.

Potential customer segments:

* Low Value Customers
* Medium Value Customers
* High Value Customers
* VIP Customers

---

# 3. Order Analysis

## Products Per Order

### Distribution

| Products in Order | Number of Orders |
| ----------------- | ---------------: |
| 1                 |           88,863 |
| 2                 |            7,516 |
| 3                 |            1,322 |
| 4+                |   Relatively Few |

### Findings

* Approximately 90% of orders contain only one product.
* Multi-product baskets are relatively uncommon.

### Implications

Market basket analysis and association-rule-based recommenders may have limited effectiveness due to weak co-purchase signals.

---

# 4. Product Analysis

## Product Popularity

### Statistics

* Total Products: 32,951
* Median Purchases Per Product: 1
* Mean Purchases Per Product: 3.42
* Maximum Purchases: 527

### Findings

* Product sales follow a long-tail distribution.
* Half of all products were purchased only once.
* A small number of products dominate sales volume.

### Implications

Popularity-based recommendations can serve as a strong baseline model.

---

## Top Purchased Categories

| Category               | Purchases |
| ---------------------- | --------: |
| cama_mesa_banho        |    11,115 |
| beleza_saude           |     9,670 |
| esporte_lazer          |     8,641 |
| moveis_decoracao       |     8,334 |
| informatica_acessorios |     7,827 |

### Findings

* Product categories exhibit strong purchase patterns.
* Category-level recommendations are feasible.

---

## Categories with Largest Catalog Size

| Category         | Unique Products |
| ---------------- | --------------: |
| cama_mesa_banho  |           3,029 |
| esporte_lazer    |           2,867 |
| moveis_decoracao |           2,657 |
| beleza_saude     |           2,444 |

### Findings

* Large product catalogs exist within popular categories.
* Category popularity is not driven by a small number of products.

---

## Highest Revenue Categories

| Category               |   Revenue |
| ---------------------- | --------: |
| beleza_saude           | 1,258,681 |
| relogios_presentes     | 1,205,005 |
| cama_mesa_banho        | 1,036,988 |
| esporte_lazer          |   988,048 |
| informatica_acessorios |   911,954 |

### Findings

* Revenue concentration differs from purchase frequency.
* Some categories generate significantly higher value despite lower purchase volume.

---

# 5. Time Series Analysis

Monthly purchase trends indicate substantial growth throughout the observation period.

### Observations

* Strong growth from early 2017 through mid-2018.
* Significant purchase spike observed in November 2017.
* Elevated activity continued through December 2017.

### Possible Explanation

* Black Friday promotions
* Holiday shopping season

### Implications

Temporal features may be useful during feature engineering.

Potential features:

* Purchase Month
* Purchase Quarter
* Purchase Year
* Recency-Based Features

---

# 6. Data Quality Findings

### Missing Categories

* Missing product categories: 1,603 records
* Represents approximately 1.4% of interaction records.

### Duplicate Customer-Product Pairs

* Duplicate customer-product interactions: 10,663

### Findings

* Repeat purchases of the same product exist.
* Missing category values are relatively low and manageable during preprocessing.

---

# 7. Recommendation System Feasibility Assessment

## Strong Signals

* Product Popularity
* Product Category
* Product Revenue
* Product Metadata
* Customer Spending Behavior
* Purchase Time Information

## Weak Signals

* Customer History
* Repeat Purchases
* Multi-Product Baskets
* Cross-Category Customer Behavior

---

# 8. Recommendation Strategy Implications

Based on the exploratory analysis:

### Recommended Approaches

1. Popularity-Based Recommendation
2. Category-Based Recommendation
3. Product Similarity Recommendation
4. Hybrid Recommendation System
5. Learning-to-Rank Models

### Less Suitable Approaches

1. Pure User-Based Collaborative Filtering
2. Heavy Market Basket Analysis
3. Deep Personalization Based Solely on Purchase History

---

# Conclusion

The dataset exhibits sparse customer behavior but strong product-level signals. Product popularity, category information, product attributes, and customer spending characteristics are expected to be the primary drivers of recommendation performance. A hybrid recommendation approach combining popularity, category affinity, and product similarity is likely to be the most effective strategy for this dataset.
