import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data for the Plotly and Seaborn tests
data = {
    'Environment': ['native debian', 'WSL', 'CB v2', 'i5', 'ARMCB'],
    'Plotly Time (ms)': [75, 150, 500, 2000, 750],
    'Seaborn Time (s)': [3, 5, 20, 10, 45]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Convert Plotly times to seconds for consistency
df['Plotly Time (s)'] = df['Plotly Time (ms)'] / 1000

# Melt the DataFrame to make it easier to plot with seaborn
df_melted = df.melt(id_vars='Environment', value_vars=['Plotly Time (s)', 'Seaborn Time (s)'], 
                    var_name='Test', value_name='Time (s)')

# Plotting
plt.figure(figsize=(10, 6))
sns.barplot(x='Environment', y='Time (s)', hue='Test', data=df_melted)
plt.yscale('log')
plt.title('Performance Comparison Across Environments (Log Scale)')
plt.ylabel('Time (s) - Log Scale')
plt.xlabel('Environment')
plt.show()
