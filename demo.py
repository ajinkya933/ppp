import streamlit as st
import pandas as pd
import numpy as np

st.title('India to US salary converter')
st.write ('According to the Worldbank Purchase Power Parity ')

chart_data = pd.DataFrame(
     [5.49599228,	6.047286381,	6.442613436,	6.914082743,	7.445126304,	7.953087579,	8.401702937,	8.794170579,	9.392878418,	9.546555886,	9.675325879,	9.766414541,	9.973857916,	10.15912616,	10.45998932,	10.71212636,	11.26447089,	11.72972395,	12.56712223,	13.36622212,	14.59772061,	15.5495491,	16.16083527,	17.34232521,	18.386549,	19.23500252,	19.89872742,	20.64779282,	20.94932114,	21.0732267,	21.98850799,	23.13813763],
     columns=['Purchase Power Parity'])

print(chart_data)
st.area_chart(chart_data)

number = st.number_input('Enter the yearly salary in India')
usd= number / 23.13813763
st.write('Equivalent yearly US salary is ', usd)
