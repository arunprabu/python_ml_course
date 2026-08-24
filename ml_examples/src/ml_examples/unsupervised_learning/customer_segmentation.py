import pandas as pd

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

"""
SCENARIO: Customer Segmentation for Marketing

A marketing team wants to stop sending the same campaign to every
customer. They have two numbers for each customer: annual income and a
"spending score" (0-100, based on purchase behavior, how it's computed
doesn't matter here). There's no "segment" label in the data — that's
exactly what clustering is for.

The goal: split customers into groups with similar income/spending
patterns, then hand marketing a short, human-readable persona for each
group so they can target campaigns instead of blasting everyone the
same message.
"""


# 1. DATA — customers with income and spending score, no segment label

data = {
    "annual_income_k": [
        25, 27, 24, 26, 23,
        20, 19, 22, 18, 21,
        60, 62, 58, 61, 59,
        85, 88, 82, 90, 86,
        55, 50, 65, 48, 53,
    ],
    "spending_score": [
        20, 18, 22, 19, 21,
        75, 80, 72, 78, 76,
        25, 22, 28, 24, 26,
        85, 88, 80, 90, 82,
        50, 55, 45, 58, 48,
    ],
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)


# 2. FEATURES (X) — scale, since income (₹ thousands) and spending score
#    (0-100) are on very different numeric scales

X = df[["annual_income_k", "spending_score"]]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


# 3. CHOOSE K — elbow method, then confirmed against business need
#
# Marketing already knows they want a handful of distinct personas to
# design campaigns around — the elbow method here is a sanity check on
# that, not the only input to the decision.

print("\nElbow method:")
for k in range(1, 7):
    model = KMeans(n_clusters=k, random_state=42, n_init=10)
    model.fit(X_scaled)
    print(f"  K={k}: inertia = {model.inertia_:.2f}")


# 4. TRAIN with K=5

k = 5
model = KMeans(n_clusters=k, random_state=42, n_init=10)
df["segment"] = model.fit_predict(X_scaled)


# 5. PROFILE each segment — turn cluster numbers into personas marketing can use

profile = df.groupby("segment")[["annual_income_k", "spending_score"]].mean().round(1)
profile["customers"] = df.groupby("segment").size()

print(f"\nSegment profile (K={k}):")
print(profile)

personas = {
    0: "Value seekers — low income, high spending: engage with loyalty/rewards programs",
    1: "Cautious savers — mid-high income, low spending: needs trust-building, not discounts",
    2: "Budget-conscious — low income, low spending: price-sensitive, respond to low-cost offers",
    3: "Premium customers — high income, high spending: best targets for high-end campaigns",
    4: "Mainstream — mid income, mid spending: general campaigns, upsell opportunities",
}

print("\nSuggested personas (match to the segment numbers above by eye):")
for segment_id, description in personas.items():
    print(f"  Segment {segment_id}: {description}")


# 6. ASSIGN a new customer to a segment

new_customer = pd.DataFrame({"annual_income_k": [30], "spending_score": [72]})
new_customer_scaled = scaler.transform(new_customer)
predicted_segment = model.predict(new_customer_scaled)[0]

print(f"\nNew customer (₹30k income, spending score 72) assigned to segment: {predicted_segment}")
