from services import InventoryService

service = InventoryService()

# Show products
products = service.get_products()

print("PRODUCTS:")
for p in products:
    print(p)

# Create order
service.create_order("John Doe", 1, 2)