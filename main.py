# pandas intro
import pandas as pd
import numpy as np

# types of pandas data structures:
# 1. Series --> 1-d labeled array
# 2. Dataframe --> 2-d labeled array

s = pd.Series([1, 3, 5, np.nan, 6, 8])

print(s)
