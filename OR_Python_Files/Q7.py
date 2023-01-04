from pulp import*
import matplotlib.pyplot as plt
import numpy as np

#Initializing the Problem
my_lp_problem= LpProblem("LinearProblem",LpMaximize)

#Defining the variables
x1 = LpVariable('x1',0)
x2 = LpVariable('x2',0)
x3 = LpVariable('x3',0)
x4 = LpVariable('x4',0)

# Defining Objective function
my_lp_problem += 70*x1 + 80*x2 + 130*x3 + 150*x4

my_lp_problem +=  x3  >= 100,"(Contract)"
my_lp_problem += 0.4*x1 + 0.5*x2 + 0.6*x3 + 0.8*x4 <= 750, "(Production Hours)"
my_lp_problem += x1 +  x3 <= 700 ,"(Celeron)"
my_lp_problem += x2 + x4 <= 550, "(Pentium)"
my_lp_problem += x1 + x2 + x3  <= 800 ,"(20gb Hard Drives)"
my_lp_problem += x4 <= 950, "(30gb Hard Drives)"
my_lp_problem += x1 + x2 + 2*x3 + x4 <= 1600, "(Floppy Drives)"
my_lp_problem += x1 + x2 + x4 <= 1000, "(Zip Drives)"
my_lp_problem += x1 + x3 + x4 <= 1600, "(CD R/W's)"
my_lp_problem += x2 + x3 + x4 <= 900, "(DVD's)"
my_lp_problem += x1 + x2 <= 850, "(15-in. monitors)"
my_lp_problem += x3 + x4 <= 800, "(17-in. monitors)"
my_lp_problem += x2 + x3 <= 1250, "(Mini-tower cases)"
my_lp_problem += x1 + x4 <= 750, "(Tower cases)"

# #print the problem
print(my_lp_problem)

# #solve the problem
print(my_lp_problem.solve())


#Print the Status of the Linear Programming Problem
print(LpStatus[my_lp_problem.status])

#Print the values of the Decision Variables
for variable in my_lp_problem.variables():
    print("{}={}".format(variable.name,variable.varValue))

#Print the Value of the Objective Function
print("Objective Function: ",pulp.value(my_lp_problem.objective))





