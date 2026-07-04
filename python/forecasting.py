import pandas as pd
from sklearn.linear_model import LinearRegression
from db import get_connection   # or database.py if renamed


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
            print("No sales data available")
            return

        print("\n=========== SALES FORECAST ===========\n")

        # loop each product
        for product in df["ProductName"].unique():

            product_data = df[df["ProductName"] == product].copy()

            # need at least 2 months
            if len(product_data) < 2:
                continue

            product_data = product_data.reset_index(drop=True)

            X = list(range(1, len(product_data) + 1))
            y = product_data["TotalSold"]

            model = LinearRegression()
            model.fit(pd.DataFrame(X), y)

            current_month = int(y.iloc[-1])
            next_month = int(model.predict([[len(product_data) + 1]])[0])

            print(product)
            print(f"Current Month : {current_month}")
            print(f"Next Month    : {next_month}\n")