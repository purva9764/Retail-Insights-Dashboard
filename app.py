
import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

# =========================================
# 1. PAGE CONFIGURATION
# =========================================

st.set_page_config(
    page_title="Retail Insights | Analytics",
    page_icon="✨",
    layout="wide"
)

# =========================================
# 2. CUSTOM DESIGN
# =========================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap');

* {
    font-family: 'Poppins', sans-serif;
}

.stApp {
    background: linear-gradient(135deg, #F8F3FF, #FCEFFA, #F1EDFF);
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #E9DDF8, #F8EAF5);
}

h1, h2, h3 {
    color: #8064A2;
    font-weight: 700;
}

p {
    color: #776A85;
}

div[data-testid="stMetric"] {
    background: rgba(255,255,255,0.9);
    padding: 20px;
    border-radius: 18px;
    border: 1px solid #E8DDF3;
    box-shadow: 0 7px 22px rgba(128,100,162,0.10);
}

.stButton button {
    background: linear-gradient(90deg, #A98ACB, #D99BCB);
    color: white;
    border-radius: 12px;
    border: none;
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)

# =========================================
# 3. LOAD AND CLEAN DATA
# =========================================

DATA_PATH = Path(__file__).parent / "data" / "retail_sales.csv"

if not DATA_PATH.exists():
    st.error("Dataset not found. Check data/retail_sales.csv")
    st.stop()

raw_df = pd.read_csv(DATA_PATH)

required_columns = [
    "Order_ID",
    "Order_Date",
    "Product",
    "Category",
    "Region",
    "Sales",
    "Profit"
]

missing_columns = [
    col for col in required_columns
    if col not in raw_df.columns
]

if missing_columns:
    st.error(f"Missing columns: {missing_columns}")
    st.stop()

# Create a copy for quality checking
quality_df = raw_df.copy()

# Convert data types
quality_df["Order_Date"] = pd.to_datetime(
    quality_df["Order_Date"], errors="coerce"
)

quality_df["Sales"] = pd.to_numeric(
    quality_df["Sales"], errors="coerce"
)

quality_df["Profit"] = pd.to_numeric(
    quality_df["Profit"], errors="coerce"
)

# Data cleaning
df = quality_df.dropna(
    subset=[
        "Order_ID",
        "Order_Date",
        "Product",
        "Category",
        "Region",
        "Sales",
        "Profit"
    ]
).drop_duplicates().copy()

if df.empty:
    st.error("No valid records found after data cleaning.")
    st.stop()

# =========================================
# 4. SIDEBAR NAVIGATION
# =========================================

st.sidebar.markdown("# ✨ Retail Insights")
st.sidebar.caption("SMART SALES ANALYTICS")
st.sidebar.divider()

page = st.sidebar.radio(
    "EXPLORE PAGES",
    [
        "🏠 Home",
        "📊 Dashboard",
        "📈 Sales Analysis",
        "📋 Dataset",
        "ℹ️ About Project"
    ]
)

st.sidebar.divider()

st.sidebar.markdown("### 💜 Project Details")
st.sidebar.caption("Python Data Analytics")
st.sidebar.caption("Interactive Dashboard")
st.sidebar.caption("Built with Streamlit")

# =========================================
# 5. HOME PAGE
# =========================================

if page == "🏠 Home":

    st.markdown(
        "<h1 style='text-align:center;'>"
        "✨ RETAIL INSIGHTS ✨</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<h3 style='text-align:center;'>"
        "Discover the Story Behind Your Sales"
        "</h3>",
        unsafe_allow_html=True
    )

    st.divider()

    st.markdown("### 💜 Welcome to Your Smart Analytics Experience")

    st.write(
        "Transform retail data into meaningful business insights. "
        "Explore sales trends, analyze products and discover "
        "business performance through interactive visualizations."
    )

    st.markdown("### 🚀 Explore What's Inside")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.info(
            "📊 **Data Analysis**\n\n"
            "Explore and understand retail data."
        )

    with c2:
        st.success(
            "📈 **Smart Visuals**\n\n"
            "Discover trends through interactive charts."
        )

    with c3:
        st.warning(
            "💡 **Business Insights**\n\n"
            "Find useful patterns in sales."
        )

    st.divider()

    st.markdown("### ✨ Project at a Glance")

    c1, c2, c3 = st.columns(3)

    c1.metric("Total Orders", df["Order_ID"].nunique())
    c2.metric("Total Sales", f"₹{df['Sales'].sum():,.0f}")
    c3.metric("Total Profit", f"₹{df['Profit'].sum():,.0f}")

    st.info("👈 Select Dashboard from the sidebar to explore your data.")

# =========================================
# 6. DASHBOARD PAGE
# =========================================

elif page == "📊 Dashboard":

    st.title("📊 Sales Dashboard")
    st.caption("Overview of retail business performance.")

    categories = sorted(
        df["Category"].dropna().unique().tolist()
    )

    selected_category = st.selectbox(
        "Select Product Category",
        ["All"] + categories
    )

    filtered = df.copy()

    if selected_category != "All":
        filtered = filtered[
            filtered["Category"] == selected_category
        ]

    total_sales = filtered["Sales"].sum()
    total_profit = filtered["Profit"].sum()
    total_orders = filtered["Order_ID"].nunique()

    average_order = (
        total_sales / total_orders
        if total_orders > 0 else 0
    )

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("💰 Total Sales", f"₹{total_sales:,.0f}")
    c2.metric("📈 Total Profit", f"₹{total_profit:,.0f}")
    c3.metric("🛍️ Total Orders", total_orders)
    c4.metric("🧾 Average Order", f"₹{average_order:,.0f}")

    st.divider()

    left, right = st.columns(2)

    with left:

        st.subheader("Category-wise Sales")

        category_data = filtered.groupby(
            "Category", as_index=False
        )["Sales"].sum()

        fig = px.bar(
            category_data,
            x="Category",
            y="Sales",
            color="Category",
            title="Sales by Product Category",
            template="plotly_white"
        )

        st.plotly_chart(fig, use_container_width=True)

    with right:

        st.subheader("Monthly Sales Trend")

        monthly = filtered.copy()

        monthly["Month"] = (
            monthly["Order_Date"]
            .dt.to_period("M")
            .astype(str)
        )

        monthly_data = monthly.groupby(
            "Month", as_index=False
        )["Sales"].sum()

        fig2 = px.line(
            monthly_data,
            x="Month",
            y="Sales",
            markers=True,
            title="Monthly Sales Performance",
            template="plotly_white"
        )

        st.plotly_chart(fig2, use_container_width=True)

# =========================================
# 7. SALES ANALYSIS PAGE
# =========================================

elif page == "📈 Sales Analysis":

    st.title("📈 Business Analysis")

    st.caption(
        "Explore product performance and regional profitability."
    )

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Profit by Region")

        region_data = df.groupby(
            "Region", as_index=False
        )["Profit"].sum()

        fig = px.pie(
            region_data,
            names="Region",
            values="Profit",
            hole=0.45,
            title="Regional Profit Distribution",
            template="plotly_white"
        )

        st.plotly_chart(fig, use_container_width=True)

    with col2:

        st.subheader("Product Performance")

        product_data = df.groupby(
            "Product", as_index=False
        )["Sales"].sum().sort_values(
            "Sales", ascending=True
        )

        fig2 = px.bar(
            product_data,
            x="Sales",
            y="Product",
            orientation="h",
            title="Sales by Product",
            template="plotly_white"
        )

        st.plotly_chart(fig2, use_container_width=True)

    best_category = (
        df.groupby("Category")["Sales"].sum().idxmax()
    )

    best_region = (
        df.groupby("Region")["Profit"].sum().idxmax()
    )

    st.divider()

    st.subheader("💡 Key Business Insights")

    st.success(f"🏆 Top Sales Category: {best_category}")
    st.info(f"📍 Most Profitable Region: {best_region}")

# =========================================
# 8. DATASET AND DATA CLEANING PAGE
# =========================================

elif page == "📋 Dataset":

    st.title("📋 Retail Sales Dataset")

    st.write(
        "Explore the retail sales records used in this project."
    )

    # Dataset overview
    st.subheader("📊 Dataset Overview")

    c1, c2, c3 = st.columns(3)

    c1.metric("Original Records", len(raw_df))
    c2.metric("Clean Records", len(df))
    c3.metric("Total Columns", len(df.columns))

    st.divider()

    # Data quality report
    st.subheader("🧹 Data Cleaning & Quality Report")

    missing_values = quality_df.isnull().sum()
    duplicate_records = int(raw_df.duplicated().sum())
    removed_records = len(raw_df) - len(df)

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Missing Values",
        int(missing_values.sum())
    )

    c2.metric(
        "Duplicate Records",
        duplicate_records
    )

    c3.metric(
        "Removed Records",
        removed_records
    )

    # Column-wise quality information
    quality_report = pd.DataFrame({
        "Column": quality_df.columns,
        "Missing Values": missing_values.values,
        "Data Type": quality_df.dtypes.astype(str).values
    })

    st.markdown("### Column-wise Data Quality")

    st.dataframe(
        quality_report,
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    # Cleaned dataset
    st.subheader("✨ Cleaned Dataset Preview")

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

    # Download cleaned data
    st.download_button(
        label="⬇️ Download Cleaned Dataset",
        data=df.to_csv(index=False),
        file_name="cleaned_retail_sales.csv",
        mime="text/csv"
    )

# =========================================
# 9. ABOUT PROJECT PAGE
# =========================================

elif page == "ℹ️ About Project":

    st.title("ℹ️ About Retail Insights")

    st.markdown("""
    ### Project Overview

    Retail Insights is a Python-based Data Analytics project
    developed to understand retail sales performance.

    ### Technologies Used

    - Python
    - Pandas
    - Streamlit
    - Plotly
    - CSV Dataset

    ### Project Objectives

    1. Analyze total sales and profit.
    2. Understand product category performance.
    3. Study monthly sales trends.
    4. Compare regional profitability.
    5. Clean and prepare the dataset.
    6. Generate useful business insights.

    ### Dataset Information

    This project uses a simulated retail sales dataset
    created for learning and demonstration purposes.

    ### Key Learning Outcomes

    - Data handling using Pandas
    - Data cleaning
    - Data analysis
    - Data visualization
    - Interactive dashboard development
    - Business data interpretation

    ### Project Type

    Python Data Analytics Internship Project
    """)

# =========================================
# 10. FOOTER
# =========================================

st.divider()

st.markdown(
    """
    <div style="text-align:center; color:#A18EB2; padding:15px;">
        ✨ RETAIL INSIGHTS |
        Built with Python, Pandas, Plotly & Streamlit 💜
    </div>
    """,
    unsafe_allow_html=True
)
