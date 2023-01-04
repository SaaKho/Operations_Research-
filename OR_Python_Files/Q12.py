from pulp import *

#Defining the Problem
prob = LpProblem("Linear Problem 12", LpMaximize)  

#Defining the Decision Variable
X1 = LpVariable("X1", lowBound=0) 
X2 = LpVariable("X2", lowBound=0) 
X3 = LpVariable("X3", lowBound=0) 
X4 = LpVariable("X4", lowBound=0) 


#Defining the Objective Function
prob +=2.50*X1 + 3.25*X2 + 3.90*X3 

prob +=  2*X1 + 3*X2 + 6*X3 <= 1920
prob +=8*X1 + 12*X2 + 14*X3 <= 3840
prob +=1*X2 >= 150
prob +=-2*X1 - 2*X2 + 1*X3 <= 0
prob +=1*X1 + 1*X2 + 1*X3 - 1*X4 == 0
prob += 1*X1 - 0.3*X4 <= 0 
prob

prob.solve()

value(X1), value(X2), value(X3),value(X4) ,value(prob.objective)  

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




