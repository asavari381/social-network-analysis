Python 3.12.3 (v3.12.3:f6650f9ad7, Apr  9 2024, 08:18:48) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> import networkx as nx
... from node2vec import Node2Vec
... 
... # Load the processed data
... data = pd.read_csv('../data/processed_social_network_data.csv')
... 
... # Create a graph
... G = nx.from_pandas_edgelist(data, 'source', 'target', ['weight'])
... 
... # Calculate centrality measures
... pagerank = nx.pagerank(G)
... betweenness = nx.betweenness_centrality(G)
... 
... # Node2Vec for generating embeddings
... node2vec = Node2Vec(G, dimensions=64, walk_length=30, num_walks=200, workers=4)
... model = node2vec.fit(window=10, min_count=1)
... 
... # Save the embeddings and centrality measures
... pd.DataFrame.from_dict(pagerank, orient='index').to_csv('../data/pagerank.csv')
... pd.DataFrame.from_dict(betweenness, orient='index').to_csv('../data/betweenness.csv')
... model.wv.save_word2vec_format('../data/node2vec_embeddings.txt')
