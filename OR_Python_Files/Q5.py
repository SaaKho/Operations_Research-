from pulp import*
import matplotlib.pyplot as plt
import numpy as np

# create an object of a model
prob = LpProblem("Simple_Lp_Problem", LpMaximize)

# Defining decision variables
x1 = LpVariable("x1",120)
x2 = LpVariable("x2",120)
x3 = LpVariable("x3",120)

# Defining the objective Function
prob += 6.50*x1 + 9.00*x2 + 10.00*x3

# Defining the constraints
prob += 3*x1 + 4*x2 + 6*x3 <= 2700, "1st constraint"
prob += 55*x1 + 75*x2 + 95*x3 <= 48000, "2nd constraint"
prob += 3*x1 + 5*x2 + 6*x3 <= 3000, "3rd constraint"
prob += 5*x1 + 6*x2 + 8*x3 <= 12000, "4th constraint"

# solve the linear programming problem
prob.solve()

# print the result
print("Status: ",LpStatus[prob.status])


#Print the value of the Decision Variables 
for v in prob.variables():
    print(v.name, "=" , v.varValue)

#Print the value of the Optimal Solution
print("The optimal value of the objective function is = ", value(prob.objective))







