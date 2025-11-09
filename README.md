# 💹 SRM Finance — Stock Analytics Dashboard

A **Flask-based Data Analytics web application** for analyzing, visualizing, and managing stock portfolios.  
This project provides a complete analytical view of stock market transactions and portfolio performance through **data processing, statistical analysis, visualization, and dashboard generation**.

Users can simulate **buying and selling stocks**, track real-time portfolio value, analyze historical performance, and export an **interactive Excel dashboard** with embedded charts and insights powered by **pandas, numpy, matplotlib, and openpyxl**.

## 📊 Project Overview

The **SRM Finance — Stock Analytics Dashboard** is a comprehensive data-driven platform that merges stock trading simulation with portfolio analytics.

It allows users to:

- View real-time stock quotes fetched via API.
    
- Record buy/sell transactions in a persistent database.
    
- Generate analytical summaries of portfolio performance.
    
- Visualize key trends with dynamic charts.
    
- Export results as a professionally formatted Excel dashboard.
    

This system serves as both a **financial analytics tool** and a **data visualization platform**, designed to deliver insights into trading behavior, investment growth, and risk exposure.

---

## 📁 Dataset Information

### **Data Sources**

- **Stock Quotes API:** Retrieves real-time or historical price data (symbol, open, high, low, close, volume).
    
- **Transaction Logs:** Captures all buy/sell activities performed by users.
    
- **Portfolio Snapshots:** Daily tracking of total portfolio value, holdings, and cash balance.
    

### **Files Used**

|File|Description|
|---|---|
|`transactions.csv`|Contains all user transactions including buy/sell data|
|`quotes_cache.csv`|Historical stock prices used for performance analysis|
|`portfolio_snapshots.csv`|Daily valuation of portfolios for trend analytics|

### **Data Columns**

#### transactions.csv

|Column|Type|Description|
|---|---|---|
|tx_id|Integer|Transaction ID|
|user_id|Integer|User identifier|
|timestamp|DateTime|Date & time of transaction|
|symbol|String|Stock symbol (e.g., AAPL)|
|side|String|'BUY' or 'SELL'|
|quantity|Integer|Number of shares traded|
|price|Float|Stock price at trade time|
|total|Float|Quantity × Price|
|fee|Float|Transaction fee applied|

#### quotes_cache.csv

|Column|Type|Description|
|---|---|---|
|symbol|String|Stock ticker|
|date|Date|Trading date|
|open|Float|Opening price|
|high|Float|Daily high|
|low|Float|Daily low|
|close|Float|Closing price|
|volume|Integer|Total trading volume|

#### portfolio_snapshots.csv

|Column|Type|Description|
|---|---|---|
|snapshot_id|Integer|Unique snapshot ID|
|user_id|Integer|User identifier|
|date|Date|Snapshot date|
|cash_balance|Float|Remaining cash in portfolio|
|holdings_value|Float|Total value of held stocks|
|total_value|Float|Sum of cash + holdings|

---

## 🛠️ Technology Stack

### **Languages & Frameworks**

- **Python (3.8+)**
    
- **Flask** — Web framework for app and API routes
    
- **SQLite + SQLAlchemy** — Database and ORM
    

### **Libraries for Data Analytics**

|Library|Purpose|
|---|---|
|`pandas`|Data manipulation, cleaning, and aggregation|
|`numpy`|Numerical computations and performance metrics|
|`matplotlib`|Chart creation and visual analytics|
|`openpyxl`|Excel report generation and dashboard export|
|`requests`|API data fetching|
|`python-dotenv`|Environment variable management|

---

## 📈 Analysis Features

### **1. Data Quality Checks**

- Detect and handle missing values and duplicates
    
- Validate data types and transaction integrity
    
- Remove inconsistencies between trades and quotes
    

### **2. Aggregations & Metrics**

- **User Analysis:** Track total value, cash, and holdings over time
    
- **Symbol Analysis:** Compute trade volume, average buy/sell price, returns
    
- **Performance Metrics:**
    
    - Daily/Monthly returns
        
    - Total gain/loss
        
    - Portfolio volatility
        
    - Sharpe ratio
        
    - Maximum drawdown
        

### **3. Key Insights**

- Top-performing and worst-performing stocks
    
- Portfolio diversification by sector/symbol
    
- Daily and cumulative return trends
    
- Most traded stocks and user trading patterns
    
- Risk-adjusted performance indicators
    

### **4. Statistical Analysis**

- Average holding period per stock
    
- Win/loss ratio of completed trades
    
- Correlation between stock holdings
    
- Profitability by symbol and user
    

---

## 📊 Visual Analytics & Dashboard

The project automatically generates **six professional charts** using `matplotlib` and exports them along with datasets into a structured Excel dashboard.

### **Charts Generated**

1. **Portfolio Value Over Time (Line Chart)**  
    Shows how total value changes across dates.
    
2. **Holdings Allocation (Donut Chart)**  
    Visualizes portfolio composition by stock symbol.
    
3. **Top Gainers and Losers (Bar Chart)**  
    Displays performance ranking by % return.
    
4. **Trade Volume by Symbol (Horizontal Bar)**  
    Indicates trading activity for each stock.
    
5. **Return Distribution (Histogram)**  
    Shows spread of daily returns across all holdings.
    
6. **Cumulative Return vs Benchmark (Line Chart)**  
    Compares portfolio against market benchmark.
    

---

## 📊 Excel Dashboard

**Exported File:** `Finance_Analytics_Dashboard.xlsx`

**Dashboard Sheets:**

|Sheet|Description|
|---|---|
|**1. Cleaned Data**|All validated transaction and quote data|
|**2. Summary Statistics**|Key performance indicators (KPIs) and metrics|
|**3. Visual Dashboard**|All charts embedded in 2×3 grid layout|
|**4. Transaction History**|Detailed log of trades with filters|

**KPIs Displayed:**

- Current Portfolio Value
    
- Total Profit/Loss
    
- Average Daily Return
    
- Portfolio Volatility
    
- Sharpe Ratio
    
- Max Drawdown
    
- Top 5 Stocks by Value
    

---

## 🚀 How to Use

### **Installation**
```
git clone https://github.com/singhadi0/SRM-Finance
cd finance
pip install -r requirements.txt
```

### **Setup**

Create `.env` file in root directory:
```
FLASK_APP=app.py
FLASK_ENV=development
IEX_API_KEY=your_iex_api_key_here
DATABASE_URL=sqlite:///finance.db

```
### **Run the Web App**
```
flask run

Visit `http://127.0.0.1:5000` in your browser.
```
### **Generate Dashboard**

`python analytics/generate_dashboard.py`

This script will:

- Process `transactions.csv`, `portfolio_snapshots.csv`, and `quotes_cache.csv`
    
- Produce `Finance_Analytics_Dashboard.xlsx`
    
- Export all charts as PNG files under `static/charts/`
    


## 📂 Project Structure
```
Project/
│
├── app.py                        # Flask application
├── models.py                     # Database models (User, Transaction, Portfolio)
├── manage_db.py                  # Initialize DB and sample data
├── requirements.txt
├── .env
│
├── data/
│   ├── transactions.csv
│   ├── quotes_cache.csv
│   └── portfolio_snapshots.csv
│
├── analytics/
│   ├── generate_dashboard.py     # Analytics & report generator
│   ├── plotting.py               # Visualization functions
│   └── utils.py                  # Data cleaning, metrics, aggregation
│
├── static/
│   └── charts/                   # Generated chart images
│
├── templates/
│   ├── index.html
│   ├── dashboard.html
│   └── portfolio.html
└── README.md
```


## 📈 Sample Insights

Based on the generated analytics:

- **Top Performing Stock:** AAPL with +12.6% gain in the last 30 days
    
- **Most Traded Symbol:** TSLA with 450 total transactions
    
- **Portfolio Growth:** +8.3% month-over-month
    
- **Risk Measure:** Volatility at 2.4%, Sharpe ratio 1.32
    
- **Holdings Distribution:** Tech sector dominates with 58% allocation
    
- **Drawdown Analysis:** Max drawdown of -4.1% during last quarter
    

---

## 💡 Design Features

- **Professional Styling:** Clean, readable charts and formatted Excel sheets
    
- **Consistent Theme:** Blue-gray financial color palette
    
- **Readable Labels:** Clear axis titles and legends
    
- **High Resolution:** 300 DPI chart exports for reports or presentations
    
- **KPI Summary Sheet:** At-a-glance performance overview
    

---

## 🔧 Troubleshooting

|Issue|Solution|
|---|---|
|Missing module error|Run `pip install -r requirements.txt`|
|Excel file locked|Close Excel before running the script|
|Charts missing in Excel|Verify chart PNGs exist in `/static/charts/`|
|API fetch fails|Check IEX API key or use cached data in `/data/`|

---

## 💻 Future Enhancements

- Integration of **real-time stock data** with live portfolio updates
    
- **AI-based forecasting** for predicting short-term price trends
    
- **Automated alerts** for price changes, drawdowns, and performance milestones
    
- Interactive **web dashboard** using Plotly or Streamlit for dynamic charting
    
- **Advanced risk analytics** (VaR, volatility clustering, correlation maps)
    
- **Natural-language summaries** of portfolio insights and trends
    
- **User comparison analytics** for collaborative or competitive evaluation
    
- Automated **weekly PDF/Excel reports** with charts and KPIs
    
- Migration to a **database-driven analytics pipeline** for larger datasets
    
- **Mobile and API integration** for monitoring and updates on the go
    

---

## 👨‍💻 Author

**Created by:** Shivam Singh , Diljan Ansari , Sumaiya Fatima

**Date:** 09/11/2025  
**Contact:**  adityasinghrajput3234@gmail.com

---

## 📝 License

This project is for educational and analytical use only.

---

##  Acknowledgments

- Data processing: **pandas**, **numpy**
    
- Visualization: **matplotlib**
    
- Excel integration: **openpyxl**
    
- API Data: **IEX Cloud**
