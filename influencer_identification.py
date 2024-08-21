Python 3.12.3 (v3.12.3:f6650f9ad7, Apr  9 2024, 08:18:48) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
================================ RESTART: Shell ================================
>>> 
================================ RESTART: Shell ================================
>>> 
================================ RESTART: Shell ================================
>>> 
================================ RESTART: Shell ================================
>>> 
================================ RESTART: Shell ================================
>>> 
================================ RESTART: Shell ================================
>>> 
================================ RESTART: Shell ================================
>>> 
================================ RESTART: Shell ================================
>>> 
================================ RESTART: Shell ================================
>>> import pandas as pd
... 
... # Load centrality measures
... pagerank = pd.read_csv('../data/pagerank.csv', header=None, names=['node', 'pagerank'])
... betweenness = pd.read_csv('../data/betweenness.csv', header=None, names=['node', 'betweenness'])
... 
... # Identify top influencers based on PageRank and Betweenness
... influencers = pagerank.sort_values('pagerank', ascending=False).head(10)
... influencers = influencers.merge(betweenness, on='node')
... influencers.to_csv('../results/influencer_results.csv', index=False)
