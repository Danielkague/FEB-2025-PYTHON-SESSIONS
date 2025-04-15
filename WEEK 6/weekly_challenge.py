import numpy as np
import requests
import pandas as pd
import matplotlib.pyplot as plt

my_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("array:", my_array)

# Replace with a valid API endpoint and your access key
url = "http://api.ipstack.com/check?access_key=YOUR_ACCESS_KEY"

response = requests.get(url)

try:
    # Parse the JSON response
    events = response.json()

    # Print the JSON response
    print(events)
except requests.exceptions.JSONDecodeError:
    print("Error: The response is not in JSON format.")

data = {
    "name": ["Alice", "Bob", "Charlie", "David"],
    "age": [24, 30, 22, 35],
    "score": [85, 90, 95, 88]
}
df = pd.DataFrame(data)
print("Dataframe:\n", df)
print(df[df["score"] >= 90])  # Filter rows based on a condition
print("array * 2:", my_array * 2)  #multiply each element by 2

plt.plot([1, 2, 3, 4], [5, 6, 7, 8])
plt.show()