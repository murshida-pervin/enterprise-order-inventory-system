from sklearn.linear_model import LinearRegression
import numpy as np

months = np.array([1, 2, 3, 4, 5, 6, 7, 8]).reshape(-1, 1)
sales = np.array([100, 120, 135, 150, 170, 180, 210, 240])
model = LinearRegression()
model.fit(months, sales)
future = model.predict([[9]])
print("Predicted sales next month:", int(future[0]))
