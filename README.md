# 🚀 AI-Enabled Enterprise Inventory Analytics System

## 📌 Problem

Businesses struggle with:
- Inventory tracking
- Sales analysis
- Demand forecasting
- Stock management inefficiencies

---

## 💡 Solution

This project is a Python + SQL Server based inventory intelligence system that:

- Manages products and stock
- Processes customer orders
- Handles purchase orders (restocking)
- Tracks inventory in real time
- Analyzes sales performance
- Forecasts future demand using Machine Learning
- Provides interactive CLI dashboard with charts and reports

---

## 📊 Key Features

### 🛒 Inventory Management
- Add and manage products
- Real-time stock tracking
- Automatic stock deduction on orders

### 📦 Order Management
- Customer order creation (manual input)
- Sample data generation (last N months)
- Purchase order creation for restocking
- Order history with timestamps

### 📈 Sales Analytics
- Total sales per product
- Top-selling product analysis
- Color-coded bar charts:
  - 🟢 High sales
  - 🟡 Medium sales
  - 🔴 Low sales
- Quantity labels on bars

### 🤖 Machine Learning Forecasting
- Linear Regression model (Scikit-Learn)
- Predicts next-month sales per product
- Uses real SQL Server data
- Trend line visualization

### 🖥️ CLI Dashboard
- Menu-driven interface:
  - View Products
  - Create Orders
  - Generate Sample Data
  - View Reports
  - Forecast Sales

---

## 🧠 Machine Learning Model

- Algorithm: Linear Regression
- Input: Monthly aggregated sales data
- Output: Next month sales prediction
- Visualization: Trend line + forecast point

---

## 🏗️ Architecture

User (CLI)
   ↓
main.py (Menu System)
   ↓
services.py (Business Logic)
   ↓
SQL Server Database
   ↓
analytics.py (Reports)
   ↓
forecasting.py (ML Model)
   ↓
matplotlib (Charts)

---

## 🛠️ Technologies Used

- Python 3
- Microsoft SQL Server
- pyodbc
- Pandas
- Matplotlib
- Scikit-Learn
- OOP (Object-Oriented Programming)
- Git & GitHub

---

## 📂 Project Structure

enterprise-order-inventory-system/
│
├── sql/
│ ├── schema.sql
│ └── procedures.sql
│
├── python/
│ ├── main.py
│ ├── dp.py
│ ├── services.py
│ ├── analytics.py
│ ├── forecasting.py
│ └── visualization.py
│
├── docs/
│ └── architecture.md
│
├── README.md
├── requirements.txt
└── .gitignore
---

## ⚙️ System Flow

1. User selects option from CLI
2. System processes request
3. Data stored in SQL Server
4. Analytics module processes sales
5. ML model forecasts demand
6. Charts generated using Matplotlib

---

## 📊 Forecast Example

=========== SALES FORECAST ===========

Laptop  
Current Month : 8  
Next Month    : 10  

Phone  
Current Month : 5  
Next Month    : 6  

Mouse  
Current Month : 42  
Next Month    : 47  

LG Monitor 32  
Current Month : 14  
Next Month    : 16  

---

## 📈 Future Improvements

- Web dashboard (Flask / Django)
- Real-time stock alerts
- Advanced ML models (ARIMA / XGBoost)
- REST API integration
- Cloud deployment (Azure / AWS)

---

## 👨‍💻 Author

Enterprise Inventory Analytics System  
Built for learning full-stack backend + ML + SQL integration

---

## ⭐ Highlights

- Inventory + Sales + Forecasting system
- Real SQL Server integration
- Machine learning prediction model
- Professional CLI dashboard
- Data visualization with charts