import pandas as pd
import matplotlib.pyplot as plt

# read the csv file, and set the variable name to df (dataframe)
df = pd.read_csv('datasets/avocado.csv')
# make a copy of the original dataframe where the type is equal to 'organic'
df = df.copy()[df['type'] == 'organic']
# sort the dataframe by the column 'Date'
df['Date'] = pd.to_datetime(df['Date'])
# sort the dataframe by the values of the column 'Date'
df.sort_values(by='Date', ascending=True, inplace=True)

# create a new dataframe
graph_df = pd.DataFrame()
# for each unique region in the dataframe up to the 16th region
for region in df['region'].unique():
    print(region)
    # create a new dataframe with the rows where the region is equal to the current region
    region_df = df.copy()[df['region'] == region]
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

graph_df.tail()
# plot the graph dataframe, dropping any NaN values, and set the size of the graph
graph_complete = graph_df.dropna().plot(figsize=(20,12), legend=True)
# set the title of the graph
graph_complete.set_title('Avocado Average Region Prices', size=30)
# set the x-axis label of the graph to anchor outside of the graph
graph_complete.legend(bbox_to_anchor=(1.0, 1.0))
# show the graph
plt.show()

# # print the first 3 rows of the dataframe to the console
# print(df.head(3))
# # print the last 2 rows of the dataframe to the console
# print(df.tail(2))
# # print the column 'AveragePrice' of the dataframe to the console
# print(df['AveragePrice'])

# # instantiates a new dataframe with only the rows where the region is 'Albany'
# albany_df = df[df['region'] == 'Albany']
# # plot the dataframe
# # albany_df['AveragePrice'].plot()
# # # show the plot
# # plt.show()

# # make a copy of the original dataframe where the region is equal to 'Albany'
# albany_df = df.copy()[df['region'] == 'Albany']
# # set the index of the dataframe to the column 'Date', inplace=True means that the dataframe is updated
# albany_df.set_index('Date', inplace=True)
# # sort the dataframe by the index
# albany_df.sort_index(inplace=True)
# # create a new column in the dataframe with the name 'price25ma' and the value of the rolling mean
# albany_df['price25ma'] = albany_df['AveragePrice'].rolling(25).mean()
# # print each region of the dataframe to the console
# print(list(set(df['region'].values.tolist())))
# # gets the unique values of the column 'region' and stores it in a list
# df['region'].unique()

# # create a new dataframe
# graph_df = pd.DataFrame()
# # for each unique region in the dataframe up to the 16th region
# for region in df['region'].unique()[:16]:
#     print(region)
#     # create a new dataframe with the rows where the region is equal to the current region
#     region_df = df.copy()[df['region'] == region]
#     # set the index of the dataframe to the column 'Date', inplace=True means that the dataframe is updated
#     region_df.set_index('Date', inplace=True)
#     # sort the dataframe by the index
#     region_df.sort_index(inplace=True)
#     # create a new column in the dataframe with the name 'price25ma' and the value of the rolling mean
#     region_df[f'{region}_price25ma'] = region_df['AveragePrice'].rolling(25).mean()

#     # if the graph dataframe is empty
#     if graph_df.empty:
#         # set the graph dataframe to the region dataframe, 2 brackets sets it to a dataframe
#         graph_df = region_df[[f'{region}_price25ma']]
#     else:
#         # join the region dataframe to the graph dataframe
#         graph_df = graph_df.join(region_df[[f'{region}_price25ma']])

# # # drop the rows with NaN values
# # albany_df['AveragePrice'].plot()
# # albany_df.dropna(inplace=True)
# # plt.show()