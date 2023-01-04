import pulp
from pulp import *

my_lp_problem= LpProblem("LinearProblem2",LpMaximize)

# Defining the decision variables.
x1 = LpVariable('x1',0)
x2 = LpVariable('x2',0)
x3 = LpVariable('x3',0)
x4 = LpVariable('x4',0)
x5 = LpVariable('x5',0)

# Defining Objective function
my_lp_problem += 110*x1 + 90*x2 + 75*x3 + 80*x4 + 130*x5

my_lp_problem += 5.5*x1 + 5.2*x2 + 5.0*x3 + 5.1*x4 + 7.5*x5 <= 4800, "Molding/pressing"
my_lp_problem += 4.5*x1 <= 1200 ,"Stove assembly"
my_lp_problem += 4.5*x2 + 4.0*x3 + 3.0*x4 <= 2400 ,"Washer/dryer assembly"
my_lp_problem += 9.0*x5 <= 1200 ,"Refrigerator assembly"
my_lp_problem += 4.0*x1 + 3.0*x2 + 2.5*x3 + 2.0*x4 + 4.0*x5 <= 3000 ,"Packaging"
my_lp_problem += x2 - x3 - x4 ==0 ,"Washers=Dryers"
my_lp_problem += x3 - x4 <= 100, "E.Dryers<=G.Dryers+100"
my_lp_problem +=-x3 + x4 <= 100, "G.Dryers<=E.Dryers+100"



# print the problem
print(my_lp_problem)
#
# # solve the problem
print(my_lp_problem.solve())
#
# # know the status of the problem
print(LpStatus[my_lp_problem.status])
#
# # print the values of the decision variables
for variable in my_lp_problem.variables():
     print("{}={}".format(variable.name,variable.varValue))
#
# # print the objective function value
print("Objective Function: ",pulp.value(my_lp_problem.objective))