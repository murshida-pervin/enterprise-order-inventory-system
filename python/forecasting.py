import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from db import get_connection


class Forecasting:

    def product_forecast(self):

        conn = get_connection()

        query = """
        SELECT
            P.ProductName,
            YEAR(O.OrderDate) AS Yr,
            MONTH(O.OrderDate) AS Mn,
            SUM(OI.Quantity) AS TotalSold
        FROM Orders O
        JOIN OrderItems OI ON O.OrderID = OI.OrderID
        JOIN Products P ON P.ProductID = OI.ProductID
        WHERE O.OrderType = 'Customer'
        GROUP BY P.ProductName, YEAR(O.OrderDate), MONTH(O.OrderDate)
        ORDER BY P.ProductName, Yr, Mn
        """

        df = pd.read_sql(query, conn)
        conn.close()

        if df.empty:
            print("No sales data available.")
            return

        print("\n========== SALES FORECAST ==========\n")

        # Forecast each product separately
        for product in df["ProductName"].unique():

            product_data = df[df["ProductName"] == product].copy()

            if len(product_data) < 2:
                continue

            product_data = product_data.reset_index(drop=True)

            # X = Month Number
            X = list(range(1, len(product_data) + 1))
            y = product_data["TotalSold"]

            model = LinearRegression()
            model.fit(pd.DataFrame(X), y)

            # Predict next month
            next_month = len(product_data) + 1
            prediction = model.predict([[next_month]])[0]

            print(f"Product       : {product}")
            print(f"Current Sales : {int(y.iloc[-1])}")
            print(f"Predicted Next Month : {int(prediction)}\n")

            # -----------------------------
            # Visualization
            # -----------------------------

            plt.figure(figsize=(8,5))

            # Historical Sales
            plt.plot(
                X,
                y,
                marker='o',
                linewidth=3,
                label="Historical Sales"
            )

            # Regression Line
            future_x = X + [next_month]
            future_y = list(model.predict(pd.DataFrame(future_x)))

            plt.plot(
                future_x,
                future_y,
                linestyle='--',
                marker='o',
                linewidth=2,
                label="Linear Regression"
            )

            # Highlight Prediction
            plt.scatter(
                next_month,
                prediction,
                s=120,
                color='red',
                label="Forecast"
            )

            plt.title(f"{product} Sales Forecast")
            plt.xlabel("Month")
            plt.ylabel("Units Sold")
            plt.xticks(future_x)
            plt.grid(True, linestyle="--", alpha=0.4)
            plt.legend()

            plt.tight_layout()
            plt.show()
