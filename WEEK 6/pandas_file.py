import pandas as pd

#create a Dataframe(table-like structure)

data = {
    "name": ["Alice", "Bob", "Charlie", "David"],
    "age": [24, 30, 22, 35],
    "score": [85, 90, 95, 88]
}

df = pd.DataFrame(data)
#print("Dataframe:\n", df)

#print("Names:", df["age"])  # Access a column
print(df[df["score"] >= 90])  # Filter rows based on a condition