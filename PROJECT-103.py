import pandas as pd
import plotly.express as px
df=pd.read_csv('./Covid.csv')
fig=px.scatter(df,x='date',y='cases',color='country',title='Cases-Per Day in different countries')
fig.show()