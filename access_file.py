import json
import pandas as pd

# Load dataset
with open("C:\\dbms\\FINAL_PROJ\\complaints_dataset.json", "r", encoding="utf-8") as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Quick check
print(df[["Section", "Offence", "Discription"]].head())
print(f"Total IPC entries: {len(df)}")