# import package.
using Pkg
using Graphs
using SimpleWeightedGraphs

adj_matrix = [
    0 13 12 14 0 0 0 0 0;
    13 0 0 0 14 0 0 0 0;
    12 0 0 6 10 11 0 0 0;
    14 0 6 0 0 7 0 0 0;
    0 14 10 0 0 9 11 0 0;
    0 0 11 7 9 0 5 10 0;
    0 0 0 0 11 5 0 17 16;
    0 0 0 0 0 10 17 0 8;
    0 0 0 0 0 0 16 8 0
]

# Create a SimpleWeightedGraph
g = SimpleWeightedGraph(adj_matrix)

# Kruskal's algorithm
mst_kruskal = kruskal_mst(g)

# Prim's algorithm
mst_prim = prim_mst(g)

# Show results
println("Minimum Spanning Tree (Kruskal):")
println(mst_kruskal)
println("\nMinimum Spanning Tree (Prim):")
println(mst_prim)
