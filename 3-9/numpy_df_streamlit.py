# numpy_random.py
import numpy as np
import pandas as pd
import streamlit as st
import random
# c.	Add a streamlit text with  st.write() at top of page
st.write("# Random Data Generator")
# d.	Add the following streamlit slider next: 
num_rows = st.slider("Number of rows", 1, 10000, 500)
# e.	Next add a Numpy random seed of some value between 2-50.
np.random.seed(random.randint(2, 50))

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
# f.	After your for loop, configure streamlit image and progress column
df = pd.DataFrame(data)
st.dataframe(df)
# g.	Next, add a streamlit toggle to enable editing. See coded addendum below.
### continuation of numpy_random.py
data = pd.DataFrame(data)

config = {
    "Preview": st.column_config.ImageColumn(),
    "Progress": st.column_config.ProgressColumn(),
}

if st.toggle("Enable editing"):
    edited_data = st.data_editor(data, column_config=config, use_container_width=True)
else:
    st.dataframe(data, column_config=config, use_container_width=True)

st.subheader("Top 10 Views")
st.line_chart(data["Views"].head(10))

