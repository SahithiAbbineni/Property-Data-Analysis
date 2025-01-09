import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_ind

# Load the cleaned data
final_data = pd.read_csv('cleaned_property_data.csv')

# 1. Identifying the most frequent category in 'property_age_category'
print(final_data['property_age_category'].value_counts())

# 2. Correlation Analysis with rent
correlation_matrix = final_data.corr()
print(correlation_matrix['rent'].sort_values(ascending=False))

# 3. Hypothesis Testing: Compare average interactions for properties with and without a gym
gym_properties = final_data[final_data['gym'] == 1]['total_interactions']
no_gym_properties = final_data[final_data['gym'] == 0]['total_interactions']

t_stat, p_value = ttest_ind(gym_properties, no_gym_properties)
if p_value < 0.05:
    print("Reject the null hypothesis (significant difference)")
else:
    print("Fail to reject the null hypothesis (no significant difference)")

# Visualization of correlation
plt.figure(figsize=(10, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix')
plt.show()

# Visualizing the property_age_category distribution
plt.figure(figsize=(8, 6))
final_data['property_age_category'].value_counts().plot(kind='bar', color='skyblue')
plt.title('Property Age Category Distribution')
plt.xlabel('Property Age Category')
plt.ylabel('Count')
plt.show()
