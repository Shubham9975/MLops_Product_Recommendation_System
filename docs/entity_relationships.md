# User Entity

customer_unique_id

Source:
olist_customers_dataset

---

# Item Entity

product_id

Source:
olist_products_dataset

---

# Interaction Entity

purchase

Source:
olist_orders_dataset +
olist_order_items_dataset

---

# Main Relationship

customers
    ↓ customer_id
orders
    ↓ order_id
order_items
    ↓ product_id
products