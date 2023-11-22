import time
import os
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np
import pandas as pd
from sklearn import datasets
st. set_page_config(
    page_title = 'Live income dashboard',
    page_icon = '📈',
    layout='wide'
)
st.title('Live income data monitoring app')
current_dir = os.path.dirname(os.path.realpath('train.csv'))
file_path = os.path.join(current_dir,'..','train.csv')
df = pd.read_csv(file_path)
df = df.drop('race',axis=1)

# filters
job_filter = st.selectbox('choose a job',df['occupation'].unique(),index=5)
placeholder = st.empty()

df = df[df['occupation']== job_filter]
for duration in range (300):
    df['new_age'] = df['age']  * np.random.choice(range(1,5))
    df['wphw_new'] = df['hours-per-week'] * np.random.choice(range(1,5))

    avg_age = np.mean(df['new_age'])
    count_married = int(df[df['marital-status']== 'married-in-spouse']['marital-status'].count()
                    +np.random.choice(range(1,5)))
    hpw = np.mean(df['wphw_new'])

    with placeholder.container():
        # creating 3 columns
        kpi1,kpi2,kpi3 = st.columns(3)
        # filling columns with required values
        kpi1.metric(label='Age',value = round(avg_age),delta = round(avg_age) - 10)
        kpi2.metric(label='Married Count', value=round(count_married), delta=10 + count_married)
        kpi3.metric(label='Working Hours/Week', value=round(hpw), delta=round(count_married/hpw) / 8)

        # creating 2 columns for charts
        figcol1,figcol2 = st.columns(2)
        with figcol1:
            st.markdown("## Age vs Martial-status")
            fig = px.density_heatmap(data_frame=df,color_continuous_scale='Plotly3',y='new_age',x='marital-status').update_layout(yaxis_title='Age')
            st.write(fig)
        with figcol1:
            st.markdown("## Age count")
            fig1 = px.histogram(data_frame=df,x='new_age').update_layout(xaxis_title='Age')
            st.write(fig1)

st.markdown('### data view as per selection')
st.dataframe(df)
time.sleep(1)




