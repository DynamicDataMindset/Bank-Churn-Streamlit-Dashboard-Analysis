# 🏦 Bank Customer Churn Analysis

A comprehensive exploratory data analysis project identifying key factors that predict customer churn in banking, with actionable business insights and an interactive dashboard.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Complete-success.svg)

---

## 📑 Table of Contents

- [Project Overview](#-project-overview)
- [Key Findings](#-key-findings)
- [Dataset Information](#-dataset-information)
- [Technologies Used](#-technologies-used)
- [Project Structure](#-project-structure)
- [Quick Start](#-quick-start)
- [Analysis Results](#-analysis-results)
- [Dashboard Features](#-dashboard-features)
- [Business Recommendations](#-business-recommendations)
- [Methodology](#-methodology)
- [Future Enhancements](#-future-enhancements)
- [Contributing](#-contributing)
- [License](#-license)
- [Contact](#-contact)

---

## 🎯 Project Overview

This project analyzes customer churn patterns using a dataset of **10,000 bank customers** to identify the primary factors that predict customer departure. The analysis reveals critical insights that can help financial institutions reduce customer attrition through **targeted retention strategies**.

### Business Impact

- **High-Risk Customers Identified**: ~2,440 customers with >50% churn probability
- **Customer Segmentation**: Three-tier risk classification system
- **Actionable Insights**: Data-driven retention strategies with measurable ROI

---

## 🔑 Key Findings

| Factor | Impact | Churn Rate |
|--------|--------|------------|
| **Customer Complaints** | 🔴 Critical | 90% (vs 15% baseline) |
| **Satisfaction Score 2** | 🔴 Critical | 55% (vs 8% at score 5) |
| **Low Account Balance** | 🟡 High | 34.7% (vs 19.9% medium balance) |
| **Poor Credit Score** | 🟡 High | 2x higher than excellent credit |

> **Baseline Churn Rate**: 24.4%

---

## 📊 Dataset Information

- **Source**: [Kaggle - Bank Customer Churn Dataset](https://www.kaggle.com/datasets/radheshyamkollipara/bank-customer-churn)
- **Size**: 10,000 customers × 18 features
- **Target Variable**: `Exited` (0 = Retained, 1 = Churned)

### Key Variables

#### Primary Predictors
- `Complain` - Customer complaint status
- `SatisfactionScore` - Customer satisfaction (1-5 scale)
- `Balance` - Account balance levels
- `CreditScore` - Credit score ranges

#### Supporting Variables
- `NumOfProducts` - Number of bank products
- `IsActiveMember` - Account activity status
- `Age` - Customer demographics
- `Geography` - Customer location
- `Tenure` - Relationship length
- `EstimatedSalary` - Income levels

---

## 🛠️ Technologies Used

```
Languages:      Python 3.8+
Data Analysis:  Pandas, NumPy
Visualization:  Matplotlib, Seaborn, Plotly
Dashboard:      Streamlit, ipywidgets
Environment:    Google Colab / Jupyter Notebook
Data Source:    KaggleHub API
```

---

## 📁 Project Structure

```
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
├── data/
│   └── .gitkeep                              # Dataset downloaded via KaggleHub
│
├── requirements.txt                          # Python dependencies
├── README.md                                 # Project documentation
├── LICENSE                                   # MIT License
└── .gitignore                                # Git ignore file
```

---

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/[your-username]/bank-customer-churn-analysis.git
cd bank-customer-churn-analysis
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Analysis Notebook

```bash
jupyter notebook notebooks/Bank_Customer_Churn_Analysis.ipynb
```

### 4. Launch Interactive Dashboard

```bash
streamlit run dashboard/churn_dashboard.py
```

---

## 📈 Analysis Results

### Churn Predictor Ranking

1. **Complaints** → 90% churn rate (vs 15% without complaints)
2. **Satisfaction Score** → Score 2 shows 55% churn (vs 8% at score 5)
3. **Account Balance** → Low balance: 34.7% churn (vs 19.9% medium)
4. **Credit Score** → Poor credit: 2x higher churn than excellent credit

### Customer Segmentation

| Risk Level | % of Customers | Characteristics |
|------------|----------------|-----------------|
| 🔴 **Critical** | ~10% | Low satisfaction + complaints |
| 🟡 **Medium** | ~15% | Low balance + poor credit |
| 🟢 **Low** | ~75% | Stable tenure, no complaints |

---

## 🎨 Dashboard Features

The interactive Streamlit dashboard includes:

- ✅ **Real-time Filtering** - Filter by demographics & financial metrics
- ✅ **Interactive Visualizations** - Dynamic churn pattern analysis
- ✅ **Risk Assessment Tools** - Flag high-risk customers automatically
- ✅ **Business Metrics** - ROI calculations & strategic recommendations

### Dashboard Preview

> *Add screenshots here*

**Live Demo**: [Streamlit App Link](#) *(Coming Soon)*

---

## 💡 Business Recommendations

### Immediate Actions (30 Days)

- 🎯 **Complaint Resolution**: Implement faster response systems (potential 75% churn reduction)
- 🎯 **Target Dissatisfied Customers**: Personalized offers for satisfaction scores ≤2
- 🎯 **Balance-Based Alerts**: Proactive outreach for low-balance accounts

### Strategic Initiatives (90 Days)

- 📊 **Loyalty Programs**: Balance-based rewards to increase retention
- 📊 **Credit Education**: Financial literacy programs + product bundling
- 📊 **Engagement Campaigns**: Reactivate inactive members with targeted incentives

---

## 🔬 Methodology

1. **Data Quality Assessment** - Missing values, duplicates, data type validation
2. **Exploratory Data Analysis** - Distribution analysis, correlation studies, visual insights
3. **Hypothesis Testing** - Statistical validation of churn drivers
4. **Customer Segmentation** - Risk profiling and tier classification
5. **Business Impact Analysis** - ROI estimation and actionable recommendations

---

## 🚀 Future Enhancements

- [ ] Predictive ML models (Random Forest, XGBoost, Neural Networks)
- [ ] Real-time churn monitoring dashboard
- [ ] A/B testing framework for retention strategies
- [ ] Customer Lifetime Value (CLV) analysis
- [ ] API integration for automated reporting

---

## 🤝 Contributing

This project was developed as part of a data science internship. Contributions are welcome!

### How to Contribute

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **Dataset**: [Radheshyam Kollipara](https://www.kaggle.com/radheshyamkollipara) on Kaggle
- **Internship**: Hex Softwares for project guidance and mentorship
- **Community**: Thanks to the open-source data science community

---

## 📞 Contact

**Boniface Ramushu**

- 📧 Email: bonifaceramushu28@gmail.com
- 💼 LinkedIn: [Your LinkedIn Profile](#)
- 🌐 Portfolio: [Your Portfolio Website](#)
- 🐙 GitHub: [@your-username](https://github.com/your-username)

---

<div align="center">

**⭐ Star this repository if you find it helpful!**

Made with ❤️ by Boniface Ramushu

</div>
