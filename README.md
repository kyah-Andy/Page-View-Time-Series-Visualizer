# 📈 Page View Time Series Visualizer

This project is a data visualization project from **freeCodeCamp** that analyzes daily page view data from the **freeCodeCamp.org forum**.  
Using **Pandas**, **Matplotlib**, and **Seaborn**, the project generates multiple visualizations to understand trends, growth, and seasonality in forum traffic.

---

## 📌 Project Overview

The dataset contains the number of page views each day on the freeCodeCamp forum from:

📅 **2016-05-09** to **2019-12-03**

This project produces three different charts:

- **Line Chart** → Daily traffic trend over time  
- **Bar Chart** → Average monthly page views grouped by year  
- **Box Plots** → Yearly distribution (trend) and monthly distribution (seasonality)

---

## 🛠️ Tools & Libraries Used

- Python  
- Pandas  
- Matplotlib  
- Seaborn  

---

## 📂 Project Structure

```bash
Page View Time Series Visualizer/
│
├── Docs/
│   ├── line_plot.png
│   ├── bar_plot.png
│   └── box_plot.png
│
├── fcc-forum-pageviews.csv
├── main.py
├── test_module.py
├── time_series_visualizer.py
└── README.md
```

---

## 📊 Visualizations Generated
✅ 1. Line Plot

Shows daily page views from May 2016 to Dec 2019.

📌 Output: Docs/line_plot.png

✅ 2. Bar Plot

Shows average daily page views for each month grouped by year.

📌 Output: Docs/bar_plot.png

✅ 3. Box Plots

Two side-by-side box plots:

Year-wise Box Plot (Trend)
Month-wise Box Plot (Seasonality)

📌 Output: Docs/box_plot.png
---

## 🧹 Data Cleaning

To remove extreme outliers, the dataset is cleaned by filtering out:

- the top 2.5% of page view values
- the bottom 2.5% of page view values

This produces more accurate and readable visualizations.

---

## ▶️ How to Run the Project
1️⃣ Install Dependencies  
```
pip install pandas matplotlib seaborn
```
2️⃣ Run the Program  
```
python main.py
```
This will generate the following image files:
```
Docs/line_plot.png
Docs/bar_plot.png
Docs/box_plot.png
```

✅ Running Unit Tests

To verify that your functions return the expected plot objects, run:
```
python -m unittest test_module.py
```
If successful, the output should display:
```
OK
```
## 📁 Dataset Source

The dataset file used in this project is:

fcc-forum-pageviews.csv

This dataset contains daily forum page view counts used for visualization and trend analysis.

### 🚀 Author

### **Andy Razon**  
🌐 Website: andyrazon.website
