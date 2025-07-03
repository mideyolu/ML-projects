# dashboard.py
import streamlit as st
import pandas as pd
import plotly.express as px
from utils.helper import kpi_card

# load the data
df = pd.read_csv("../dataset/bank_churn.csv")

# encoding the attrition flag
df["Attrition"] = df["Attrition_Flag"].map(
    {"Existing Customer": 0, "Attrited Customer": 1}
)

# color map
COLOR_MAP = {
    "Existing Customer": "#6A3A00",
    "Attrited Customer": "#E5E5E5",
}


def dashboard():
    st.title("Bank Customer Attrition Dashboard")

    card_categories = df["Card_Category"].unique().tolist()
    all_checked = st.checkbox("Select All Card Categories", value=True)

    if all_checked:
        selected = card_categories  # all selected
    else:
        # show checkboxes for each category, collect selected ones
        selected = []
        for cat in card_categories:
            if st.checkbox(cat, value=False):
                selected.append(cat)

    # If none selected and not all, then show empty filtered data
    if not selected:
        st.warning("Please select at least one Card Category.")
        return

    # Filter dataframe
    filtered_df = df[df["Card_Category"].isin(selected)]

    # Recalculate KPI's on filtered data
    total_customers = filtered_df.shape[0]
    attrited_customers = filtered_df["Attrition"].sum()
    attrition_rate = (
        (attrited_customers / total_customers * 100) if total_customers > 0 else 0
    )
    avg_age = filtered_df["Customer_Age"].mean() if total_customers > 0 else 0
    avg_credit_limit = filtered_df["Credit_Limit"].mean() if total_customers > 0 else 0
    avg_trans_amt = filtered_df["Total_Trans_Amt"].mean() if total_customers > 0 else 0
    avg_relationship_count = (
        filtered_df["Total_Relationship_Count"].mean() if total_customers > 0 else 0
    )
    avg_utilization_ratio = (
        filtered_df["Avg_Utilization_Ratio"].mean() if total_customers > 0 else 0
    )
    avg_contacts = (
        filtered_df["Contacts_Count_12_mon"].mean() if total_customers > 0 else 0
    )

    # KPI cards
    col1, col2, col3 = st.columns(3)
    with col1:
        kpi_card("Total Customers", f"{total_customers:,}")
        kpi_card("Attrited Customers", f"{attrited_customers:,}")
        kpi_card("Attrition Rate (%)", f"{attrition_rate:.2f}%")
    with col2:
        kpi_card("Average Customer Age", f"{avg_age:.1f} years")
        kpi_card("Average Credit Limit", f"${avg_credit_limit:,.2f}")
        kpi_card("Average Monthly Transaction", f"${avg_trans_amt:,.2f}")
    with col3:
        kpi_card("Average Relationship Count", f"{avg_relationship_count:.2f}")
        kpi_card("Average Utilization Ratio", f"{avg_utilization_ratio:.2f}")
        kpi_card("Average Contacts Last Year", f"{avg_contacts:.2f}")

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        fig_age = px.histogram(
            filtered_df,
            x="Customer_Age",
            color="Attrition_Flag",
            nbins=15,
            barmode="overlay",
            title="Customer Age Distribution by Attrition Status",
            labels={
                "Customer_Age": "Customer Age (years)",
                "count": "Number of Customers",
                "Attrition_Flag": "Attrition Status",
            },
            color_discrete_map=COLOR_MAP,
        )
        st.plotly_chart(fig_age, use_container_width=True)

        fig_scatter = px.scatter(
            filtered_df,
            x="Credit_Limit",
            y="Customer_Age",
            color="Attrition_Flag",
            title="Credit Limit vs Customer Age Colored by Attrition",
            labels={
                "Credit_Limit": "Credit Limit ($)",
                "Customer_Age": "Customer Age (years)",
                "Attrition_Flag": "Attrition Status",
            },
            color_discrete_map=COLOR_MAP,
        )
        st.plotly_chart(fig_scatter, use_container_width=True)

        fig_box = px.box(
            filtered_df,
            x="Attrition_Flag",
            y="Credit_Limit",
            title="Credit Limit Distribution by Attrition Status",
            labels={
                "Attrition_Flag": "Attrition Status",
                "Credit_Limit": "Credit Limit ($)",
            },
            color="Attrition_Flag",
            color_discrete_map=COLOR_MAP,
        )
        st.plotly_chart(fig_box, use_container_width=True)

    with col2:
        fig_income = px.histogram(
            filtered_df,
            x="Income_Category",
            color="Attrition_Flag",
            barmode="group",
            title="Attrition by Income Category",
            labels={
                "Income_Category": "Income Category",
                "count": "Number of Customers",
                "Attrition_Flag": "Attrition Status",
            },
            color_discrete_map=COLOR_MAP,
        )
        st.plotly_chart(fig_income, use_container_width=True)

        fig_education = px.histogram(
            filtered_df,
            x="Education_Level",
            color="Attrition_Flag",
            barmode="group",
            title="Attrition by Educational Level",
            labels={
                "Education_Level": "Education Level",
                "count": "Number of Customers",
                "Attrition_Flag": "Attrition Status",
            },
            color_discrete_map=COLOR_MAP,
        )
        st.plotly_chart(fig_education, use_container_width=True)

        avg_trans = (
            filtered_df.groupby("Attrition_Flag")["Total_Trans_Ct"].mean().reset_index()
        )
        fig_bar = px.bar(
            avg_trans,
            x="Attrition_Flag",
            y="Total_Trans_Ct",
            title="Average Total Transactions by Attrition Status",
            labels={
                "Attrition_Flag": "Attrition Status",
                "Total_Trans_Ct": "Average Total Transactions",
            },
            color="Attrition_Flag",
            color_discrete_map=COLOR_MAP,
        )
        st.plotly_chart(fig_bar, use_container_width=True)

    fig_pie = px.pie(
        filtered_df,
        names="Attrition_Flag",
        title="Customer Attrition Proportion",
        hole=0.55,
        color="Attrition_Flag",
        color_discrete_map=COLOR_MAP,
    )
    st.plotly_chart(fig_pie, use_container_width=True)
