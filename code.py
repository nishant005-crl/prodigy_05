import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from io import StringIO

# Simulated accident dataset
data = StringIO("""Date,Time,Severity,Weather,Road_Condition,Location
2023-06-01,07:45,2,Clear,Dry,Los Angeles
2023-06-01,23:15,3,Rain,Wet,New York
2023-06-02,12:30,1,Clear,Dry,Chicago
2023-06-02,18:45,2,Snow,Snowy,Denver
2023-06-03,06:00,3,Fog,Foggy,Seattle
2023-06-03,22:15,2,Rain,Wet,Houston
2023-06-04,14:10,1,Clear,Dry,San Francisco
2023-06-04,20:30,3,Rain,Wet,New York
2023-06-05,09:00,2,Clear,Dry,Los Angeles
2023-06-05,17:45,3,Rain,Wet,Chicago
""")

# Read the dataset
df = pd.read_csv(data, parse_dates=['Date'])

# Extract hour for time-based analysis
df['Hour'] = pd.to_datetime(df['Time'], format='%H:%M').dt.hour

# ----------------- Plot 1: Severity by Weather -------------------
plt.figure(figsize=(8, 6))
sns.countplot(data=df, x='Weather', hue='Severity', palette='Set3')
plt.title("Accident Severity by Weather Conditions")
plt.xlabel("Weather")
plt.ylabel("Number of Accidents")
plt.legend(title="Severity")
plt.tight_layout()
plt.show()

# ----------------- Plot 2: Road Condition Impact ------------------
plt.figure(figsize=(8, 6))
sns.countplot(data=df, x='Road_Condition', palette='Set2')
plt.title("Number of Accidents by Road Condition")
plt.xlabel("Road Condition")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

# ----------------- Plot 3: Time of Day Pattern --------------------
plt.figure(figsize=(8, 6))
sns.histplot(df['Hour'], bins=8, kde=True, color="orange")
plt.title("Accidents by Hour of Day")
plt.xlabel("Hour")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# ----------------- Plot 4: Accident Locations ---------------------
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='Location', palette='coolwarm')
plt.title("Accidents by Location")
plt.xlabel("City")
plt.ylabel("Number of Accidents")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

