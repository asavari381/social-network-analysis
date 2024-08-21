Python 3.12.3 (v3.12.3:f6650f9ad7, Apr  9 2024, 08:18:48) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> import pandas as pd
... import networkx as nx
... 
... # Load the data
... data = pd.read_csv('/Users/nikhilshejwal/Downloads/social-network-analysis')
... 
... # Preprocessing steps: handling missing values, normalization, etc.
... # For simplicity, let's assume the data is already clean
... 
... # Save the processed data
... data.to_csv('/Users/nikhilshejwal/Downloads/social-network-analysis', index=False)
