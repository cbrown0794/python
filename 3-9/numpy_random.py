# numpy_random.py
import numpy as np
import pandas as pd
num_rows = 5
data = []
for i in range(num_rows):
    data.append(
        {
            "Preview": f"https://picsum.photos/400/200?lock={i}",
            "Views": np.random.randint(0, 1000),
            "Active": np.random.choice([True, False]),
            "Category": np.random.choice(["🤖 LLM", "📊 Data", "⚙️ Tool"]),
            "Progress": np.random.randint(1, 100),
        }
    )
# a.	Add a print statement for ‘data’.
print(data)
#  b.	Convert the ‘data’ into a DataFrame object, then print that object
df = pd.DataFrame(data)
print(df)