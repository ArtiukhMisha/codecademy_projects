import pandas as pd

inventory = pd.read_csv("inventory.csv")

staten_island = inventory.head(10)
product_request = staten_island.product_description[staten_island["quantity"] == 0]
seed_request = staten_island[
    (staten_island["location"] == "Brooklyn")
    | (staten_island["product_type"] == "seeds")
]

inventory["in_stock"] = inventory.quantity.apply(lambda x: True if x > 0 else False)
inventory["total_value"] = inventory.apply(lambda x: x["price"] * x["quantity"], axis=1)

combine_lambda = lambda row: "{} - {}".format(row.product_type, row.product_description)  # noqa: E731
inventory["full_description"] = inventory.apply(combine_lambda, axis=1)
print(inventory.head(10))
