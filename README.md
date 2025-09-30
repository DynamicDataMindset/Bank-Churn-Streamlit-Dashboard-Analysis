# Bank Customer Churn Analysis

A comprehensive exploratory data analysis project identifying key factors that predict customer churn in banking, with actionable business insights and an interactive dashboard.

---

## 🎯 Project Overview

This project analyzes customer churn patterns using a dataset of **10,000 bank customers** to identify the primary factors that predict customer departure. The analysis reveals critical insights that can help financial institutions reduce customer attrition through **targeted retention strategies**.

### 🔑 Key Findings
- Customers who file complaints have **90% churn rate vs 15%** for non-complainers  
- **Satisfaction Score 2** demonstrates the highest churn among all satisfaction levels  
- **Low balance customers** show **34.7% churn rate** vs **19.9%** for medium balance customers  
- Customers with **poor credit scores** exhibit significantly higher churn than excellent credit customers  

---

## 📊 Dataset Information

- **Source**: [Kaggle - Bank Customer Churn Dataset](https://www.kaggle.com/datasets/radheshyamkollipara/bank-customer-churn)  
- **Size**: 10,000 customers × 18 features  
- **Target Variable**: Customer churn (`Exited`: 0/1)  
- **Baseline Churn Rate**: **24.4%**

### Variables Analyzed
**Primary Predictors**
- `Complain`: Customer complaint status  
- `SatisfactionScore`: Customer satisfaction (1–5 scale)  
- `Balance`: Account balance levels  
- `CreditScore`: Credit score ranges  

**Supporting Variables**
- `NumOfProducts`: Number of bank products  
- `IsActiveMember`: Account activity status  
- `Age`: Customer demographics  
- `Geography`: Customer location  
- `Tenure`: Relationship length  
- `EstimatedSalary`: Income levels  

---

## 🛠️ Technologies Used

- **Python 3.8+**
- **Data Analysis**: Pandas, NumPy  
- **Visualization**: Matplotlib, Seaborn, Plotly  
- **Dashboard**: ipywidgets (in-notebook), Streamlit (external)  
- **Environment**: Google Colab / Jupyter Notebook  
- **Data Source**: KaggleHub  

---

## 📁 Project Structure


Bank-Customer-Churn-Analysis/
│
├── notebooks/
│   └── Bank_Customer_Churn_Analysis.ipynb    # Main analysis notebook
│
├── dashboard/
│   └── churn_dashboard.py                    # Interactive Streamlit dashboard
│
├── reports/
│   └── Project_Report.pdf                    # Detailed analysis report
│
├── requirements.txt                          # Python dependencies
├── README.md                                 # Project documentation
└── .gitignore                                # Git ignore file


🚀 Quick Start
1. Clone the Repository
   
```bash
Copy code
git clone https://github.com/[your-username]/bank-customer-churn-analysis.git
cd bank-customer-churn-analysis
```
3. Install Dependencies
```bash
Copy code
pip install -r requirements.txt
```
4. Run the Analysis Notebook
```bash
Copy code
jupyter notebook notebooks/Bank_Customer_Churn_Analysis.ipynb
```
5. Launch Interactive Dashboard
```bash
Copy code
streamlit run dashboard/churn_dashboard.py
```

📈 Key Analysis Results

1) Churn Predictor Ranking
-Complaints – Customers with complaints churned at 90% vs 15% baseline

-Satisfaction Score – Score = 2 linked to 55% churn vs 8% at score 5

-Balance – Low balance customers churned at 34.7% vs 19.9% medium balance

-Credit Score – Poor credit category churned 2x higher than excellent credit

3) Business Impact
-High-Risk Customers: ~2,440 customers identified with >50% churn probability
-Potential Revenue Saved: $[Insert Estimate] annually via retention efforts
-ROI: [Insert %] return on customer retention investment

4) Segmentation
-Critical Risk: ~10% of customers (low satisfaction + complaints)
-Medium Risk: ~15% of customers (low balance, poor credit)
-Low Risk: ~75% of customers (stable tenure, no complaints)

5) Interactive Dashboard Features
-The Streamlit dashboard includes:
-Real-time filtering by demographics & financial metrics
-Interactive churn pattern visualizations
-Risk assessment tools to flag high-risk customers
-Business metrics with ROI calculations & recommendations

6) Dashboard Preview
(Add screenshots here)

7) Business Recommendations
-Immediate Actions (30 days)
-Implement faster complaint resolution (churn drops ~75% without complaints)
-Target dissatisfied customers (Score ≤2) with personalized offers
-Strategic Initiatives (90 days)
-Introduce balance-based loyalty programs
-Launch credit score education + product bundling to increase stickiness
-Expand customer engagement for inactive members

8) Methodology
-Data Quality Assessment – Checked missing values, duplicates, dtypes
-EDA – Distribution analysis, correlations, visual insights
-Hypothesis Testing – Validated drivers via groupby + chi-square tests
-Segmentation – Customer risk profiling into tiers
-Business Impact – ROI estimation & actionable recommendations

9) Future Enhancements
-Predictive ML models with scikit-learn
-Real-time churn monitoring dashboards
-A/B testing framework for retention strategies
-Customer Lifetime Value (CLV) analysis

10) Documentation
-Detailed Report: reports/Project_Report.pdf
-Code: Fully commented notebook + Streamlit app
-Methodology Notes: Included inline with code

11) Contributing
-This project was developed as part of a data science internship.
-Issues: Open issues for bugs or enhancements
-Pull Requests: Contributions welcome

12) Contact: [Your Email]

13) License
Licensed under the MIT License – see the LICENSE file for details.

14) Acknowledgments
Dataset: Radheshyam Kollipara on Kaggle

15) Internship: Hex Softwares for project guidance

📞 Contact
Author: Boniface Ramushu
Email:  bonifaceramushu28@gmail.com
LinkedIn: 
Portfolio: 

🎨 Dashboard Demo
[Add deployed Streamlit app link]

This project demonstrates end-to-end data science capability: from exploratory analysis to business insights to dashboard deployment.
