"""from services import InventoryService

service = InventoryService()

# Show products
products = service.get_products()

print("PRODUCTS:")
for p in products:
    print(p)

# Create order
service.create_order("John Doe", 1, 2)
"""
import matplotlib.pyplot as plt
from services import InventoryService
from analytics import Analytics


service = InventoryService()
products = service.get_products()
print("\nPRODUCTS\n")
for p in products:
    print(p)
service.create_order("Vytautas", 2, 10)
analytics = Analytics()
report = analytics.sales_report()
print(report)


# Print the DataFrame
print("\nSALES REPORT\n")
print(report)

# Create bar chart
report.plot(
    x="ProductName",
    y="TotalSold",
    kind="bar",
    legend=False
)

plt.title("Top Selling Products")
plt.xlabel("Product")
plt.ylabel("Quantity Sold")
plt.tight_layout()
plt.show()
