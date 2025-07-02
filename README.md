# 📊 Task 5: Sales Data Analysis using Pandas

## 🎯 Objective
Analyze **sales dataset (`sales dataset.xlsx`) using Pandas** to:
- Extract sales insights
- Visualize trends
- Practice real-world Python data analysis

---

## 🛠 Tools Used
- Python 3
- Pandas
- Matplotlib
- Seaborn
- Jupyter Notebook / Python script

---

## 📂 Dataset Columns
- `Order ID`
- `Order Date`
- `Customer Name`
- `City`, `Country`, `State`, `Region`
- `Segment`, `Ship Mode`
- `Category`, `Sub-Category`
- `Product Name`
- `Cost`, `Sales`, `Profit`, `Quantity`

---

## 🚀 Steps Performed

✅ Loaded the Excel file using `pd.read_excel()`  
✅ Inspected data using `.head()`, `.info()`, `.describe()`, `.isnull()`  
✅ Ensured `Order Date` is converted to `datetime`  
✅ Created `Month` column for monthly analysis

✅ **Analysis Performed:**
- **Total Sales per Month:** Line plot of sales trends.
- **Sales by Category:** Bar plot to visualize high-performing categories.
- **Sales by Sub-Category:** Bar plot to analyze sub-segment sales.
- **Top 10 Products by Sales:** Identify top revenue generators.
- **Top 10 Products by Quantity Sold:** Identify fast-moving products.
- **Regional Sales Distribution:** Pie chart to visualize region-wise sales share.

✅ Generated **insights-ready plots for visual understanding**.

---

## 📈 Visualizations Included

- 📈 Monthly Sales Trend (Line Plot)
- 📊 Sales by Category (Bar Plot)
- 📊 Sales by Sub-Category (Bar Plot)
- 📊 Top 10 Products by Sales (Bar Plot)
- 📊 Top 10 Products by Quantity Sold (Bar Plot)
- 🥧 Regional Sales Distribution (Pie Chart)

---


## 📝 Usage

1️⃣ Ensure you have:
- `sales dataset.xlsx` in your working directory.
- Required Python libraries (`pandas`, `matplotlib`, `seaborn`) installed.

2️⃣ Run:
```bash
python salesAnalysis.py
