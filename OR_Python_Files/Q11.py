from pulp import *
prob = LpProblem("Linear Model 11", LpMinimize)  

#Defining the Decision Variable
X1 = LpVariable("X1", lowBound=0) 
X2 = LpVariable("X2", lowBound=0) 
X3 = LpVariable("X3", lowBound=0) 

#Defining the Objective Function
prob +=140*X1 + 50*X2 + 36*X3 

prob +=100*X1 + 35*X2 + 27*X3 >= 2000000
prob +=1*X1>=5000
prob +=  1*X2 >=4000
prob += 1*X3 >=2300
prob += 1*X1 <=15000
prob += 1*X2 <=15000
prob += 1*X3 <=15000

# print the problem
print(prob)

#Solving the Problem
prob.solve()

# # know the status of the problem
print(LpStatus[prob.status])
#
#print the values of the decision variables
for variable in prob.variables():
    print("{}={}".format(variable.name,variable.varValue))

#
# # print the objective function value
print("Objective Function: ",pulp.value(prob.objective))






