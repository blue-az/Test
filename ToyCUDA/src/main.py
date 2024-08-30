import cudf
import pandas as pd
import numpy as np
import time

# Generate a large random DataFrame
data_size = int(1e7)  # 10 million rows
df = pd.DataFrame({
    'A': np.random.rand(data_size),
    'B': np.random.rand(data_size),
    'C': np.random.rand(data_size)
})

# Convert to cudf DataFrame
gdf = cudf.DataFrame.from_pandas(df)

# Pandas computation
start_time = time.time()
df['D'] = df['A'] + df['B'] * df['C']
pandas_time = time.time() - start_time

# cudf computation
start_time = time.time()
gdf['D'] = gdf['A'] + gdf['B'] * gdf['C']
cudf_time = time.time() - start_time

print(f"Pandas time: {pandas_time} seconds")
print(f"cuDF time: {cudf_time} seconds")

