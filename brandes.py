import pandas as pd
import networkx as nx

# Load dataset
df = pd.read_csv("datasets/musae_facebook_edges.csv")

print("Columns:", df.columns)

# Create graph
G = nx.from_pandas_edgelist(df, 'id_1', 'id_2')

print("Nodes:", G.number_of_nodes())
print("Edges:", G.number_of_edges())

# Brandes algorithm (betweenness centrality)
bc = nx.betweenness_centrality(G, k=100)  # faster

# Top nodes
top = sorted(bc.items(), key=lambda x: x[1], reverse=True)[:10]

print("\nTop Influencers:")
for node, score in top:
    print(node, round(score, 4))