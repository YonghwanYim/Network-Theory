# import package.
using Pkg
using JuMP, GLPK
using Combinatorics

# length of edge 
m = [1000 13 12 14 1000 1000 1000 1000 1000;
      13 1000 1000 1000 14 1000 1000 1000 1000;
      12 1000 1000 6 10 11 1000 1000 1000;
      14 1000 6 1000 1000 7 1000 1000 1000;
      1000 14 10 1000 1000 9 11 1000 1000;
      1000 1000 11 7 9 1000 5 10 1000;
      1000 1000 1000 1000 11 5 1000 17 16;
      1000 1000 1000 1000 1000 10 17 1000 8;
      1000 1000 1000 1000 1000 1000 16 8 1000]

# Number of Nodes
num_nodes = size(m, 1)

# Generate JuMP model.
model = Model(GLPK.Optimizer)

# LP Relaxation
@variable(model, 0 <= x[1:num_nodes, 1:num_nodes] <= 1)

# Original Problem 
#@variable(model, x[1:num_nodes, 1:num_nodes], Bin)

# Objective Function
@objective(model, Min, sum(adj_matrix[i, j] * x[i, j] for i in 1:num_nodes, j in 1:num_nodes))

# Constraint 1
@constraint(model, sum(x[i, j] for i in 1:num_nodes, j in 1:num_nodes) == num_nodes - 1)

# Constraint 2 (using Combinatorics)
for size in 2:num_nodes
    for subset in combinations(1:num_nodes, size)
        @constraint(model, sum(x[i, j] for i in subset, j in subset) <= size - 1)
    end
end
JuMP.optimize!(model)

println("Optimal Objective Value (LP Relaxation): ", JuMP.objective_value(model))
println("X = ", JuMP.value.(x))
@show raw_status(model)
