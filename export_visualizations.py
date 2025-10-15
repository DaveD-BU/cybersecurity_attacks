#!/usr/bin/env python
# Script to export visualizations from the cybersecurity attacks analysis

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.colors import LinearSegmentedColormap
from datetime import datetime
import os

# Define color palette according to project standards
COLOR_PALETTE = [
    "#c6d4e1",  # light blue-grey
    "#9bbcd4",  # soft blue
    "#6fa3c7",  # medium blue
    "#4a8ab8",  # strong blue
    "#2f6fa1",  # deep blue
    "#1f4f75",  # navy
    "#d3d3d3",  # light grey
    "#a9a9a9",  # medium grey
    "#696969",  # dark grey
]

# Set visualization styles
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette(COLOR_PALETTE)

# Create directories if they don't exist
os.makedirs("reports/visualizations", exist_ok=True)

# Set random seed for reproducibility
np.random.seed(42)

# Load the dataset
file_path = 'cybersecurity_attacks_data/cleaned_cybersecurity_attacks.csv'
df = pd.read_csv(file_path)

# Convert timestamp to datetime
df['Timestamp'] = pd.to_datetime(df['Timestamp'])

# Extract time components
df['Year'] = df['Timestamp'].dt.year
df['Month'] = df['Timestamp'].dt.month
df['Day'] = df['Timestamp'].dt.day
df['Hour'] = df['Timestamp'].dt.hour
df['DayOfWeek'] = df['Timestamp'].dt.dayofweek

# Extract city and state
df[['City', 'State']] = df['Geo-location Data'].str.split(', ', expand=True)

# Create custom colormaps from our palette
custom_heatmap = LinearSegmentedColormap.from_list('custom_blues', [COLOR_PALETTE[0], COLOR_PALETTE[4]], N=100)
custom_diverging = LinearSegmentedColormap.from_list('custom_diverging', 
                                                [COLOR_PALETTE[5], COLOR_PALETTE[6], COLOR_PALETTE[2]], N=100)

# 1. Attack Types Distribution
plt.figure(figsize=(12, 6))
attack_counts = df['Attack Type'].value_counts()
# Create a temporary dataframe for plotting
temp_df = pd.DataFrame({'Attack Type': attack_counts.index, 'Count': attack_counts.values})
sns.barplot(data=temp_df, x='Attack Type', y='Count', hue='Attack Type', palette=COLOR_PALETTE[:len(attack_counts)], legend=False)
plt.title('Distribution of Attack Types')
plt.xlabel('Attack Type')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('reports/visualizations/attack_types_distribution.png', dpi=300)
plt.close()

# 2. Severity Levels Distribution
plt.figure(figsize=(10, 6))
severity_counts = df['Severity Level'].value_counts()
sns.countplot(x='Severity Level', data=df, order=severity_counts.index)
plt.title('Distribution of Severity Levels')
plt.xlabel('Severity Level')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('reports/visualizations/severity_levels_distribution.png', dpi=300)
plt.close()

# 3. Protocol Distribution
plt.figure(figsize=(10, 6))
protocol_counts = df['Protocol'].value_counts()
sns.countplot(x='Protocol', data=df, order=protocol_counts.index)
plt.title('Distribution of Protocols')
plt.xlabel('Protocol')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('reports/visualizations/protocol_distribution.png', dpi=300)
plt.close()

# 4. Attacks by Year
plt.figure(figsize=(12, 6))
year_counts = df['Year'].value_counts().sort_index()
sns.barplot(x=year_counts.index, y=year_counts.values)
plt.title('Attacks by Year')
plt.xlabel('Year')
plt.ylabel('Number of Attacks')
plt.tight_layout()
plt.savefig('reports/visualizations/attacks_by_year.png', dpi=300)
plt.close()

# 5. Attacks by Day of Week
plt.figure(figsize=(12, 6))
day_counts = df['DayOfWeek'].value_counts().sort_index()
sns.barplot(x=day_counts.index, y=day_counts.values)
plt.title('Attacks by Day of Week')
plt.xlabel('Day of Week')
plt.ylabel('Number of Attacks')
plt.xticks(range(7), ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
plt.tight_layout()
plt.savefig('reports/visualizations/attacks_by_dayofweek.png', dpi=300)
plt.close()

# 6. Heatmap: Attack Type vs Protocol
plt.figure(figsize=(12, 8))
attack_protocol_crosstab = pd.crosstab(df['Attack Type'], df['Protocol'])
sns.heatmap(attack_protocol_crosstab, annot=True, fmt='d', cmap='viridis', cbar_kws={'label': 'Count'})
plt.title('Relationship Between Attack Types and Protocols')
plt.xlabel('Protocol')
plt.ylabel('Attack Type')
plt.tight_layout()
plt.savefig('reports/visualizations/attack_protocol_heatmap.png', dpi=300)
plt.close()

# 7. Anomaly Score Distribution
plt.figure(figsize=(12, 6))
sns.histplot(df['Anomaly Scores'], bins=50, kde=True)
plt.title('Distribution of Anomaly Scores')
plt.xlabel('Anomaly Score')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('reports/visualizations/anomaly_scores_distribution.png', dpi=300)
plt.close()

# 8. Network Segment Analysis
plt.figure(figsize=(14, 8))
segment_attack_crosstab = pd.crosstab(df['Network Segment'], df['Attack Type'])
sns.heatmap(segment_attack_crosstab, annot=True, fmt='d', cmap='viridis', cbar_kws={'label': 'Count'})
plt.title('Network Segment by Attack Type')
plt.tight_layout()
plt.savefig('reports/visualizations/network_segment_attack_heatmap.png', dpi=300)
plt.close()

# 9. Top 10 Cities
plt.figure(figsize=(12, 6))
top_cities = df['City'].value_counts().head(10)
sns.barplot(x=top_cities.index, y=top_cities.values)
plt.title('Top 10 Cities with Most Attacks')
plt.xlabel('City')
plt.ylabel('Number of Attacks')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('reports/visualizations/top_cities.png', dpi=300)
plt.close()

# 10. Actions Taken by Attack Type
plt.figure(figsize=(14, 8))
action_attack_crosstab = pd.crosstab(df['Action Taken'], df['Attack Type'])
sns.heatmap(action_attack_crosstab, annot=True, fmt='d', cmap='viridis', cbar_kws={'label': 'Count'})
plt.title('Actions Taken by Attack Type')
plt.tight_layout()
plt.savefig('reports/visualizations/actions_by_attack_heatmap.png', dpi=300)
plt.close()

print("Visualizations exported successfully to the reports/visualizations directory!")