import pandas as pd
from pandas_profiling import ProfileReport
df = pd.read_csv('corona dataset.csv',index_col=0,parse_dates=True)
profile = ProfileReport(df)
profile.to_file('corona.html')