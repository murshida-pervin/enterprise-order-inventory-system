import pandas as pd
from db import get_connection


class Analytics:

    def sales_report(self):
        conn = get_connection()

        try:
            query = """
            SELECT
                p.ProductName,
                SUM(oi.Quantity) AS TotalSold
            FROM Products p
            JOIN OrderItems oi
                ON p.ProductID = oi.ProductID
            GROUP BY p.ProductName
            """

            return pd.read_sql(query, conn)

        finally:
            conn.close()