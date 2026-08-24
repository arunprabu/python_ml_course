import pandas as pd

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

"""
HANDS-ON: Cluster customers by purchase behavior.

Follow the numbered steps below and run this file. Then open
customer_clustering_handson.md for exercises — tweak this same script
to complete them.

Scenario: a retailer tracks two things per customer — how often they
visit each month, and how much they spend per visit on average
(their "basket value"). There's no label for what TYPE of shopper each
customer is; we'll let K-Means find that structure.
"""


# STEP 1 — Load the data
#
# In a real project this would usually come from a CSV
# (pd.read_csv("customer_purchases.csv")). Here it's written out
# directly so the example runs standalone with no extra files.

data = {
    "visits_per_month": [1, 2, 1, 2, 1, 8, 9, 7, 8, 9, 2, 3, 2, 3, 2, 10, 11, 9, 10, 12],
    "avg_basket_value": [15, 18, 12, 20, 16, 20, 22, 18, 25, 21, 80, 85, 78, 90, 82, 60, 65, 58, 70, 62],
}

df = pd.DataFrame(data)
print("Sample of the data:")
print(df.head(), "\n")


# STEP 2 — Choose features (X)
#
# There's no target column here — clustering only needs X.

X = df[["visits_per_month", "avg_basket_value"]]


# STEP 3 — Scale the features
#
# avg_basket_value (₹12-90) and visits_per_month (1-12) are on
# different numeric ranges. Distance-based algorithms like K-Means
# always risk letting the larger-range feature dominate, so scaling
# first is good practice even when — as here — the groups turn out to
# be separated enough that it doesn't change the final result.

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


# STEP 4 — Choose K with the elbow method

print("Elbow method:")
for k in range(1, 7):
    model = KMeans(n_clusters=k, random_state=7, n_init=10)
    model.fit(X_scaled)
    print(f"  K={k}: inertia = {model.inertia_:.2f}")
print()


# STEP 5 — Train the final model

k = 4
model = KMeans(n_clusters=k, random_state=7, n_init=10)
df["cluster"] = model.fit_predict(X_scaled)


# STEP 6 — Interpret each cluster

profile = df.groupby("cluster")[["visits_per_month", "avg_basket_value"]].mean().round(1)
profile["customers"] = df.groupby("cluster").size()

print(f"Cluster profile (K={k}):")
print(profile)
print(
    "\nRead each row as a shopper type: low visits + low basket = occasional"
    "\nbargain shoppers; high visits + low basket = frequent small-basket"
    "\nregulars; low visits + high basket = occasional stock-up shoppers;"
    "\nhigh visits + high basket = the retailer's most valuable customers."
)


# STEP 7 — Assign a new customer to a cluster

new_customer = pd.DataFrame({"visits_per_month": [9], "avg_basket_value": [24]})
new_customer_scaled = scaler.transform(new_customer)
predicted_cluster = model.predict(new_customer_scaled)[0]

print(f"\nNew customer (9 visits/month, ₹24 avg basket) assigned to cluster: {predicted_cluster}")

# ---------------------------------------------------------------------------
# TRY IT YOURSELF — see customer_clustering_handson.md for the full exercises.
# 1. Change K to 3 — which two clusters merge together? Does the merged
#    group still make business sense as a single persona?
# 2. Comment out the `StandardScaler` step (use X instead of X_scaled
#    everywhere) and re-run. Do the clusters change? Why?
# 3. Add a `days_since_last_purchase` column and include it as a third
#    feature — does K=4 still look like the right choice on the elbow plot?
# ---------------------------------------------------------------------------
