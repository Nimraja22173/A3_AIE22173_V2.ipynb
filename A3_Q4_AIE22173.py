import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Taking dataset from Excel sheet
data_set = pd.read_excel(r"C:\Users\nimra\OneDrive\Desktop\Lab Session1 Data.xlsx", sheet_name="IRCTC Stock Price")

# For mean and variable
col_D = data_set.iloc[:, 3]
stat_mean = np.mean(col_D)
stat_var = np.var(col_D)

# For Wednesday mean calculation
data_set["Date"] = pd.to_datetime(data_set["Date"])
data_set['weekday'] = data_set["Date"].dt.weekday
wednesdays = data_set[data_set['weekday'] == 2]
wednesday_mean = wednesdays['Price'].mean()

# April mean calculation
april_data = data_set[data_set["Date"].dt.month == 4]
April_mean = np.mean(april_data['Price'])

# Probability for making a loss in the stock
probability_of_loss = (data_set['Chg%'] < 0).mean()

# Probability of making a profit on Wednesdays
probability_of_profit_wed = (wednesdays['Chg%'] > 0).mean()

# Calculate the conditional probability of making a profit, given that today is Wednesday
conditional_prob_wed = (wednesdays[wednesdays['Chg%'] > 0].shape[0] / wednesdays.shape[0])

# Scatter-plot of Chg% against the day of the week
sns.scatterplot(x="weekday", y="Chg%", data=data_set, hue="weekday", palette="hls")
plt.xlabel("Day of the Week")
plt.ylabel("Chg%")
plt.title("Chg% Distribution by Day of the Week")
plt.show()

# Display results
print(f"The mean of Wednesdays is {wednesday_mean}")
print(f"The mean of the dataset is {stat_mean}")
print(f"The variance of the dataset is {stat_var}")
print(f"The mean of the April month is {April_mean}")
print(f"The probability of making a loss in the stock is {probability_of_loss}")
print(f"The probability of making a profit on Wednesdays is {probability_of_profit_wed}")
print(f"The conditional probability of making a profit given that today is Wednesday is: {conditional_prob_wed}")
