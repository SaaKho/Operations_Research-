from pulp import *

prob = LpProblem("Linear Problem 10", LpMinimize)  

#Defining the Decision Variable
X1 = LpVariable("X1", lowBound=0) 
X2 = LpVariable("X2", lowBound=0) 
X3 = LpVariable("X3", lowBound=0) 
X4 = LpVariable("X4", lowBound=0) 
X5 = LpVariable("X5", lowBound=0) 


#Defining the Objective Function
prob +=12*X1 + 9*X2 + 9*X3 + 15*X4 

prob += 30*X1 + 30*X2 + 20*X3 + 20*X4 >= 50
prob +=25*X1 + 2*X2 + 100*X3 + 25*X4 >= 50
prob +=25*X1 + 25*X2 + 25*X3 + 25*X4 >= 50 
prob +=25*X1 + 25*X2 + 100*X3 + 25*X4 >= 50
prob +=45*X1 + 45*X2 + 100*X3 + 25*X4 >= 50
prob += 1*X1 + 1*X2 + 1*X3 + 1*X4 - 1*X5 == 0
prob += 1*X1 - 0.1*X5 >= 0  
prob += 1*X2 - 0.1*X5 >= 0 
prob += 1*X3 - 0.1*X5 >= 0  
prob += 1*X4 - 0.1*X5 >= 0  


# print the problem
print(prob)

#Solving the Problem
prob.solve()
value(X1), value(X2), value(X3),value(X4),value(X5) ,value(prob.objective)  

# # know the status of the problem
print(LpStatus[prob.status])
#
#print the values of the decision variables
for variable in prob.variables():
    print("{}={}".format(variable.name,variable.varValue))

# # print the objective function value
print("Objective Function: ",pulp.value(prob.objective))




