CREATE DATABASE InventorySystem;
GO
USE InventorySystem;


CREATE TABLE Products (
    ProductID INT IDENTITY PRIMARY KEY,
    Name VARCHAR(100),
    Price DECIMAL(10,2),
    Stock INT
);
GO

CREATE TABLE Orders (
    OrderID INT IDENTITY PRIMARY KEY,
    CustomerName VARCHAR(100),
    OrderDate DATETIME DEFAULT GETDATE()
);

GO

CREATE TABLE OrderItems (
    OrderItemID INT IDENTITY PRIMARY KEY,
    OrderID INT FOREIGN KEY REFERENCES Orders(OrderID),
    ProductID INT FOREIGN KEY REFERENCES Products(ProductID),
    Quantity INT
);