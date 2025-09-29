# ============================================================================
# BANK CUSTOMER CHURN ANALYSIS - STREAMLIT DASHBOARD (BUG-FREE VERSION)
# ============================================================================
# Professional interactive dashboard for analyzing customer churn patterns

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import warnings
warnings.filterwarnings('ignore')

# ============================================================================
# PAGE CONFIGURATION
# ============================================================================
st.set_page_config(
    page_title="Bank Customer Churn Analysis",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================================
# DATA LOADING FUNCTION
# ============================================================================
@st.cache_data
def load_data():
    """
    Load the banking customer churn dataset from Kaggle
    """
    try:
        # Load your actual Kaggle dataset
        import kagglehub
        import os
        
        # Download the dataset
        path = kagglehub.dataset_download("radheshyamkollipara/bank-customer-churn")
        
        # Find CSV files in the downloaded directory
        csv_files = [f for f in os.listdir(path) if f.endswith('.csv')]
        
        if not csv_files:
            raise ValueError("No CSV files found in the dataset")
        
        # Load the first CSV file
        df = pd.read_csv(os.path.join(path, csv_files[0]))
        
        return df
        
    except Exception as e:
        st.error(f"Error loading data: {e}")
        st.info("Make sure you have kagglehub installed: pip install kagglehub")
        return None

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================
def safe_group_analysis(df, group_col, target_col='Exited'):
    """Safely perform groupby analysis with error handling"""
    if len(df) == 0 or group_col not in df.columns:
        return pd.DataFrame()
    
    try:
        result = df.groupby(group_col)[target_col].agg(['count', 'mean']).reset_index()
        result['churn_rate'] = result['mean'] * 100
        return result
    except Exception:
        return pd.DataFrame()

def create_safe_bar_chart(data, x_col, y_col, title, baseline=24.4):
    """Create bar chart with error handling"""
    if data.empty or len(data) == 0:
        return None
    
    fig = px.bar(
        data,
        x=x_col,
        y=y_col,
        title=title,
        text=y_col
    )
    
    fig.add_hline(y=baseline, line_dash="dash", line_color="orange", 
                 annotation_text=f"Baseline ({baseline}%)")
    fig.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
    fig.update_layout(showlegend=False, height=400)
    return fig

def create_binned_analysis(df, column, bins, labels):
    """Create binned analysis with proper error handling"""
    if len(df) == 0 or column not in df.columns:
        return pd.DataFrame()
    
    try:
        df_temp = df.copy()
        df_temp['BinCategory'] = pd.cut(df_temp[column], bins=bins, labels=labels)
        df_temp = df_temp.dropna(subset=['BinCategory'])
        
        if len(df_temp) == 0:
            return pd.DataFrame()
            
        result = df_temp.groupby('BinCategory')['Exited'].agg(['count', 'mean']).reset_index()
        result['churn_rate'] = result['mean'] * 100
        return result
    except Exception:
        return pd.DataFrame()

# ============================================================================
# MAIN DASHBOARD FUNCTION
# ============================================================================
def main():
    # Load data
    df = load_data()
    
    if df is None:
        st.error("Failed to load data")
        st.stop()
    
    # ============================================================================
    # SIDEBAR FILTERS
    # ============================================================================
    st.sidebar.header("Dashboard Filters")
    
    # Credit Score Filter
    credit_min, credit_max = int(df['CreditScore'].min()), int(df['CreditScore'].max())
    credit_range = st.sidebar.slider(
        "Credit Score Range",
        min_value=credit_min,
        max_value=credit_max,
        value=(credit_min, credit_max),
        step=10
    )
    
    # Balance Filter
    balance_max = int(df['Balance'].max())
    balance_range = st.sidebar.slider(
        "Balance Range ($)",
        min_value=0,
        max_value=balance_max,
        value=(0, balance_max),
        step=1000,
        format="$%d"
    )
    
    # Geography Filter
    geography_options = st.sidebar.multiselect(
        "Select Countries",
        options=df['Geography'].unique(),
        default=df['Geography'].unique()
    )
    
    # Age Filter
    age_range = st.sidebar.slider(
        "Age Range",
        min_value=int(df['Age'].min()),
        max_value=int(df['Age'].max()),
        value=(int(df['Age'].min()), int(df['Age'].max()))
    )
    
    # Apply Filters
    filtered_df = df[
        (df['CreditScore'] >= credit_range[0]) &
        (df['CreditScore'] <= credit_range[1]) &
        (df['Balance'] >= balance_range[0]) &
        (df['Balance'] <= balance_range[1]) &
        (df['Geography'].isin(geography_options)) &
        (df['Age'] >= age_range[0]) &
        (df['Age'] <= age_range[1])
    ]
    
    # ============================================================================
    # MAIN DASHBOARD HEADER
    # ============================================================================
    st.title("Bank Customer Churn Analysis Dashboard")
    st.markdown("### Interactive Analysis of Customer Retention Patterns")
    st.markdown("---")
    
    # Check if filtered data is empty
    if len(filtered_df) == 0:
        st.error("No data matches the selected filters. Please adjust your filter criteria.")
        return
    
    # ============================================================================
    # KEY METRICS ROW
    # ============================================================================
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        total_customers = len(filtered_df)
        st.metric("Total Customers", f"{total_customers:,}")
    
    with col2:
        churn_rate = (filtered_df['Exited'].sum() / len(filtered_df)) * 100
        st.metric("Churn Rate", f"{churn_rate:.1f}%", delta=f"{churn_rate - 24.4:.1f}%")
    
    with col3:
        avg_balance = filtered_df['Balance'].mean()
        st.metric("Avg Balance", f"${avg_balance:,.0f}")
    
    with col4:
        complaint_rate = (filtered_df['Complain'].sum() / len(filtered_df)) * 100
        st.metric("Complaint Rate", f"{complaint_rate:.1f}%")
    
    with col5:
        avg_satisfaction = filtered_df['Satisfaction Score'].mean()
        st.metric("Avg Satisfaction", f"{avg_satisfaction:.1f}/5")
    
    st.markdown("---")
    
    # ============================================================================
    # ANALYSIS TABS
    # ============================================================================
    tab1, tab2, tab3, tab4 = st.tabs([
        "Key Predictors", 
        "Customer Segments", 
        "Detailed Analysis",
        "Business Insights"
    ])
    
    # TAB 1: KEY PREDICTORS
    with tab1:
        st.header("Top Churn Predictors")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Complaints vs Churn")
            complaint_data = safe_group_analysis(filtered_df, 'Complain')
            
            if not complaint_data.empty:
                # Map 0,1 to meaningful labels
                complaint_data['Complaint_Label'] = complaint_data['Complain'].map({
                    0: 'No Complaints', 1: 'Filed Complaints'
                })
                
                fig = create_safe_bar_chart(
                    complaint_data, 'Complaint_Label', 'churn_rate', 
                    "Churn Rate by Complaint Status"
                )
                if fig:
                    st.plotly_chart(fig, use_container_width=True, key="complaint_chart")
            else:
                st.warning("No complaint data available for current filters")
        
        with col2:
            st.subheader("Satisfaction Score vs Churn")
            satisfaction_data = safe_group_analysis(filtered_df, 'Satisfaction Score')
            
            if not satisfaction_data.empty:
                fig = create_safe_bar_chart(
                    satisfaction_data, 'Satisfaction Score', 'churn_rate',
                    "Churn Rate by Satisfaction Score"
                )
                if fig:
                    st.plotly_chart(fig, use_container_width=True, key="satisfaction_chart")
            else:
                st.warning("No satisfaction data available for current filters")
        
        # Balance and Credit Analysis
        col3, col4 = st.columns(2)
        
        with col3:
            st.subheader("Balance Range vs Churn")
            balance_data = create_binned_analysis(
                filtered_df, 'Balance',
                bins=[0, 1, 50000, 100000, 150000, 300000],
                labels=['Zero', 'Low', 'Medium', 'High', 'Very High']
            )
            
            if not balance_data.empty:
                fig = create_safe_bar_chart(
                    balance_data, 'BinCategory', 'churn_rate',
                    "Churn Rate by Balance Range"
                )
                if fig:
                    st.plotly_chart(fig, use_container_width=True, key="balance_chart")
            else:
                st.warning("No balance data available for current filters")
        
        with col4:
            st.subheader("Credit Score vs Churn")
            credit_data = create_binned_analysis(
                filtered_df, 'CreditScore',
                bins=[300, 500, 600, 700, 800, 900],
                labels=['Poor', 'Fair', 'Good', 'Very Good', 'Excellent']
            )
            
            if not credit_data.empty:
                fig = create_safe_bar_chart(
                    credit_data, 'BinCategory', 'churn_rate',
                    "Churn Rate by Credit Score Range"
                )
                if fig:
                    st.plotly_chart(fig, use_container_width=True, key="credit_chart")
            else:
                st.warning("No credit score data available for current filters")
    
    # TAB 2: CUSTOMER SEGMENTS
    with tab2:
        st.header("Customer Segmentation Analysis")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Demographics")
            
            # Age groups
            age_data = create_binned_analysis(
                filtered_df, 'Age',
                bins=[18, 30, 40, 50, 60, 100],
                labels=['Young (18-30)', 'Adult (30-40)', 'Middle (40-50)', 'Mature (50-60)', 'Senior (60+)']
            )
            
            if not age_data.empty:
                fig = create_safe_bar_chart(
                    age_data, 'BinCategory', 'churn_rate',
                    "Churn Rate by Age Group"
                )
                if fig:
                    st.plotly_chart(fig, use_container_width=True, key="age_demo_chart")
            
            # Geography - Fixed to show churn rates instead of customer distribution
            geo_data = safe_group_analysis(filtered_df, 'Geography')
            if not geo_data.empty:
                fig = px.pie(
                    geo_data,
                    values='churn_rate',  # Changed from 'count' to 'churn_rate'
                    names='Geography',
                    title="Churn Rate by Geography"  # Updated title
                )
                fig.update_traces(textposition='inside', textinfo='percent+label')
                fig.update_layout(height=400)
                st.plotly_chart(fig, use_container_width=True, key="geography_pie_chart")
        
        with col2:
            st.subheader("Behavioral Patterns")
            
            # Products
            products_data = safe_group_analysis(filtered_df, 'NumOfProducts')
            if not products_data.empty:
                fig = create_safe_bar_chart(
                    products_data, 'NumOfProducts', 'churn_rate',
                    "Churn Rate by Number of Products"
                )
                if fig:
                    st.plotly_chart(fig, use_container_width=True, key="products_chart")
            
            # Activity Status
            activity_data = safe_group_analysis(filtered_df, 'IsActiveMember')
            if not activity_data.empty:
                activity_data['Activity_Label'] = activity_data['IsActiveMember'].map({
                    0: 'Inactive', 1: 'Active'
                })
                
                fig = create_safe_bar_chart(
                    activity_data, 'Activity_Label', 'churn_rate',
                    "Churn Rate by Activity Status"
                )
                if fig:
                    st.plotly_chart(fig, use_container_width=True, key="activity_chart")
    
    # TAB 3: DETAILED ANALYSIS
    with tab3:
        st.header("Interactive Variable Analysis")
        
        # Variable selector
        variable_options = {
            'Complaints': 'Complain',
            'Satisfaction Score': 'Satisfaction Score',
            'Balance': 'Balance',
            'Credit Score': 'CreditScore',
            'Number of Products': 'NumOfProducts',
            'Activity Status': 'IsActiveMember',
            'Age': 'Age',
            'Geography': 'Geography',
            'Gender': 'Gender',
            'Tenure': 'Tenure'
        }
        
        selected_var_name = st.selectbox("Select Variable to Analyze", list(variable_options.keys()))
        selected_var = variable_options[selected_var_name]
        
        # Analysis based on variable type
        if selected_var in ['Balance', 'CreditScore', 'Age', 'Tenure']:
            # Continuous variables - create bins
            if selected_var == 'Balance':
                analysis_data = create_binned_analysis(
                    filtered_df, selected_var, bins=5, 
                    labels=['Very Low', 'Low', 'Medium', 'High', 'Very High']
                )
            elif selected_var == 'CreditScore':
                analysis_data = create_binned_analysis(
                    filtered_df, selected_var,
                    bins=[300, 500, 600, 700, 800, 900],
                    labels=['Poor', 'Fair', 'Good', 'Very Good', 'Excellent']
                )
            elif selected_var == 'Age':
                analysis_data = create_binned_analysis(
                    filtered_df, selected_var,
                    bins=[18, 30, 40, 50, 60, 100],
                    labels=['Young', 'Adult', 'Middle', 'Mature', 'Senior']
                )
            else:  # Tenure
                analysis_data = create_binned_analysis(
                    filtered_df, selected_var,
                    bins=[0, 2, 4, 6, 8, 11],
                    labels=['New', 'Growing', 'Stable', 'Mature', 'Loyal']
                )
            
            x_column = 'BinCategory'
        else:
            # Categorical variables
            analysis_data = safe_group_analysis(filtered_df, selected_var)
            x_column = selected_var
        
        if not analysis_data.empty:
            col1, col2 = st.columns(2)
            
            with col1:
                # Churn rate chart
                fig = create_safe_bar_chart(
                    analysis_data, x_column, 'churn_rate',
                    f"Churn Rate by {selected_var_name}"
                )
                if fig:
                    st.plotly_chart(fig, use_container_width=True, key="detailed_churn_chart")
            
            with col2:
                # Customer count
                fig = px.bar(
                    analysis_data,
                    x=x_column,
                    y='count',
                    title=f"Customer Count by {selected_var_name}",
                    text='count'
                )
                fig.update_traces(texttemplate='%{text}', textposition='outside')
                fig.update_layout(height=400)
                st.plotly_chart(fig, use_container_width=True, key="detailed_count_chart")
            
            # Summary table
            st.subheader("Analysis Results")
            display_data = analysis_data[[x_column, 'count', 'churn_rate']].copy()
            display_data['churn_rate'] = display_data['churn_rate'].round(1)
            display_data.columns = ['Category', 'Customer Count', 'Churn Rate (%)']
            st.dataframe(display_data, use_container_width=True)
        else:
            st.warning("No data available for the selected variable with current filters")
    
    # TAB 4: BUSINESS INSIGHTS
    with tab4:
        st.header("Business Insights & Recommendations")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Critical Findings")
            
            # Complaint insights
            complaint_customers = filtered_df[filtered_df['Complain'] == 1]
            no_complaint_customers = filtered_df[filtered_df['Complain'] == 0]
            
            if len(complaint_customers) > 0 and len(no_complaint_customers) > 0:
                complaint_churn = complaint_customers['Exited'].mean() * 100
                no_complaint_churn = no_complaint_customers['Exited'].mean() * 100
                st.write(f"• **Complaint Impact**: {complaint_churn:.1f}% vs {no_complaint_churn:.1f}%")
            
            # Satisfaction insights
            low_sat = filtered_df[filtered_df['Satisfaction Score'].isin([1, 2])]
            high_sat = filtered_df[filtered_df['Satisfaction Score'].isin([4, 5])]
            
            if len(low_sat) > 0 and len(high_sat) > 0:
                low_sat_churn = low_sat['Exited'].mean() * 100
                high_sat_churn = high_sat['Exited'].mean() * 100
                st.write(f"• **Satisfaction Impact**: Low (1-2): {low_sat_churn:.1f}% vs High (4-5): {high_sat_churn:.1f}%")
        
        with col2:
            st.subheader("Recommended Actions")
            st.write("**Immediate Priority:**")
            st.write("• Implement complaint resolution protocol")
            st.write("• Survey low satisfaction customers")
            st.write("• Re-engagement campaigns for inactive accounts")
            
            st.write("**Strategic Initiatives:**")
            st.write("• Premium service for high balance customers")
            st.write("• Cross-selling opportunities")
            st.write("• Targeted retention programs")
        
        # Dataset summary
        st.subheader("Dataset Summary")
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Total Customers", f"{len(filtered_df):,}")
        
        with col2:
            overall_churn = (filtered_df['Exited'].mean() * 100)
            st.metric("Overall Churn Rate", f"{overall_churn:.1f}%")
        
        with col3:
            avg_credit = filtered_df['CreditScore'].mean()
            st.metric("Avg Credit Score", f"{avg_credit:.0f}")
        
        with col4:
            avg_products = filtered_df['NumOfProducts'].mean()
            st.metric("Avg Products per Customer", f"{avg_products:.1f}")

# ============================================================================
# RUN THE APP
# ============================================================================
if __name__ == "__main__":
    main()