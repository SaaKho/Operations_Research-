import pulp
from pulp import *

my_lp_problem= LpProblem("LinearProblem",LpMaximize)

# Defining the decision variables.
x1 = LpVariable('the number of Delta assemblies produced daily i.e(x1)',0)
x2 = LpVariable('the number of Omega assemblies produced daily i.e(x2)',0)
x3 = LpVariable('the number of Theta assemblies produced daily i.e(x3)',0)

# Defining Objective function
my_lp_problem += 800*x1 + 900*x2 + 600*x3

my_lp_problem += x1 + x2 + x3 <= 7, "(X70686 chips)"
my_lp_problem += 2*x1 + x2 + x3 <= 8, "(Production hours)"
my_lp_problem += 80*x1 + 160*x2 + 80*x3 <= 480, "(Quality minutes)"

# print the problem
print(my_lp_problem)

# solve the problem
print(my_lp_problem.solve())

#Print the status of the problem
print(LpStatus[my_lp_problem.status])

# print the values of the decision variables
for variable in my_lp_problem.variables():
    print("{}={}".format(variable.name,variable.varValue))

# print the objective function value
print("Objective Function: ",pulp.value(my_lp_problem.objective))





