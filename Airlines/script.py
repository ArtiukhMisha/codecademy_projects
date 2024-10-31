import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

air_data = pd.read_csv("flight.csv")
print(air_data.head(20))
print(air_data.info())
sns.histplot(air_data.coach_price)
plt.axvline(air_data.coach_price.mean(), color="red")
Q1, Q3 = np.percentile(air_data.coach_price, [25, 75])
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
avg = np.mean(
    air_data.coach_price[
        (air_data.coach_price >= lower_bound) & (air_data.coach_price <= upper_bound)
    ]
)
plt.axvline(avg, color="black")
plt.show()
plt.clf()

sns.histplot(air_data[air_data.hours == 8].coach_price)
plt.axvline(air_data[air_data.hours == 8].coach_price.mean(), color="red")
plt.show()
plt.clf()


sns.histplot(air_data[air_data.delay < 50].delay)
plt.xlim(0, 50)
plt.axvline(air_data.delay.median(), color="red")
plt.show()
plt.clf()


samp = air_data.sample(n=len(air_data) // 50)
sns.lmplot(
    x="coach_price",
    y="firstclass_price",
    data=samp,
    line_kws={"color": "black"},
    scatter_kws={"alpha": 0.2},
)
plt.show()
plt.clf()
air_data["inflight_meal"] = air_data["inflight_meal"].map({"Yes": 0, "No": 1})
air_data["inflight_entertainment"] = air_data["inflight_entertainment"].map(
    {"Yes": 0, "No": 1}
)
air_data["inflight_wifi"] = air_data["inflight_wifi"].map({"Yes": 0, "No": 1})
selected_column = air_data[["inflight_meal", "inflight_entertainment", "inflight_wifi"]]
air_data["inflight_features"] = selected_column.idxmax(axis=1)

sns.boxplot(x="inflight_features", y="coach_price", data=air_data, palette="Set2")
# GPT help
"""
air_data[['inflight_meal', 'inflight_entertainment', 'inflight_wifi']] = air_data[['inflight_meal', 'inflight_entertainment', 'inflight_wifi']].replace({'Yes': 0, 'No': 1})
air_data['inflight_features'] = air_data[['inflight_meal', 'inflight_entertainment', 'inflight_wifi']].idxmax(axis=1)
sns.boxplot(x='inflight_features', y='coach_price', data=air_data, palette='Set2')

inflight_columns = ['inflight_meal', 'inflight_entertainment', 'inflight_wifi']

# Replace 'Yes'/'No' with 0/1, create 'inflight_features' in one step, and plot directly
air_data = (
    air_data.assign(**{col: air_data[col].map({'Yes': 0, 'No': 1}) for col in inflight_columns})
            .assign(inflight_features=lambda df: df[inflight_columns].idxmax(axis=1))
)
"""
plt.show()
plt.clf()

sns.lmplot(x = "hours", y = "passengers", data = samp, x_jitter = 0.25, scatter_kws={"s": 5, "alpha":0.2}, fit_reg = False)

plt.show()
plt.clf()


samp['weekdays'] = samp.apply(lambda row: row['weekends'] if row['day_of_week'] in ['Saturday', 'Sunday'] else row['weekday'], axis=1)

samp['weekdays']=samp.apply(lambda row: 'weekends' if row['day_of_week'] in ['Saturday','Sunday'] else 'weekday',axis=1)
sns.scatterplot(x='coach_price',y='firstclass_price',data=samp, hue='weekdays', palette='Set1')
plt.show()
plt.clf()

sns.boxplot(x='day_of_week',y='coach_price',data=samp,hue='redeye',palette='Set2')
plt.show()
plt.clf()
