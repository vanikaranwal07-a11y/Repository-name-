import pandas as pd
df = pd.read_csv("data/tickets.csv")
print(df.info())
print(df["category"].value_counts())
print(df["priority"].value_counts())
print(df["text"].str.len().describe())