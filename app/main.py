import streamlit as st
import pandas as pd
import plotly.express as px
from io import BytesIO

# --- Page Config ---
st.set_page_config(page_title="Agri Data Explorer",page_icon=":seedling:", layout="wide")

st.markdown("<h1 style='color:#00B4D8;'>🌿 Agri Data Explorer</h1>", unsafe_allow_html=True)
st.markdown("Analyze key crop production trends across Indian states and years.")

st.markdown("---")

# --- Load Data ---
@st.cache_data
def load_data():
    return pd.read_csv("data\\agri_data.csv")  

agri_df = load_data()
# Dropdown Options
chart_options = {
    "Top 7 Rice Producing States": "chart1",
    "Top 5 Wheat Producing States and Their Production Percentages (Bar Chart)": "chart2",
    "Top 5 States in Oilseed Production": "chart3",
    "Top 7 Sunflower Producing States": "chart4",
    "India's Sugarcane Production Over the Last 50 Years": "chart5",
    "Rice vs Wheat Production Over the Last 50 Years": "chart6",
    "Rice Production in West Bengal by District": "chart7",
    "Top 10 Years of Wheat Production in Uttar Pradesh": "chart8",
    "Millet Production Over the Last 50 Years": "chart9",
    "Sorghum Production (Kharif and Rabi) by Region": "chart10",
    "Top 7 States in Groundnut Production": "chart11",
    "Soybean Production and Yield Efficiency by Top 5 States": "chart12",
    "Oilseed Production Across Major States": "chart13",
    "Impact of Area Cultivated on Rice, Wheat, and Maize Production": "chart14",
    "Rice vs Wheat Yield Across States": "chart15"
}

#Dropdown 
st.markdown("### 🧭 Select the Chart to Display")
selected_chart = st.selectbox(
    "",
    list(chart_options.keys())
)


# --- Chart 1 Function ---
def chart_1():
    # Top 7 Rice Producing States
    q1_df = agri_df.groupby('State Name')['RICE PRODUCTION (1000 tons)'].sum().sort_values(ascending=False).head(7)

    fig1 = px.bar(
        q1_df,
        x=q1_df.index,
        y='RICE PRODUCTION (1000 tons)',
        title='Top 7 Rice Producing States',
        color=q1_df.index
    )
    fig1.update_layout(
        title_font=dict(color='#FF6F61', size=22),
        xaxis_title=dict(text="State Name", font=dict(color='#999999', size=17)),
        yaxis_title=dict(text="RICE PRODUCTION (1000 tons)", font=dict(color='#999999', size=17)),
        bargap=0.5,
        template="plotly_dark",
        paper_bgcolor="black",
        plot_bgcolor="black",
        shapes=[dict(
            type="rect", xref="paper", yref="paper",
            x0=0, y0=0, x1=1, y1=1,
            line=dict(color="#4d4d4d", width=1),
            layer="below"
        )],
        margin=dict(l=50, r=50, t=80, b=50)
    )
    fig1.update_layout(height=500)  # control height

    st.plotly_chart(fig1, use_container_width=True)

    # Show data table
    with st.expander("📄 View Raw Data"):
        st.dataframe(q1_df)

    # Download button
    st.download_button(
    label="📥 Download this data as CSV",
    data=q1_df.to_csv(index=False),
    file_name="Top_7_Rice_Producing_States.csv",
    mime="text/csv")


# --- Chart 2 Function ---
def chart_2():
    # Top 5 Wheat Producing States with Bar and Pie Chart
    q2_df = agri_df.groupby('State Name')['WHEAT PRODUCTION (1000 tons)'] \
                   .sum().sort_values(ascending=False).head(5)

    # Bar Chart
    fig2 = px.bar(
        q2_df,
        x=q2_df.index,
        y='WHEAT PRODUCTION (1000 tons)',
        title='Top 5 Wheat Producing States (Bar Chart)',
        color=q2_df.index
    )
    fig2.update_layout(
        title_font=dict(color='#FF6F61', size=22),
        xaxis_title=dict(text="State Name", font=dict(color='#999999', size=17)),
        yaxis_title=dict(text="WHEAT PRODUCTION (1000 tons)", font=dict(color='#999999', size=17)),
        bargap=0.6,
        template="plotly_dark",
        paper_bgcolor="black",
        plot_bgcolor="black",
        shapes=[dict(
            type="rect", xref="paper", yref="paper",
            x0=0, y0=0, x1=1, y1=1,
            line=dict(color="#4d4d4d", width=1),
            layer="below"
        )],
        margin=dict(l=50, r=50, t=80, b=50),
        height=500
    )

    st.plotly_chart(fig2, use_container_width=True)

    # Pie Chart Section Title
    st.markdown("### 📊 Wheat Production Share (Pie Chart)")

    # Prepare data for Pie Chart
    q2_df = q2_df.reset_index()

    # Pie Chart
    fig2_1 = px.pie(
        q2_df,
        values='WHEAT PRODUCTION (1000 tons)',
        names='State Name',
        title='Top 5 Wheat Producing States (Pie Chart)',
        hole=0.3
    )
    fig2_1.update_traces(
        textinfo='percent+label'  # Show percent + label on pie
    )
    fig2_1.update_layout(
        title_font=dict(color='#FF6F61', size=22),
        template="plotly_dark",
        paper_bgcolor="black",
        plot_bgcolor="black",
        legend_title_text='State Name',
        shapes=[dict(
            type="path", xref="paper", yref="paper",
            x0=1, y0=1, x1=1, y1=1,
            line=dict(color="#4d4d4d", width=1),
            layer="below"
        )],
        margin=dict(l=50, r=50, t=80, b=50),
        height=450
    )

    st.plotly_chart(fig2_1, use_container_width=True)

    # Show data table
    with st.expander("📄 View Raw Data"):
        st.dataframe(q2_df)

        # Download button
    st.download_button(
    label="📥 Download this data as CSV",
    data=q2_df.to_csv(index=False),
    file_name="Top 5 Wheat Producing States with Bar and Pie Chart.csv",
    mime="text/csv")



# --- Chart 3 Function ---
def chart_3():
    # Oilseed Production by Top 5 States
    q3_df = agri_df.groupby('State Name')['OILSEEDS PRODUCTION (1000 tons)'].sum().sort_values(ascending=False).head(5)

    fig3 = px.bar(
        q3_df,
        x=q3_df.index,
        y='OILSEEDS PRODUCTION (1000 tons)',
        title='Top 5 Oilseed Producing States',
        color=q3_df.index
    )
    fig3.update_layout(
        title_font=dict(color='#FF6F61', size=22),
        xaxis_title=dict(text="State Name", font=dict(color='#999999', size=17)),
        yaxis_title=dict(text="OILSEEDS PRODUCTION (1000 tons)", font=dict(color='#999999', size=17)),
        bargap=0.6,
        template="plotly_dark",
        paper_bgcolor="black",
        plot_bgcolor="black",
        shapes=[dict(
            type="rect", xref="paper", yref="paper",
            x0=0, y0=0, x1=1, y1=1,
            line=dict(color="#4d4d4d", width=1),
            layer="below"
        )],
        margin=dict(l=50, r=50, t=80, b=50)
    )
    fig3.update_layout(height=500)  # control height


    st.plotly_chart(fig3, use_container_width=True)

    # Show data table
    with st.expander("📄 View Raw Data"):
        st.dataframe(q3_df)

        # Download button
    st.download_button(
    label="📥 Download this data as CSV",
    data=q3_df.to_csv(index=False),
    file_name="Oilseed Production by Top 5 States.csv",
    mime="text/csv")


# --- Chart 4 Function ---
def chart_4():
    # Top 7 Sunflower Producing States
    q4_df = agri_df.groupby('State Name')['SUNFLOWER PRODUCTION (1000 tons)'].sum().sort_values(ascending=False).head(7)

    fig4 = px.bar(
        q4_df,
        x=q4_df.index,
        y='SUNFLOWER PRODUCTION (1000 tons)',
        title='Top 7 Sunflower Producing States',
        color=q4_df.index
    )
    fig4.update_layout(
        title_font=dict(color='#FF6F61', size=22),
        xaxis_title=dict(text="State Name", font=dict(color='#999999', size=17)),
        yaxis_title=dict(text="SUNFLOWER PRODUCTION (1000 tons)", font=dict(color='#999999', size=17)),
        bargap=0.5,
        template="plotly_dark",
        paper_bgcolor="black",
        plot_bgcolor="black",
        shapes=[dict(
            type="rect", xref="paper", yref="paper",
            x0=0, y0=0, x1=1, y1=1,
            line=dict(color="#4d4d4d", width=1),
            layer="below"
        )],
        margin=dict(l=50, r=50, t=80, b=50)
    )
    fig4.update_layout(height=500)  # control height


    st.plotly_chart(fig4, use_container_width=True)

    # Show data table
    with st.expander("📄 View Raw Data"):
        st.dataframe(q4_df)


        # Download button
    st.download_button(
    label="📥 Download this data as CSV",
    data=q4_df.to_csv(index=False),
    file_name="Top 7 Sunflower Producing States.csv",
    mime="text/csv")


def chart_5():
    # 5. India's Sugarcane Production from Last 50 Years (Line Plot)
    q5_df = agri_df.groupby('Year')['SUGARCANE PRODUCTION (1000 tons)'].sum().reset_index().tail(50)

    fig5 = px.line(
        q5_df,
        x='Year',
        y='SUGARCANE PRODUCTION (1000 tons)',
        title="India's Sugarcane Production (Last 50 Years)",
        labels={
            'Year': 'Year',
            'SUGARCANE PRODUCTION (1000 tons)': 'Production (1000 tons)'
        },
        markers=True,
        color_discrete_sequence=['#00B4D8']
    )

    fig5.update_layout(
        title_font=dict(color='#FF6F61', size=22),
        xaxis_title=dict(text='Year', font=dict(color='#999999', size=17)),
        yaxis_title=dict(text='Production (1000 tons)', font=dict(color='#999999', size=17)),
        hovermode="x unified",
        template="plotly_dark",
        paper_bgcolor="black",
        plot_bgcolor="black",
        shapes=[dict(
            type="rect", xref="paper", yref="paper",
            x0=0, y0=0, x1=1, y1=1,
            line=dict(color="#4d4d4d", width=1),
            layer="below"
        )],
        margin=dict(l=50, r=50, t=80, b=50)
    )

    max_year = q5_df.loc[q5_df['SUGARCANE PRODUCTION (1000 tons)'].idxmax(), 'Year']
    max_val = q5_df['SUGARCANE PRODUCTION (1000 tons)'].max()

    fig5.add_annotation(
        x=max_year,
        y=max_val,
        text="Peak Sugarcane",
        showarrow=True,
        arrowhead=2,
        font=dict(color='white'),
        bgcolor="#333",
        bordercolor="#666",
        borderwidth=1
    )
    fig5.update_layout(height=550)  # control height

    st.plotly_chart(fig5, use_container_width=True)

    # Show data table
    with st.expander("📄 View Raw Data"):
        st.dataframe(q5_df)


        # Download button
    st.download_button(
    label="📥 Download this data as CSV",
    data=q5_df.to_csv(index=False),
    file_name="sugarcane_production_last_50_years.csv",
    mime="text/csv"
)



def chart_6():
    # 6. Rice Production Vs Wheat Production (Last 50 Years)
    q6_df = agri_df.groupby('Year')[['RICE PRODUCTION (1000 tons)', 'WHEAT PRODUCTION (1000 tons)']].sum().tail(50).reset_index()

    fig6 = px.line(
        q6_df,
        x='Year',
        y=['RICE PRODUCTION (1000 tons)', 'WHEAT PRODUCTION (1000 tons)'],
        title="Rice vs Wheat Production (Last 50 Years)",
        markers=True
    )

    fig6.update_layout(
        title_font=dict(color='#FF6F61', size=22),
        xaxis_title=dict(text='Year', font=dict(color='#999999', size=17)),
        yaxis_title=dict(text='Production (1000 tons)', font=dict(color='#999999', size=17)),
        legend_title_text='Crop',
        hovermode="x unified",
        template="plotly_dark",
        paper_bgcolor="black",
        plot_bgcolor="black",
        shapes=[dict(
            type="rect", xref="paper", yref="paper",
            x0=0, y0=0, x1=1, y1=1,
            line=dict(color="#4d4d4d", width=1),
            layer="below"
        )],
        margin=dict(l=50, r=50, t=80, b=50)
    )

    max_year_rice = q6_df.loc[q6_df['RICE PRODUCTION (1000 tons)'].idxmax(), 'Year']
    max_val_rice = q6_df['RICE PRODUCTION (1000 tons)'].max()

    fig6.add_annotation(
        x=max_year_rice,
        y=max_val_rice,
        text="Peak Rice",
        showarrow=True,
        arrowhead=2,
        font=dict(color='white'),
        bgcolor="#333",
        bordercolor="#666",
        borderwidth=1
    )

    max_year_wheat = q6_df.loc[q6_df['WHEAT PRODUCTION (1000 tons)'].idxmax(), 'Year']
    max_val_wheat = q6_df['WHEAT PRODUCTION (1000 tons)'].max()

    fig6.add_annotation(
        x=max_year_wheat,
        y=max_val_wheat,
        text="Peak Wheat",
        showarrow=True,
        arrowhead=2,
        ax=80,
        ay=-20,
        font=dict(color='white'),
        bgcolor="#333",
        bordercolor="#666",
        borderwidth=1
    )
    fig6.update_layout(height=550)  # control height

    st.plotly_chart(fig6, use_container_width=True)

    # Show data table
    with st.expander("📄 View Raw Data"):
        st.dataframe(q6_df)

        # Download button
    st.download_button(
    label="📥 Download this data as CSV",
    data=q6_df.to_csv(index=False),
    file_name="Rice Production Vs Wheat Production (Last 50 Years).csv",
    mime="text/csv")


def chart_7():
    # 7. Rice Production by West Bengal Districts
    q7_df = agri_df[agri_df['State Name'] == 'West Bengal'].groupby('Dist Name')['RICE PRODUCTION (1000 tons)'].sum().sort_values(ascending=False)

    fig7 = px.bar(
        q7_df,
        x=q7_df.index,
        y='RICE PRODUCTION (1000 tons)',
        title='Rice Production by Districts (West Bengal)',
        color=q7_df.index
    )

    fig7.update_layout(
        title_font=dict(color='#FF6F61', size=22),
        xaxis_title=dict(text='District Name', font=dict(color='#999999', size=17)),
        yaxis_title=dict(text='RICE PRODUCTION (1000 tons)', font=dict(color='#999999', size=17)),
        bargap=0.5,
        template="plotly_dark",
        paper_bgcolor="black",
        plot_bgcolor="black",
        shapes=[dict(
            type="rect", xref="paper", yref="paper",
            x0=0, y0=0, x1=1, y1=1,
            line=dict(color="#4d4d4d", width=1),
            layer="below"
        )],
        margin=dict(l=50, r=50, t=80, b=50)
    )
    fig7.update_layout(height=500)  # control height


    st.plotly_chart(fig7, use_container_width=True)

    # Show data table
    with st.expander("📄 View Raw Data"):
        st.dataframe(q7_df)


        # Download button
    st.download_button(
    label="📥 Download this data as CSV",
    data=q7_df.to_csv(index=False),
    file_name="Rice Production by West Bengal Districts.csv",
    mime="text/csv")


def chart_8():
    # 8. Top 10 Wheat Production Years from Uttar Pradesh
    q8_df = agri_df[agri_df['State Name'] == 'Uttar Pradesh'].groupby('Year')['WHEAT PRODUCTION (1000 tons)'].sum().sort_values(ascending=False).head(10)

    fig8 = px.bar(
        q8_df,
        x=q8_df.index,
        y='WHEAT PRODUCTION (1000 tons)',
        title='Top 10 Wheat Production Years (Uttar Pradesh)',
        color=q8_df.index
    )

    fig8.update_layout(
        title_font=dict(color='#FF6F61', size=22),
        xaxis_title=dict(text='Year', font=dict(color='#999999', size=17)),
        yaxis_title=dict(text='WHEAT PRODUCTION (1000 tons)', font=dict(color='#999999', size=17)),
        bargap=0.5,
        template="plotly_dark",
        paper_bgcolor="black",
        plot_bgcolor="black",
        shapes=[dict(
            type="rect", xref="paper", yref="paper",
            x0=0, y0=0, x1=1, y1=1,
            line=dict(color="#4d4d4d", width=1),
            layer="below"
        )],
        margin=dict(l=50, r=50, t=80, b=50)
    )
    fig8.update_layout(height=500)  # control height


    st.plotly_chart(fig8, use_container_width=True)

    # Show data table
    with st.expander("📄 View Raw Data"):
        st.dataframe(q8_df)


        # Download button
    st.download_button(
    label="📥 Download this data as CSV",
    data=q8_df.to_csv(index=False),
    file_name="Top 10 Wheat Production Years from Uttar Pradesh.csv",
    mime="text/csv")


def chart_9():
    # Millet Production (Last 50 Years)
    q9_df = agri_df.groupby('Year')[['PEARL MILLET PRODUCTION (1000 tons)', 'FINGER MILLET PRODUCTION (1000 tons)']].sum().tail(50)

    fig9 = px.line(
        q9_df,
        x=q9_df.index,
        y=['PEARL MILLET PRODUCTION (1000 tons)', 'FINGER MILLET PRODUCTION (1000 tons)'],
        title="Millet Production (Last 50 Years)",
        markers=True
    )

    fig9.update_layout(
        title_font=dict(color='#FF6F61', size=22),
        xaxis_title=dict(text='Year', font=dict(color='#999999', size=17)),
        yaxis_title=dict(text='Production (1000 tons)', font=dict(color='#999999', size=17)),
        legend_title_text='Crop',
        hovermode="x unified",
        template="plotly_dark",
        paper_bgcolor="black",
        plot_bgcolor="black",
        shapes=[dict(
            type="rect", xref="paper", yref="paper",
            x0=0, y0=0, x1=1, y1=1,
            line=dict(color="#4d4d4d", width=1), layer="below"
        )],
        margin=dict(l=50, r=50, t=80, b=50)
    )

    # Annotate peak Pearl Millet
    max_year = q9_df['PEARL MILLET PRODUCTION (1000 tons)'].idxmax()
    max_val = q9_df['PEARL MILLET PRODUCTION (1000 tons)'].max()
    fig9.add_annotation(
        x=max_year, y=max_val,
        text="Peak Pearl Millet", showarrow=True, arrowhead=2,
        font=dict(color='white'), bgcolor="#333",
        bordercolor="#666", borderwidth=1,
    )

    # Annotate peak Finger Millet
    max_year = q9_df['FINGER MILLET PRODUCTION (1000 tons)'].idxmax()
    max_val = q9_df['FINGER MILLET PRODUCTION (1000 tons)'].max()
    fig9.add_annotation(
        x=max_year, y=max_val,
        text="Peak Finger Millet", showarrow=True, arrowhead=2,
        font=dict(color='white'), bgcolor="#333",
        bordercolor="#666", borderwidth=1,
    )

    fig9.update_layout(height=550)  # control height

    st.plotly_chart(fig9, use_container_width=True)

    # Show data table
    with st.expander("📄 View Raw Data"):
        st.dataframe(q9_df)


        # Download button
    st.download_button(
    label="📥 Download this data as CSV",
    data=q9_df.to_csv(index=False),
    file_name="Millet Production (Last 50 Years).csv",
    mime="text/csv")


def chart_10():

    # 10.Sorghum Production (Kharif and Rabi) by Region

    q10_df = agri_df.groupby(['State Name'])[['KHARIF SORGHUM PRODUCTION (1000 tons)','RABI SORGHUM PRODUCTION (1000 tons)']].sum()

    # Add TOTAL_SORGHUM PRODUCTION (1000 tons)
    q10_df["TOTAL_SORGHUM PRODUCTION (1000 tons)"] = (
    q10_df["KHARIF SORGHUM PRODUCTION (1000 tons)"] + q10_df["RABI SORGHUM PRODUCTION (1000 tons)"] )
    #Sorting TOTAL_SORGHUM PRODUCTION (1000 tons)
    q10_df = q10_df.sort_values(by="TOTAL_SORGHUM PRODUCTION (1000 tons)", ascending=False)


    fig10 = px.bar(q10_df,
             x=q10_df.index,
             y='TOTAL_SORGHUM PRODUCTION (1000 tons)',
             title='Sorghum Production (1000 tons) by State',
             color=q10_df.index)
    fig10.update_layout(
    title_font=dict(color='#FF6F61', size=22),  # Title
    xaxis_title=dict(text='State Name', font=dict(color='#999999',size=17)),
    yaxis_title=dict(text='TOTAL_SORGHUM PRODUCTION (1000 tons)', font=dict(color='#999999',size=17)),
    template="plotly_dark",
        # Add outer paper background color
    paper_bgcolor="black",
    plot_bgcolor="black",
    

    # Add chart border using shapes
    shapes=[dict(
        type="rect",
        xref="paper", yref="paper",
        x0=0, y0=0, x1=1, y1=1,
        line=dict(color="#4d4d4d", width=1),
        layer="below"
    )],

    margin=dict(l=50, r=50, t=80, b=50)
    )

    st.plotly_chart(fig10, use_container_width=True)

    # Show data table
    with st.expander("📄 View Raw Data"):
        st.dataframe(q10_df)


        # Download button
    st.download_button(
    label="📥 Download this data as CSV",
    data=q10_df.to_csv(index=False),
    file_name="Sorghum Production (Kharif and Rabi) by Region.csv",
    mime="text/csv")


def chart_11():
    # Top 7 States for Groundnut Production
    q11_df = agri_df.groupby('State Name')['GROUNDNUT PRODUCTION (1000 tons)'].sum().sort_values(ascending=False).head(7)

    fig11 = px.bar(
        q11_df,
        x=q11_df.index,
        y='GROUNDNUT PRODUCTION (1000 tons)',
        title='Top 7 States for Groundnut Production',
        color=q11_df.index
    )

    fig11.update_layout(
        title_font=dict(color='#FF6F61', size=22),
        xaxis_title=dict(text='State Name', font=dict(color='#999999', size=17)),
        yaxis_title=dict(text='GROUNDNUT PRODUCTION (1000 tons)', font=dict(color='#999999', size=17)),
        bargap=0.7,
        template="plotly_dark",
        paper_bgcolor="black",
        plot_bgcolor="black",
        shapes=[dict(
            type="rect", xref="paper", yref="paper",
            x0=0, y0=0, x1=1, y1=1,
            line=dict(color="#4d4d4d", width=1), layer="below"
        )],
        margin=dict(l=50, r=50, t=80, b=50)
    )
    fig11.update_layout(height=550)  # control height

    st.plotly_chart(fig11, use_container_width=True)

    # Show data table
    with st.expander("📄 View Raw Data"):
        st.dataframe(q11_df)


        # Download button
    st.download_button(
    label="📥 Download this data as CSV",
    data=q11_df.to_csv(index=False),
    file_name="Top 7 States for Groundnut Production.csv",
    mime="text/csv")


def chart_12():
    # Soybean Production by Top 5 States and Yield Efficiency
    q12_df = agri_df.groupby('State Name')[
        ['SOYABEAN PRODUCTION (1000 tons)', 'SOYABEAN YIELD (Kg per ha)']
    ].sum().sort_values(by='SOYABEAN YIELD (Kg per ha)', ascending=False).head(5)

    fig12 = px.bar(
        q12_df,
        x=q12_df.index,
        y=['SOYABEAN PRODUCTION (1000 tons)', 'SOYABEAN YIELD (Kg per ha)'],
        title='Soybean Production by Top 5 States and Yield Efficiency',
        barmode='group',
        color_discrete_sequence=['#00B4D8', '#F9A825'],
        labels={"variable": "Soyabean Production & Yield"}
    )

    fig12.update_layout(
        title_font=dict(color='#FF6F61', size=22),
        xaxis_title=dict(text='State Name', font=dict(color='#999999', size=17)),
        yaxis_title=dict(text='Production & Yield', font=dict(color='#999999', size=17)),
        bargap=0.6,
        template="plotly_dark",
        paper_bgcolor="black",
        plot_bgcolor="black",
        shapes=[dict(
            type="rect", xref="paper", yref="paper",
            x0=0, y0=0, x1=1, y1=1,
            line=dict(color="#4d4d4d", width=1), layer="below"
        )],
        margin=dict(l=50, r=50, t=80, b=50),
        yaxis=dict(tickmode='linear', dtick=200000),
        height=500
    )

    st.plotly_chart(fig12, use_container_width=True)

    # Show data table
    with st.expander("📄 View Raw Data"):
        st.dataframe(q12_df)

        # Download button
    st.download_button(
    label="📥 Download this data as CSV",
    data=q12_df.to_csv(index=False),
    file_name="Soybean Production by Top 5 States and Yield Efficiency.csv",
    mime="text/csv")



def chart_13():
    # Oilseed Production in Major States
    q13_df = agri_df.groupby('State Name')['OILSEEDS PRODUCTION (1000 tons)'].sum().sort_values(ascending=False).head(5)

    fig13 = px.bar(
        q13_df,
        x=q13_df.index,
        y='OILSEEDS PRODUCTION (1000 tons)',
        title='Oilseed Production in Major States',
        color=q13_df.index
    )

    fig13.update_layout(
        width=1000,
        height=600,
        title_font=dict(color='#FF6F61', size=22),
        xaxis_title=dict(text='State Name', font=dict(color='#999999', size=17)),
        yaxis_title=dict(text='OILSEEDS PRODUCTION (1000 tons)', font=dict(color='#999999', size=17)),
        bargap=0.8,
        template="plotly_dark",
        barmode='group',
        paper_bgcolor="black",
        plot_bgcolor="black",
        shapes=[dict(
            type="rect", xref="paper", yref="paper",
            x0=0, y0=0, x1=1, y1=1,
            line=dict(color="#4d4d4d", width=1), layer="below"
        )],
        margin=dict(l=50, r=50, t=80, b=50)
    )
    fig13.update_layout(height=550)  # control height

    st.plotly_chart(fig13, use_container_width=True)

    # Show data table
    with st.expander("📄 View Raw Data"):
        st.dataframe(q13_df)

        
        # Download button
    st.download_button(
    label="📥 Download this data as CSV",
    data=q13_df.to_csv(index=False),
    file_name="Oilseed Production in Major States.csv",
    mime="text/csv")


def chart_14():
    # Chart 14: Impact of Area Cultivated on Production (Rice, Wheat, Maize)
    # Create individual dataframes with a "Crop" column
    rice_df = agri_df[['RICE AREA (1000 ha)', 'RICE YIELD (Kg per ha)']].copy()
    rice_df.columns = ['Area', 'Yield']
    rice_df['Crop'] = 'Rice'
    
    wheat_df = agri_df[['WHEAT AREA (1000 ha)', 'WHEAT YIELD (Kg per ha)']].copy()
    wheat_df.columns = ['Area', 'Yield']
    wheat_df['Crop'] = 'Wheat'
    
    maize_df = agri_df[['MAIZE AREA (1000 ha)', 'MAIZE YIELD (Kg per ha)']].copy()
    maize_df.columns = ['Area', 'Yield']
    maize_df['Crop'] = 'Maize'
    
    #Combine them
    
    combined_df = pd.concat([rice_df, wheat_df, maize_df], ignore_index=True)
    
    #Create scatter plot
     
    fig14 = px.scatter(combined_df,
                 x='Area',
                 y='Yield',
                 color='Crop',
                 title='Impact of Area Cultivated on Yield for Major Crops',
                 labels={'Area': 'Area Cultivated (1000 ha)',
                         'Yield': 'Yield (Kg per ha)'},
                 color_discrete_map={
                     'Rice': '#00B4D8',
                     'Wheat': '#FFB703',
                     'Maize': '#90E0EF'
                 })
    
    #Styling
    
    
    fig14.update_layout(
    title_font=dict(color='#FF6F61', size=22),
    xaxis_title=dict(text='Area Cultivated (1000 ha)', font=dict(color='#999999', size=17)),
    yaxis_title=dict(text='Yield (Kg per ha)', font=dict(color='#999999', size=17)),
    template="plotly_dark",
    legend_title_text='Crop',
    paper_bgcolor="black",
    plot_bgcolor="black",
    shapes=[dict(
        type="rect", xref="paper", yref="paper",
        x0=0, y0=0, x1=1, y1=1,
        line=dict(color="#4d4d4d", width=1), layer="below"
    )],
    margin=dict(l=50, r=50, t=80, b=50)
)
    
    fig14.update_layout(height=550)  # control height
    
    st.plotly_chart(fig14, use_container_width=True)

    # Show data table
    with st.expander("📄 View Raw Data"):
        st.dataframe(combined_df)

        # Download button
    st.download_button(
    label="📥 Download this data as CSV",
    data=combined_df.to_csv(index=False),
    file_name="Area vs Production (Rice, Wheat, Maize).csv",
    mime="text/csv")


def chart_15():
    # Chart 15: Rice vs. Wheat Yield Across States

    q15_df = agri_df.groupby('State Name')[
        ['RICE YIELD (Kg per ha)', 'WHEAT YIELD (Kg per ha)']
    ].sum()

    q15_df['Total_Yield'] = q15_df['RICE YIELD (Kg per ha)'] + q15_df['WHEAT YIELD (Kg per ha)']
    q15_df = q15_df.sort_values(by='Total_Yield', ascending=False)

    q15_df_melted = q15_df.drop(columns='Total_Yield').reset_index().melt(
        id_vars='State Name', var_name='Crop', value_name='Yield')

    fig15 = px.bar(
        q15_df_melted,
        x='State Name',
        y='Yield',
        color='Crop',
        barmode='group',
        title='Rice vs. Wheat Yield Across States',
        color_discrete_map={
            'RICE YIELD (Kg per ha)': '#00B4D8',
            'WHEAT YIELD (Kg per ha)': '#F9A825'
        }
    )

    fig15.update_layout(
        title_font=dict(color='#FF6F61', size=22),
        xaxis_title=dict(text='State Name', font=dict(color='#999999', size=17)),
        yaxis_title=dict(text='Yield (Kg per ha)', font=dict(color='#999999', size=17)),
        template="plotly_dark",
        bargap=0.4,
        paper_bgcolor="black",
        plot_bgcolor="black",
        shapes=[dict(
            type="rect", xref="paper", yref="paper",
            x0=0, y0=0, x1=1, y1=1,
            line=dict(color="#4d4d4d", width=1),
            layer="below"
        )],
        margin=dict(l=50, r=50, t=80, b=50),
        yaxis=dict(tickmode='linear', dtick=1000000)
    )
    fig15.update_layout(height=500)  # control height

    st.plotly_chart(fig15, use_container_width=True)

    # Show data table
    with st.expander("📄 View Raw Data"):
        st.dataframe(q15_df)

        # Download button
    st.download_button(
    label="📥 Download this data as CSV",
    data=q15_df.to_csv(index=False),
    file_name="Rice vs. Wheat Yield Across States.csv",
    mime="text/csv")




# --- Chart Dispatcher ---
if chart_options[selected_chart] == "chart1":
        # 💎 Rice Metrics Section
    st.markdown("### 🌾 Rice Production – Key Metrics")

# Calculate differences
    top_values = [544232.26, 445597.62, 335040.10, 315185.40, 291201.51, 282532.93, 231759]
    diffs = [round(top_values[0] - v, 2) for v in top_values[1:]]

# Show metrics with changes
    col1, col2, col3 = st.columns(3)
    col1.metric("🥇 West Bengal", "544.2K Tons", "—")
    col2.metric("🥈 Uttar Pradesh", "445.6K Tons", f"↓ {diffs[0]/1000:.1f}K Tons")
    col3.metric("🥉 Punjab", "335.0K Tons", f"↓ {diffs[1]/1000:.1f}K Tons")

    chart_1()

elif chart_options[selected_chart] == "chart2":

    # --- Wheat Metrics ---
    st.markdown("### 🌽 Wheat Production – Key Metrics")

    top_values = [970210.07, 593848.9, 348429.6, 338644.25, 265994.99]
    diffs = [round(top_values[0] - v, 2) for v in top_values[1:]]

    col1, col2, col3 = st.columns(3)
    col1.metric("🥇 Uttar Pradesh", "970.2K Tons", "—")
    col2.metric("🥈 Punjab", "593.8K Tons", f"↓ {diffs[0]/1000:.1f}K Tons")
    col3.metric("🥉 Haryana", "348.4K Tons", f"↓ {diffs[1]/1000:.1f}K Tons")


    chart_2()

elif chart_options[selected_chart] == "chart3":

    # --- Oilseeds Metrics ---
    st.markdown("### 🛢️ Oilseed Production – Key Metrics")

    top_values = [153594.79, 126224.01, 122726.86, 95567.91, 76888.09]
    diffs = [round(top_values[0] - v, 2) for v in top_values[1:]]

    col1, col2, col3 = st.columns(3)
    col1.metric("🥇 Madhya Pradesh", "153.6K Tons", "—")
    col2.metric("🥈 Gujarat", "126.2K Tons", f"↓ {diffs[0]/1000:.1f}K Tons")
    col3.metric("🥉 Rajasthan", "122.7K Tons", f"↓ {diffs[1]/1000:.1f}K Tons")

    chart_3()

elif chart_options[selected_chart] == "chart4":

    # 🌻 Sunflower Metrics Section
    st.markdown("### 🌻 Sunflower Production – Key Metrics")

    # Values (in 1000 tons)
    sunflower_values = [10785.87, 5599.46, 4447.78, 1401.06, 1081.86, 762.38, 552.66]
    sunflower_diffs = [round(sunflower_values[0] - v, 2) for v in sunflower_values[1:]]

    col1, col2, col3 = st.columns(3)
    col1.metric("🥇 Karnataka", "10.8K Tons", "—")
    col2.metric("🥈 Maharashtra", "5.6K Tons", f"↓ {sunflower_diffs[0]:.1f}K Tons")
    col3.metric("🥉 Andhra Pradesh", "4.4K Tons", f"↓ {sunflower_diffs[1]:.1f}K Tons")

    chart_4()

elif chart_options[selected_chart] == "chart5":

    # Sugarcane Production – Peak Year Highlight
    st.markdown("### 🍬 Sugarcane Production – Key Metrics")

    peak_year = 2011
    peak_value = 38988.84
    prev_value = 35213.44  # 2012 value (next year drop)

    diff = round(prev_value - peak_value, 2)  # drop after peak
    status = "↓"

    # Metric Display
    st.metric(f"📅 {peak_year}", f"{peak_value:,.2f} Tons", f"{status} {abs(diff):,.2f} Tons in 2012")

    chart_5()

elif chart_options[selected_chart] == "chart6":

    # Key Metrics – Rice & Wheat Production
    st.markdown("### ⚖️ Rice vs Wheat – Production Metrics")

    # Latest and Peak values
    rice_peak_year = 2016
    rice_peak_value = 117614.1
    rice_2017_value = 114319.61

    wheat_peak_year = 2016
    wheat_peak_value = 112962.82
    wheat_2017_value = 110418.21

    # Differences from 2016 to 2017
    rice_diff = round(rice_2017_value - rice_peak_value, 2)
    wheat_diff = round(wheat_2017_value - wheat_peak_value, 2)

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
        label=f"🍚 Rice Peak Year - {rice_peak_year}",
        value=f"{rice_peak_value:,.2f} Tons",
        delta=f"{'↓' if rice_diff < 0 else '↑'} {abs(rice_diff):,.2f} Tons in 2017"
    )

    with col2:
        st.metric(
        label=f"🌾 Wheat Peak Year - {wheat_peak_year}",
        value=f"{wheat_peak_value:,.2f} Tons",
        delta=f"{'↓' if wheat_diff < 0 else '↑'} {abs(wheat_diff):,.2f} Tons in 2017"
    )


    chart_6()
    
elif chart_options[selected_chart] == "chart7":

    # West Bengal – Rice Production by District (Top 5)
    st.markdown("### 📍 West Bengal Rice Production – District Metrics")

    district_names = ["Midnapur", "Burdwan", "24 Parganas", "Birbhum", "Bankura"]
    top_districts = [98868.28, 71422.15, 63011.99, 42213.81, 40165.20]
    diffs = [round(top_districts[0] - val, 2) for val in top_districts[1:]]

    col1, col2, col3 = st.columns(3)
    col1.metric(f"🥇 {district_names[0]}", f"{top_districts[0]/1000:.1f}K Tons", "—")
    col2.metric(f"🥈 {district_names[1]}", f"{top_districts[1]/1000:.1f}K Tons", f"↓ {diffs[0]/1000:.1f}K")
    col3.metric(f"🥉 {district_names[2]}", f"{top_districts[2]/1000:.1f}K Tons", f"↓ {diffs[1]/1000:.1f}K")

    col4, col5, _ = st.columns(3)
    col4.metric(f"4️⃣ {district_names[3]}", f"{top_districts[3]/1000:.1f}K Tons", f"↓ {diffs[2]/1000:.1f}K")
    col5.metric(f"5️⃣ {district_names[4]}", f"{top_districts[4]/1000:.1f}K Tons", f"↓ {diffs[3]/1000:.1f}K")

    chart_7()

elif chart_options[selected_chart] == "chart8":

    # Uttar Pradesh – Wheat Production Key Metrics
    st.markdown("### 🌽 Uttar Pradesh Wheat Production – Yearly Metrics")

    top_wheat = [35798.6, 35120.9, 32271.69, 31611.63, 30602.91]
    years = ["2017", "2016", "2013", "2011", "2010"]
    diffs = [round(top_wheat[0] - val, 2) for val in top_wheat[1:]]

    col1, col2, col3 = st.columns(3)
    col1.metric(f"🥇 {years[0]}", f"{top_wheat[0]/1000:.1f}K Tons", "—")
    col2.metric(f"🥈 {years[1]}", f"{top_wheat[1]/1000:.1f}K Tons", f"↓ {diffs[0]/1000:.1f}K")
    col3.metric(f"🥉 {years[2]}", f"{top_wheat[2]/1000:.1f}K Tons", f"↓ {diffs[1]/1000:.1f}K")

    chart_8()

elif chart_options[selected_chart] == "chart9":

    # Millet Production – Key Metrics for Last 50 Years
    st.markdown("### 🌾 Millet Production – Key Metrics")

    # Manually entered from your values
    pearl_millet_peak = 12413.46
    finger_millet_peak = 3123.91
    year_pearl_peak = "2011"
    year_finger_peak = "1978"

    # Comparing against next highest
    pearl_millet_second = 12376.91
    finger_millet_second = 3000.37

    pearl_diff = round(pearl_millet_peak - pearl_millet_second, 2)
    finger_diff = round(finger_millet_peak - finger_millet_second, 2)

    col1, col2 = st.columns(2)

    col1.metric(
    label=f"🌟 Peak Pearl Millet – {year_pearl_peak}",
    value=f"{pearl_millet_peak / 1000:.2f}K Tons",
    delta=f"↑ {pearl_diff / 1000:.2f}K"
    )

    col2.metric(
    label=f"🌟 Peak Finger Millet – {year_finger_peak}",
    value=f"{finger_millet_peak / 1000:.2f}K Tons",
    delta=f"↑ {finger_diff / 1000:.2f}K"
    )

    chart_9()

elif chart_options[selected_chart] == "chart10":
    
    ## 
    data = {
    'State': ['Maharashtra', 'Karnataka', 'Madhya Pradesh', 'Telangana', 'Tamil Nadu'],
    'Kharif': [116655.48, 35279.76, 56642.83, 13221.64, 16020.74],
    'Rabi': [85454.84, 42753.83, 116.69, 12564.79, 7620.00],
    }

    df = pd.DataFrame(data)
    df['Total'] = df['Kharif'] + df['Rabi']
    df = df.sort_values(by='Total', ascending=False).reset_index(drop=True)

    # Calculate difference from top producer
    diffs = [round(df.loc[0, 'Total'] - val, 2) for val in df['Total'][1:]]

    # Show key metrics
    st.markdown("### 🧺 Sorghum Production – Regional Metrics")

    col1, col2, col3 = st.columns(3)
    col1.metric(f"🥇 {df.loc[0, 'State']}", f"{df.loc[0, 'Total']/1000:.2f}K Tons", "—")
    col2.metric(f"🥈 {df.loc[1, 'State']}", f"{df.loc[1, 'Total']/1000:.2f}K", f"↓ {diffs[0]/1000:.2f}K")
    col3.metric(f"🥉 {df.loc[2, 'State']}", f"{df.loc[2, 'Total']/1000:.2f}K", f"↓ {diffs[1]/1000:.2f}K")

    chart_10()

elif chart_options[selected_chart] == "chart11":

    st.markdown("### 🥜 Groundnut Production – Key Metrics")


    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(label="🥇 Gujarat", 
              value="98,321 tons", 
              delta="↑")

    with col2:
        st.metric(label="🥈 Andhra Pradesh", 
              value="57,844 tons", 
              delta="-424 tons")

    with col3:
        st.metric(label="🥉 Tamil Nadu", 
              value="57,662 tons", 
              delta="-182 tons")


    chart_11()

elif chart_options[selected_chart] == "chart12":

    st.markdown("### 🫘 Soybean Production & Yield Metrics")


    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(label="🌾 Madhya Pradesh", 
              value="136K tons", 
              delta="↑ 1.16M kg/ha Yield")

    with col2:
        st.metric(label="🌿 Maharashtra", 
              value="58.6K tons", 
              delta="↑ 770K kg/ha")

    with col3:
        st.metric(label="🌱 Rajasthan", 
              value="21.2K tons", 
              delta="↑ 405K kg/ha")


    chart_12()

elif chart_options[selected_chart] == "chart13":

    st.markdown("### 🛢️ Oilseed Major States – Key Metrics")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(label="🏆 Madhya Pradesh", 
              value="153.6K tons", 
              delta="↑ Highest Producer")

    with col2:
        st.metric(label="🥈 Gujarat", 
              value="126.2K tons", 
              delta="↓ -27.4K vs MP")

    with col3:
        st.metric(label="🥉 Rajasthan", 
              value="122.7K tons", 
              delta="↓ -3.5K vs Gujarat")

    chart_13()

elif chart_options[selected_chart] == "chart14":

    st.markdown("### 📐 Area vs Production (Rice, Wheat, Maize) – Key Metrics")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(label="🌾 Rice", 
              value="r = 0.98", 
              delta="Strong Positive")

    with col2:
        st.metric(label="🌿 Wheat", 
              value="r = 0.94", 
              delta="Strong Positive")

    with col3:
        st.metric(label="🌽 Maize", 
              value="r = 0.81", 
              delta="Moderate Positive")


    chart_14()
    
elif chart_options[selected_chart] == "chart15":

    st.markdown("### 🌾 Rice Yield – Top States Metrics")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(label="🥇 Uttar Pradesh", 
              value="3.77M kg/ha", 
              delta="↑ Highest Rice Yield")

    with col2:
        st.metric(label="🥈 Karnataka", 
              value="2.13M kg/ha", 
              delta="↓ -1.64M vs UP")

    with col3:
        st.metric(label="🥉 Tamil Nadu", 
              value="1.76M kg/ha", 
              delta="↓ -373K vs Karnataka")
        
    st.subheader("🌾 Top States by Wheat Yield")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(label="🥇 Uttar Pradesh", 
              value="5.21M kg/ha", 
              delta="↑ Highest Wheat Yield")

    with col2:
        st.metric(label="🥈 Madhya Pradesh", 
              value="2.93M kg/ha", 
              delta="↓ -2.28M vs UP")

    with col3:
        st.metric(label="🥉 Rajasthan", 
              value="2.72M kg/ha", 
              delta="↓ -210K vs MP")



    chart_15()


    # Footer
st.markdown("""
    <hr>
    <div style="text-align: center;">
        <p style="font-size: 13px;">🚨 SecureCheck | Built by <strong>Infant Joshva</strong></p>
        <a href="https://github.com/Infant-Joshva" target="_blank" style="text-decoration: none; margin: 0 10px;">🐙 GitHub</a>
        <a href="https://www.linkedin.com/in/infant-joshva" target="_blank" style="text-decoration: none; margin: 0 10px;">🔗 LinkedIn</a>
        <a href="mailto:infantjoshva46@gmail.com" style="text-decoration: none; margin: 0 10px;">📩 Contact</a>
    </div>
""", unsafe_allow_html=True)