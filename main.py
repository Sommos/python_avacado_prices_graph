import pandas as pd
import matplotlib.pyplot as plt
import re
import mplcursors

# turns off the warning for chained assignment
pd.set_option('mode.chained_assignment', None)
# read the csv file, and set the variable name to df (dataframe)
df = pd.read_csv('datasets/avocado.csv')
# make a copy of the original dataframe where the type is equal to 'organic'
df = df[df['type'] == 'organic']
# sort the dataframe by the values of the column 'Date'
df.sort_values(by='Date', ascending=True, inplace=True)
# sort the dataframe by the column 'Date'
df['Date'] = pd.to_datetime(df['Date'])

# create a new dataframe
graph_df = pd.DataFrame()
# for each unique region in the dataframe up to the 16th region
for region in df['region'].unique():
    print(f'Processing Region: {region}')
    # create a new dataframe with the rows where the region is equal to the current region
    region_df = df[df['region'] == region]
    # set the index of the dataframe to the column 'Date', inplace=True means that the dataframe is updated
    region_df.set_index('Date', inplace=True)
    # sort the dataframe by the index
    region_df.sort_index(inplace=True)
    # create a new column in the dataframe with the name 'price25ma' and the value of the rolling mean
    region_df[f'{region}_price25ma'] = region_df['AveragePrice'].rolling(25).mean()

    # if the graph dataframe is empty
    if graph_df.empty:
        # set the graph dataframe to the region dataframe, 2 brackets sets it to a dataframe
        graph_df = region_df[[f'{region}_price25ma']]
    else:
        # join the region dataframe to the graph dataframe
        graph_df = graph_df.join(region_df[[f'{region}_price25ma']])

# create a list of the legend labels where the '_price25ma' suffix is removed from the region name
legend_labels = [region.replace('_price25ma', '') for region in graph_df.columns]
# set the maximum number of legend entries you want to display
max_legend_entries = 54
# create a list of legend labels limited to the specified number of entries, and split the labels on capital letters
limited_legend_labels = [re.sub(r'(?<=\w)([A-Z])', r' \1', label) for label in legend_labels[:max_legend_entries]]
# plot the graph dataframe, dropping any NaN values, and set the size of the graph
graph_complete = graph_df.dropna().plot(figsize=(20,12), legend=True)
# set the title of the graph
graph_complete.set_title('Avocado Average Region Prices', size=30, fontfamily='Arial')
# set the x-axis label of the graph to anchor outside of the graph, on the right side with 1 column and a font size of 7
graph_complete.legend(labels=limited_legend_labels, loc='center left', bbox_to_anchor=(1.0, 0.5), ncol=1, prop={'family': 'Arial', 'size': 7})

# create the mplcursors cursor object for the plot
cursors = mplcursors.cursor(graph_complete)
# set the hover annotation format
cursors.add_highlight('{label}') 

# show the graph
plt.show()