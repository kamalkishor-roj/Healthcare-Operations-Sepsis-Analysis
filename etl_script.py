import xml.etree.ElementTree as ET
import pandas as pd

# 1. Parse the XML File
print("Loading data...")
tree = ET.parse(r"C:\Users\91930\OneDrive\Desktop\resume projects\Sepsis Cases - Event Log_1_all\Sepsis Cases - Event Log.xes\Sepsis Cases - Event Log.xes") # Make sure filename matches exactly
root = tree.getroot()

data = []

# 2. Extract Data (Loop through every patient 'Trace')
for trace in root.findall('trace'):
    case_id = "Unknown"
    
    # Get Patient ID
    for string_tag in trace.findall('string'):
        if string_tag.get('key') == 'concept:name':
            case_id = string_tag.get('value')
            break
            
    # Get Events (Arrival, Triage, Antibiotics, etc.)
    for event in trace.findall('event'):
        activity = None
        timestamp = None
        
        for string_tag in event.findall('string'):
            if string_tag.get('key') == 'concept:name':
                activity = string_tag.get('value')
        
        for date_tag in event.findall('date'):
            if date_tag.get('key') == 'time:timestamp':
                timestamp = date_tag.get('value')

        if case_id and activity and timestamp:
            data.append([case_id, activity, timestamp])

# 3. Save to CSV
df = pd.DataFrame(data, columns=['Case_ID', 'Activity', 'Timestamp'])
df['Timestamp'] = pd.to_datetime(df['Timestamp'], utc=True)
df.to_csv('sepsis_cleaned.csv', index=False)
print(f"Success! Saved {len(df)} rows to 'sepsis_cleaned.csv'.")
