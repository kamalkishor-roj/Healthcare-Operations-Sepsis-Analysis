import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import io

# 1. Load and Clean Data
# We handle the 'quote' issue directly here just in case
print("Loading data...")
try:
    df = pd.read_csv('sepsis_cleaned.csv')
except:
    # Fallback for "quoted" CSVs
    with open('sepsis_cleaned.csv', 'r') as f:
        lines = f.readlines()
    clean_lines = [line.strip().strip('"') for line in lines]
    df = pd.read_csv(io.StringIO('\n'.join(clean_lines)))

df['Timestamp'] = pd.to_datetime(df['Timestamp'], utc=True)

# 2. Extract "Arrival" Events
# We filter for 'ER Registration' to count when patients actually walk in the door
arrivals = df[df['Activity'] == 'ER Registration'].copy()

# 3. Create Time Features
arrivals['Day_of_Week'] = arrivals['Timestamp'].dt.day_name()
arrivals['Hour_of_Day'] = arrivals['Timestamp'].dt.hour

# Fix Sort Order (Mon -> Sun)
days_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
arrivals['Day_of_Week'] = pd.Categorical(arrivals['Day_of_Week'], categories=days_order, ordered=True)

# 4. Build the Pivot Matrix (Day vs Hour)
heatmap_data = arrivals.pivot_table(
    index='Day_of_Week', 
    columns='Hour_of_Day', 
    values='Case_ID', 
    aggfunc='count'
).fillna(0)

# 5. Plot the Heatmap
plt.figure(figsize=(12, 6))
sns.heatmap(heatmap_data, cmap='Reds', annot=True, fmt='g', linewidths=.5)

plt.title('ER Crisis Hours: Patient Volume by Day & Hour', fontsize=16)
plt.xlabel('Hour of Day (0-23)', fontsize=12)
plt.ylabel('Day of Week', fontsize=12)

# 6. Save for Portfolio
plt.savefig('er_volume_heatmap.png', dpi=300, bbox_inches='tight')
print("Success! Heatmap saved as 'er_volume_heatmap.png'")
plt.show()
