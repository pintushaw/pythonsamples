#Program for open high low intraday trading strategy

import pandas as pd
import numpy as np
import datetime
from IPython.display import display

# Get the current date in the format you want, e.g., DD-MMM-YYYY
current_date = datetime.datetime.now().strftime("%d-%b-%Y")

# Construct the filename with the current date
filename = f"MW-NIFTY-50-{current_date}.csv"

# Load CSV data into a DataFrame
df = pd.read_csv(filename)

def make_pretty(styler):
        styler.set_caption("Open High Low Strategy")
        styler.background_gradient(axis=None, vmin=1, vmax=5, cmap="YlGnBu")
        return styler   
def color_cells(val):
        color = 'red' if val < 0 else 'green'
        return f'background-color: {color}'
# Display the first few rows of the DataFrame
#print(df.head())
    
# Adjust pandas settings to display all rows
pd.set_option('display.max_rows', None)  # This will show all rows
# Adjust pandas settings to display all columns
#pd.set_option('display.max_columns', None)
selected_columns = ['SYMBOL', 'OPEN','HIGH','LOW','LTP','%CHNG','VOLUME (shares)']  # Replace with actual column names from your CSV
#Sort values by %cange
df.sort_values(by='%CHNG',ascending=False)
    
    
df['Buy_Sell']=np.where(df['OPEN'] == df['LOW'], 'Buy',np.where(df['OPEN'] == df['HIGH'], 'SELL','NA'))
    
selected_columns = ['SYMBOL', 'OPEN','HIGH','LOW','LTP','%CHNG','Buy_Sell']
projection=df[(df['Buy_Sell'] =='Buy') | (df['Buy_Sell'] == 'SELL')]
    
#print(df[selected_columns])
projection.style.pipe(make_pretty)
projection.style.background_gradient(cmap='viridis')
projection.style.map(color_cells)
display(projection[selected_columns])



#print(style_projection)