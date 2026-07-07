# Olist E-commerce Data Analysis Project

## Overview
This project provides an Exploratory Data Analysis (EDA) of the [Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce). The goal was to transform raw relational data into actionable business insights regarding logistics efficiency, sales trends, and customer behavior.

## Tech Stack
* **Languages:** Python
* **Data Manipulation:** Pandas
* **Database & SQL:** SQLAlchemy, SQLite3
* **Visualization:** Seaborn, Matplotlib
* **Environment:** PyCharm (for scripts), Jupyter Notebooks (for EDA)
* **Version Control:** Git & GitHub


## About the Dataset
* **Source:** [Kaggle - Olist Dataset](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)
* **License:** [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)
* **Description:** A dataset containing information on 100k orders from 2016 to 2018 made at multiple marketplaces in Brazil.

## Methodology
The project follows a standard data science workflow:
1. **Data Preparation:** Loading data, cleaning types, and handling missing values.
2. **SQL Integration:** Using SQLite and `pandas` to query the relational structure of the database.
3. **Visualization:** Applying `seaborn` and `matplotlib` to identify trends, distributions, and outliers.

## Analysis Summary
<table>
  <thead>
    <tr>
      <th style="text-align: left;">Section</th>
      <th style="text-align: left;">Analysis Question</th>
      <th style="text-align: left;">Visualization Type</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>Part 1: Finance & Scale</b></td>
      <td>1.1 Monthly Sales Trend</td>
      <td>Line Chart</td>
    </tr>
    <tr>
      <td rowspan="2"><b>Part 2: Core Business</b></td>
      <td>2.1 Top Product Categories</td>
      <td>Dual-Panel Horizontal Bar Chart</td>
    </tr>
    <tr>
      <td>2.2 Payment Method Analysis</td>
      <td>Pie Chart </td>
    </tr>
    <tr>
      <td rowspan="3"><b>Part 3: Logistics & Operations</b></td>
      <td>3.1 Delivery Time by State</td>
      <td>Box Plot</td>
    </tr>
    <tr>
      <td>3.2 Freight vs. Product Value</td>
      <td>Grouped Bar Chart</td>
    </tr>
    <tr>
      <td>3.3 Delivery Time vs. Customer Satisfaction</td>
      <td>Bar Chart </td>
    </tr>
  </tbody>
</table>

##  Key Findings
*The following insights were derived from the analysis of the Olist e-commerce dataset:*
###  Part 1: Finance & Business Scale (Macro View)
### 1.1 Monthly Sales Trend:
* **Aggressive Expansion:** Throughout 2017, the platform demonstrated rapid market penetration, scaling monthly revenue predictably from **100k BRL** to over **600k BRL**.
* **Seasonal Dependency:** November 2017 marks an absolute historical peak (nearly **1M BRL**), proving that Black Friday promotions are a massive, singular driver for Olist's yearly revenue model.
* **Market Maturity:** In 2018, the initial explosive growth transitioned into a stable, high-volume plateau, consistently generating between **850k and 1M BRL** in monthly revenue.
* **Data Boundary Optimization:** Trailing data from September and October 2018 was deliberately excluded from the analysis. These months contain incomplete tracking periods in the raw dataset, which would artificially distort the trend line downward. Cutting the timeline at August 2018 ensures data integrity.

<img src="images/Monthly_Sales_Trend.png" width="800" />  

### Part 2: Sales Structure & Payment Mechanics
### 2.1 Top Product Categories:
* **Volume vs. Value Kings:** While `cama_mesa_banho` leads the platform in total units sold, `beleza_saude` takes the #1 spot in total revenue, capturing the highest financial share of the marketplace.
* **High-AOV Premium Shift:** `relogios_presentes` demonstrates a massive high-ticket multiplier; despite sitting lower at #7 in transaction volume, it represents the #2 largest revenue stream for Olist.
* **Hidden Gems Discovered:** Separating the metrics revealed categories like `cool_stuff` and `brinquedos` within the top financial earners. These high-margin/high-price categories scale the business without requiring unsustainable transactional volume.
* **Operational Strategy:** High-volume categories maintain customer acquisition loops and shipping ecosystem activity, while high-value electronics, gifts, and health products scale total marketplace GMV.
  
<img src="images/Top_Product_Categories.png" width="800" />

### 2.2 Payment Method Analysis:
   [wniosek]
  
<img src="images/Payment_Method_Analysis.png" width="800" />

### Part 3: Operational Efficiency & Logistics

### 3.1 Logistics Performance: 
* **Regional Disparities:** The economic core (**SP**, **MG**, **PR**) enjoys highly efficient logistics with median delivery times under **10–12 days**. In contrast, northern and remote states (**AP**, **RR**, **AM**) face severe bottlenecks, with medians spiking to **20–30 days**.
* **High Volatility:** Remote regions suffer from extreme unpredictability (wider interquartile ranges), making delivery promises highly unreliable for customers in those areas.
* **Volume-Driven Failures:** While major hubs like **SP** and **RJ** are fast on average, they experience a high absolute volume of severe outliers (orders stretching to **80+ days**), highlighting a critical edge-case failure mode in high-density areas.
* **Analytical Limitation:** Delivery times were measured end-to-end (purchase to delivery). A critical next step for the business would be to isolate courier transit time from internal merchant fulfillment speed to precisely target the root cause of these delays.
 
<img src="images/Logistics_Performance.png" width="800" />

### 3.2 Freight vs. Product Value:
   [wniosek]
  
<img src="images/Freight_vs_Product_Value.png" width="800" />

### 3.3 Delivery Time vs. Customer Satisfaction: 
   [wniosek]
  
<img src="images/Q6.png" width="800" />


## How to Run
1. **Clone the repository:**
   ```bash
   git clone https://github.com/Chrzanisko/data-driven-ecommerce.git
   cd data-driven-ecommerce
2. **Install dependecies:**
   ```bash
   pip install -r requirements.txt
3. **Data Setup:  <br>**
   Download the Olist dataset from Kaggle. Extract all .csv files and place them into the data/ directory.
   <br> <br>
4. **Initialize Database:**
   ```bash
   python src/clear_and_load_data.py
5. **Analyze: <br>**
   Open notebooks/eda.ipynb in your IDE and run the cells sequentially to perform the analysis.