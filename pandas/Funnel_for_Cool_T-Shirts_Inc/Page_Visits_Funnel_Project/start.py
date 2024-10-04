import pandas as pd

visits = pd.read_csv("visits.csv", parse_dates=[1])
cart = pd.read_csv("cart.csv", parse_dates=[1])
checkout = pd.read_csv("checkout.csv", parse_dates=[1])
purchase = pd.read_csv("purchase.csv", parse_dates=[1])
print(visits.head(10))
print(cart.head(10))
print(checkout.head(10))
print(purchase.head(10))


c_to_v = pd.merge(visits, cart, how="left")
print(float(len(c_to_v[c_to_v.cart_time.isnull()])) / float(len(visits)) * 100)

check_to_cart = pd.merge(cart, checkout, how="left")

print(
    float(len(check_to_cart[check_to_cart.checkout_time.isnull()]))
    / float(len(cart))
    * 100
)

all_data = (
    pd.merge(visits, cart, how="left")
    .merge(checkout, how="left")
    .merge(purchase, how="left")
)

print(
    float(len(all_data[all_data.purchase_time.isnull()][(all_data.checkout_time.notnull())]))
    / float(len(visits))
    * 100
)


# Using the giant merged DataFrame all_data that you created, let’s calculate the average time from initial visit to final purchase. Add a column that is the difference between purchase_time and visit_time.
all_data["time_to_purchase"] = all_data.purchase_time - all_data.visit_time
print(all_data[all_data.time_to_purchase.notnull()]["time_to_purchase"])
print(all_data.time_to_purchase.mean())
# Examine the results by printing the new column to the screen.
# Calculate the average time to purchase by applying the .mean() function to your new column.
