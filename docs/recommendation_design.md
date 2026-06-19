# Recommendation Objective

Business Goal:

Recommend relevant products to customers based on their historical purchase behavior and product characteristics.

Recommendation Type:

Top-N Product Recommendation

Input:

customer_unique_id

Output:

Top N recommended products

Success Criteria:

Recommend products likely to be purchased by the customer while increasing customer engagement and product discovery.


# Model Roadmap

Model 1:
Popularity-Based Recommender

Model 2:
Category Affinity Recommender

Model 3:
Content-Based Recommender

Model 4:
Hybrid Recommender

Model 5:
Learning-to-Rank Recommender



# Recommendation Universe

Total Products: 32,951

Products With >= 5 Purchases:
4,832

Recommendation Catalog:

Only products with at least 5 historical purchases will be considered eligible for recommendation.

Reason:

Products with extremely low interaction counts provide insufficient signal for recommendation models and may introduce noise.


## Recommendation Catalog

Products Eligible For Recommendation:

Products with at least 5 historical purchases.

Statistics:

- Eligible Products: 4,832
- Interactions: 68,810
- Customers: 58,678

Reason:

Products with extremely low interaction frequency provide insufficient recommendation signal and increase noise.