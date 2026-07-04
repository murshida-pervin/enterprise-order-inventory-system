import random
from datetime import datetime, timedelta

import matplotlib.pyplot as plt

from services import InventoryService
from analytics import Analytics
from forecasting import Forecasting

service = InventoryService()


def view_products():
    """Display all available products."""
    print("\nAVAILABLE PRODUCTS\n")

    for product in service.get_products():
        print(product)


def generate_sample_data():
    """Generate random customer orders."""

    months = int(input("Generate data for how many months? (e.g. 2): "))

    customers = [
        "ABC Retail",
        "City Supermarket",
        "Fresh Mart",
        "Global Traders"
    ]

    products = [
        (1, 2),   # Laptop
        (2, 2),   # Phone
        (3, 8),   # Mouse
        (4, 3)    # LG Monitor
    ]

    total_orders = months * 50
    start_date = datetime.now() - timedelta(days=months * 30)

    print(f"\nGenerating {total_orders} sample orders...\n")

    for _ in range(total_orders):

        customer = random.choice(customers)
        product_id, max_qty = random.choice(products)

        quantity = random.randint(1, max_qty)

        order_date = start_date + timedelta(
            days=random.randint(0, months * 30),
            hours=random.randint(0, 23),
            minutes=random.randint(0, 59)
        )

        service.create_order(
            customer,
            product_id,
            quantity,
            order_date
        )

    print("Sample data generated successfully.\n")


def create_order():

    print("\nCREATE CUSTOMER ORDER\n")

    products = service.get_products()

    customer = input("Customer Name: ")

    print("\nAvailable Products")

    for product in products:
        print(f"{product[0]}. {product[1]} (Stock: {product[3]})")

    product_id = int(input("\nProduct ID: "))
    quantity = int(input("Quantity: "))

    date = input("Order Date (YYYY-MM-DD) [Leave blank for today]: ").strip()

    if date:
        order_date = datetime.strptime(date, "%Y-%m-%d")
    else:
        order_date = datetime.now()

    service.create_order(
        customer,
        product_id,
        quantity,
        order_date
    )

    print("\nOrder created successfully!")


def show_sales_report():

    analytics = Analytics()

    report = analytics.sales_report()

    print("\nSALES REPORT\n")
    print(report)

    report = report.sort_values("TotalSold", ascending=False)

    max_sales = report["TotalSold"].max()

    colors = []

    for sold in report["TotalSold"]:

        if sold >= max_sales * 0.70:
            colors.append("green")
        elif sold >= max_sales * 0.40:
            colors.append("gold")
        else:
            colors.append("red")

    plt.figure(figsize=(9, 5))

    bars = plt.bar(
        report["ProductName"],
        report["TotalSold"],
        color=colors
    )

    for bar in bars:

        height = bar.get_height()

        plt.text(
            bar.get_x() + bar.get_width()/2,
            height + 0.5,
            int(height),
            ha="center",
            fontweight="bold"
        )

    plt.title("Top Selling Products")
    plt.xlabel("Product")
    plt.ylabel("Quantity Sold")
    plt.grid(axis="y", linestyle="--", alpha=0.3)

    plt.tight_layout()
    plt.show()

def menu():

    while True:

        print("\n" + "=" * 40)
        print(" Enterprise Inventory System")
        print("=" * 40)
        print("1. View Products")
        print("2. Generate Sample Data")
        print("3. Create Customer Order")
        print("4. View Sales Report")
        print("5. Forecast Next Month Sales")
        print("6. Exit")

        choice = input("\nSelect an option: ")

        if choice == "1":
            view_products()

        elif choice == "2":
            generate_sample_data()

        elif choice == "3":
            create_order()

        elif choice == "4":
            show_sales_report()

        elif choice == "5":
           forecasting = Forecasting()
           forecasting.product_forecast() 

        elif choice == "6":
             break


if __name__ == "__main__":
    menu()