import pandas as pd
import numpy as np
import seaborn as sb
import openpyxl

feb =  pd.read_excel('https://github.com/CodeSolid/CodeSolid.github.io/raw/main/booksource/data/AnalyticsSnapshot.xlsx',sheet_name='February 2022',index_col=0)


address = ['NewYork', 'Chicago', 'Boston']

# Using 'Address' as the column name
# and equating it to the list
feb['Address'] = address