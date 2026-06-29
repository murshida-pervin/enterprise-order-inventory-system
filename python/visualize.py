import matplotlib.pyplot as plt

report = analytics.sales_report()
report.plot(x="ProductName", y="TotalSold", kind="bar")
plt.title("Top Selling Products")
plt.show()
