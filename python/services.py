from db import get_connection

class InventoryService:

    # GET all products
    def get_products(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM Products")
        rows = cursor.fetchall()

        conn.close()
        return rows

    # CREATE ORDER (IMPORTANT)
    def create_order(self, customer_name, product_id, quantity,order_date):
        conn = get_connection()
        cursor = conn.cursor()

        # 1. Check stock
        cursor.execute("SELECT Stock FROM Products WHERE ProductID = ?", product_id)
        stock = cursor.fetchone()[0]

        if stock < quantity:
            print("❌ Not enough stock!")
            return

        # 2. Insert order
        cursor.execute("INSERT INTO Orders (CustomerName, OrderDate, OrderType) VALUES (?,?,?)", customer_name, order_date, "Customer")
        conn.commit()

        # 3. Get last order id
        cursor.execute("SELECT @@IDENTITY")
        order_id = cursor.fetchone()[0]

        # 4. Insert order item
        cursor.execute(
            "INSERT INTO OrderItems (OrderID, ProductID, Quantity) VALUES (?, ?, ?)",
            order_id, product_id, quantity
        )

        # 5. Reduce stock
        cursor.execute(
            "UPDATE Products SET Stock = Stock - ? WHERE ProductID = ?",
            quantity, product_id
        )

        conn.commit()
        conn.close()

        print("✅ Order created successfully")