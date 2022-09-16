# import matplotlib
import matplotlib.pyplot as plt

#create a dataframe df from the results
df = pd.DataFrame(results)

# Set the DataFrame's column names
df.columns = results[0].keys()

# plot a bar chart of the results
df.plot.bar (x='state', y='population', rot=90, title='Population by State', legend=False, figsize=(10,7), fontsize=12, color='red', alpha=0.5, edgecolor='black', linewidth=1, grid=True)
plt.show()